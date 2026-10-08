#!/usr/bin/env python3
# Check de entrega · Bootcamp QA con IA (AcademiaQA)
# Revisa tu repo antes de que lo vea un reclutador: plantillas sin completar, datos personales,
# copias del repo de referencia, secretos y emails de commit. Solo usa git y python3.
import os, re, subprocess, sys, urllib.request

REF_REPO = 'Simonethg/ejemplo-portafolio-qa'
HASHES_URL = 'https://raw.githubusercontent.com/%s/main/checks/hashes-referencia.txt' % REF_REPO
REPO = os.environ.get('REPO') or os.environ.get('GITHUB_REPOSITORY', '')
ES_REFERENCIA = REPO.lower() == REF_REPO.lower() or os.environ.get('ES_REFERENCIA') == '1'
EN_ACTIONS = os.environ.get('GITHUB_ACTIONS') == 'true'

errores, avisos = [], []

def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True).stdout

def reportar(lista, tipo, archivo, linea, que, como):
    lista.append((tipo, archivo, linea, que, como))

def error(archivo, linea, que, como): reportar(errores, 'ERROR', archivo, linea, que, como)
def aviso(archivo, linea, que, como): reportar(avisos, 'AVISO', archivo, linea, que, como)

SUBIR = 'Después: git add <archivo>, git commit -m "Corrijo el check de entrega" y git push.'

# ---------- archivos del repo ----------
ls = [l.split('\t', 1) for l in git('ls-files', '-s', '-z').split('\0') if l]
archivos = {}  # ruta -> hash blob
for meta, ruta in ls:
    archivos[ruta] = meta.split()[1]

PROPIOS_DEL_CHECK = ('checks/', '.github/workflows/entrega.yml')
def es_del_check(r): return r.startswith(PROPIOS_DEL_CHECK[0]) or r == PROPIOS_DEL_CHECK[1]
def es_plantilla(r):
    return 'plantilla' in r.lower() or r.startswith('.github/ISSUE_TEMPLATE/') or r.startswith('.github/PULL_REQUEST_TEMPLATE')
TEXTO = ('.md', '.csv', '.txt', '.json', '.ts', '.js', '.yml', '.yaml', '.sql', '.html', '.env', '.py', '.sh')
def es_texto(r):
    b = os.path.basename(r)
    return r.endswith(TEXTO) or b.startswith('.env') or b in ('.gitignore', 'README', 'LICENSE')

def leer(r):
    try:
        with open(r, encoding='utf-8', errors='replace') as f: return f.read().split('\n')
    except Exception: return []

def sin_codigo(lineas, es_md):
    """Devuelve (nro, texto) sin bloques ``` ni `código en línea` (solo para Markdown)."""
    en_bloque = False
    for i, l in enumerate(lineas, 1):
        if es_md and l.lstrip().startswith(('```', '~~~')):
            en_bloque = not en_bloque; continue
        if en_bloque: continue
        yield i, (re.sub(r'`[^`]*`', '', l) if es_md else l)

# ---------- 1. corchetes de plantilla ----------
EXACTOS = {s.lower() for s in [
    'tu nombre', 'tu ciudad', 'tu país', 'tu pais', 'tu email', 'tu-usuario', 'tu usuario', 'tu texto corregido',
    'tarea real en lenguaje QA', 'tu formación: cursos y estudios', 'tu nivel real', 'tu primera versión',
    'tu perfil verificado, con las palabras clave del aviso', 'palabras clave reales del aviso',
    'qué hiciste, con números reales', 'un riesgo que encontraste vos y la IA no vio', 'característica', 'riesgo',
    'riesgo de la IA', 'por qué', 'por qué no aplica a MiniModa', 'por qué no se puede probar', 'captura', 'caso',
    'caso de la IA', 'criterio de la IA', 'cómo', 'cómo lo corregí', 'qué corregí', 'qué hizo mal', 'fecha', 'N',
    'ej. inventó una función', 'pegala acá', 'pegá la respuesta de la IA sin tocar', 'ninguno / cuál', 'cambio',
    'flujo', 'mejora', 'tema', 'pregunta', 'pregunta de IA', '1-5', 'paso', 'aaaa-mm-dd', 'R-xx', 'CP-xxx',
    'Chrome xx', 'SO', 'Crítica / Alta / Media / Baja', 'BUG', 'segundo proyecto']}
INICIOS = ('tu ', 'tus ', 'tu-', 'qué ', 'cómo ', 'por qué', 'ej. ', 'ej: ', 'pegá', 'pegala', 'completá', 'escribí ', 'describí ', 'tu versión')
TOKENS = re.compile(r'TU-USUARIO|URL-DE-TU-REPO|ID\+tu-usuario|TU-REPO')
CORCHETE = re.compile(r'(?<!!)\[([^\[\]\n]{1,90})\](?![(\[:])')

def es_placeholder(t):
    s = t.strip(); low = s.lower()
    if s in ('', 'x', 'X', ' ') or s.startswith('^'): return False
    if re.fullmatch(r'[A-Z]{1,6}-\d+', s): return False      # IDs: BUG-001, R-01
    if low in EXACTOS: return True
    return low.startswith(INICIOS)

for r in sorted(archivos):
    if es_del_check(r) or es_plantilla(r) or not r.endswith(('.md', '.csv', '.txt')): continue
    if ES_REFERENCIA and r.startswith('perfil-ejemplo/'): continue  # perfil de muestra con huecos a propósito
    for n, l in sin_codigo(leer(r), r.endswith('.md')):
        if re.match(r'\s*[-*]\s\[[ xX]\]', l): l = re.sub(r'\[[ xX]\]', '', l, count=1)
        for m in CORCHETE.finditer(l):
            if es_placeholder(m.group(1)):
                error(r, n, 'Quedó un espacio de la plantilla sin completar: «[%s]».' % m.group(1),
                      'Cambialo por tu dato real (sin los corchetes) o borrá esa parte si no aplica. ' + SUBIR)
        for m in TOKENS.finditer(l):
            error(r, n, 'Quedó «%s» de la plantilla.' % m.group(0),
                  'Cambialo por tu usuario o tu link de GitHub reales. ' + SUBIR)

# ---------- 2. teléfonos y direcciones ----------
EXENTOS_DATOS = ('test-data/', 'tests/', 'api-tests/')
FICTICIO = re.compile(r'\b(ficticio|ficticia|ficticios|ficticias|de prueba|inventad[oa]|fals[oa])\b', re.I)
CLAVE_TEL = re.compile(r'\b(tel|tel\.|tél|teléfono|telefono|cel|celular|whats ?app|wsp|wpp|móvil|movil|phone)\b', re.I)
CAND_TEL = re.compile(r'(?<![\w+/.-])(\+?\(?\d[\d\s().-]{6,20}\d)(?![\w/])')
DIR = re.compile(r'\b(calle|av\.|avda\.?|avenida|pasaje|pje\.|bv\.|bulevar|boulevard|diagonal)\s+[A-Za-zÁÉÍÓÚÑáéíóúñü0-9 .]{2,40}?\s\d{1,5}\b'
                 r'|\b(piso|depto\.?|dpto\.?|departamento)\s*\d', re.I)

def parece_telefono(c, linea):
    d = re.sub(r'\D', '', c)
    if not 8 <= len(d) <= 13: return False
    if re.fullmatch(r'\d{4}[-/.]\d{1,2}[-/.]\d{1,2}|\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}', c.strip()): return False  # fechas
    if re.fullmatch(r'\d{1,3}(\.\d{3})+', c.strip()): return False                                          # precios / DNI con puntos
    if re.fullmatch(r'[\d.]+', c.strip()): return False                                                     # versiones, decimales
    con_sep = re.search(r'[\s().-]', c.strip()) is not None
    if c.strip().startswith('+') and len(d) >= 10: return True
    if CLAVE_TEL.search(linea) and con_sep: return True
    if CLAVE_TEL.search(linea) and len(d) >= 10: return True
    return re.fullmatch(r'\(?\d{2,4}\)?[\s-]\d{3,4}[\s-]\d{4}', c.strip()) is not None and len(d) in (10, 11)

for r in sorted(archivos):
    if es_del_check(r) or r.startswith(EXENTOS_DATOS) or not es_texto(r) or r.endswith(('.json', 'package-lock.json')): continue
    for n, l in enumerate(leer(r), 1):
        if FICTICIO.search(l): continue
        for m in CAND_TEL.finditer(l):
            if parece_telefono(m.group(1), l):
                error(r, n, 'Parece un número de teléfono: «%s».' % m.group(1).strip(),
                      'Tu teléfono va solo en el CV que mandás en privado, nunca en GitHub. Borralo. '
                      'Si es un dato de prueba inventado, aclaralo en la misma línea con la palabra «ficticio». ' + SUBIR)
                break
        m = DIR.search(l)
        if m:
            error(r, n, 'Parece una dirección: «%s».' % m.group(0),
                  'Tu dirección no va en GitHub (solo ciudad y país). Borrala. '
                  'Si es un dato de prueba inventado, aclaralo en la misma línea con la palabra «ficticio». ' + SUBIR)

# ---------- 3. rastros de Lucía y copias de la referencia ----------
if not ES_REFERENCIA:
    autor = git('log', '-1', '--format=%an').strip().lower()
    MARCAS = [
        (re.compile(r'lucia\.qa@example\.com', re.I), 'el email de Lucía (la alumna ficticia del ejemplo)'),
        (re.compile(r'Ejemplo con \*\*|Desde acá, el README de|Cómo armar y subir TU repo|Estás viendo \*\*`v\d\d'), 'el texto del repo de ejemplo'),
        (re.compile(r'\[NO ESTÁ EN LA FICHA\]'), 'una marca del repo de ejemplo'),
        (re.compile(r'\b(Lucía|Lucia)\b'), 'el nombre de Lucía (la alumna ficticia del ejemplo)'),
    ]
    for r in sorted(archivos):
        if es_del_check(r) or not es_texto(r): continue
        for n, l in enumerate(leer(r), 1):
            for rx, que in MARCAS:
                if rx.search(l):
                    if 'nombre de Lucía' in que and ('lucía' in autor or 'lucia' in autor): continue  # te llamás Lucía
                    error(r, n, 'Tiene %s: «%s».' % (que, rx.search(l).group(0)),
                          'Esto viene del repo de ejemplo. Escribí este archivo con tus propios datos y hallazgos. ' + SUBIR)
                    break
    for prohibido, que in (('docs/00-primeros-pasos.md', 'la guía de primeros pasos'), ('perfil-ejemplo/', 'el perfil de ejemplo')):
        for r in archivos:
            if r == prohibido or r.startswith(prohibido) and prohibido.endswith('/'):
                error(r, 1, 'Este archivo es del repo de ejemplo (%s) y no va en tu repo.' % que,
                      'Borralo de tu repo: git rm -r %s, git commit -m "Saco archivos del ejemplo" y git push.' % prohibido)
                break
    # archivos idénticos byte a byte
    lineas = []
    try:
        with urllib.request.urlopen(HASHES_URL, timeout=10) as resp: lineas = resp.read().decode().split('\n')
    except Exception:
        if os.path.exists('checks/hashes-referencia.txt'):
            lineas = open('checks/hashes-referencia.txt', encoding='utf-8').read().split('\n')
            aviso('checks/hashes-referencia.txt', 1, 'No pude bajar la lista nueva de la referencia; usé la copia local.', 'No hace falta que hagas nada.')
    ref = {}
    for l in lineas:
        p = l.split(' ', 2)
        if len(p) == 3 and not l.startswith('#'): ref[p[0]] = (p[1], p[2])
    IGUALES_PARA_TODOS = ('package-lock.json', '.gitignore', 'LICENSE', 'playwright.config.ts', 'tests/example.spec.ts',
                          '.github/workflows/playwright.yml', '.github/workflows/entrega.yml')
    for r, h in sorted(archivos.items()):
        if r == 'docs/00-primeros-pasos.md' or r.startswith('perfil-ejemplo/'): continue  # ya reportado arriba
        if es_del_check(r) or es_plantilla(r) or r in IGUALES_PARA_TODOS or os.path.basename(r) in ('.gitignore', 'LICENSE', 'package-lock.json'): continue
        try:
            if os.path.getsize(r) < 256: continue  # archivos mínimos (se escriben iguales sin copiar)
        except OSError: continue
        if h in ref:
            rama, ruta = ref[h]
            error(r, 1, 'Es idéntico (byte a byte) a «%s» de la rama %s del repo de ejemplo.' % (ruta, rama),
                  'Hacelo vos: tu captura, tus casos, tus consultas. Copiar el ejemplo se detecta y no muestra tu trabajo. ' + SUBIR)

# ---------- 4. secretos ----------
for r in archivos:
    b = os.path.basename(r)
    if b == '.env' or (b.startswith('.env.') and b not in ('.env.example', '.env.ejemplo')):
        error(r, 1, 'Subiste un archivo .env (ahí van claves y contraseñas).',
              'Sacalo del repo sin borrarlo de tu compu: git rm --cached %s, sumá .env al .gitignore, git commit y git push. '
              'Si tenía una clave real, cambiala ya: queda en el historial.' % r)
nm = [r for r in archivos if r.startswith('node_modules/') or '/node_modules/' in r]
if nm:
    error(nm[0], 1, 'Subiste la carpeta node_modules (%d archivos): se regenera con npm install y no va al repo.' % len(nm),
          'git rm -r --cached node_modules, sumá node_modules/ al .gitignore, git commit y git push.')
gi = leer('.gitignore') if '.gitignore' in archivos else None
if gi is None:
    error('.gitignore', 1, 'Tu repo no tiene .gitignore.', 'Crealo como en la guía T1 (paso «Repo creado + .gitignore»), git add .gitignore, git commit y git push.')
else:
    g = [l.strip() for l in gi]
    if not any(re.fullmatch(r'/?\.env(\*|\.\*)?', l) for l in g):
        error('.gitignore', 1, 'Tu .gitignore no tiene la línea .env.', 'Agregá una línea que diga .env (y otra .env.*). ' + SUBIR)
    if not any(re.fullmatch(r'/?node_modules/?', l) for l in g):
        error('.gitignore', 1, 'Tu .gitignore no tiene la línea node_modules/.', 'Agregá una línea que diga node_modules/. ' + SUBIR)
CLAVES = [
    (r'gh[pousr]_[A-Za-z0-9]{36}', 'un token de GitHub'), (r'github_pat_[A-Za-z0-9_]{40,}', 'un token de GitHub'),
    (r'AIza[0-9A-Za-z_-]{35}', 'una clave de Google (Gemini/Firebase)'), (r'sk-(proj-|ant-)?[A-Za-z0-9_-]{20,}', 'una clave de IA (OpenAI/Anthropic)'),
    (r'-----BEGIN [A-Z ]*PRIVATE KEY-----', 'una clave privada'), (r'AKIA[0-9A-Z]{16}', 'una clave de AWS'),
    (r'xox[baprs]-[A-Za-z0-9-]{10,}', 'un token de Slack'), (r'PMAK-[a-f0-9]{24}-[a-f0-9]{34}', 'una clave de Postman'),
]
CLAVES = [(re.compile(p), q) for p, q in CLAVES]
for r in sorted(archivos):
    if es_del_check(r) or not es_texto(r) or r.endswith('package-lock.json'): continue
    for n, l in enumerate(leer(r), 1):
        for rx, que in CLAVES:
            if rx.search(l):
                error(r, n, 'Parece %s.' % que, 'Borrala del archivo y revocala YA en el sitio que la creó: aunque la borres, '
                      'queda en el historial de GitHub. Las claves van en .env (que no se sube) o en los secrets del repo. ' + SUBIR)
                break

# ---------- 5. emails de los commits ----------
def ok_mail(m): m = m.lower(); return m.endswith('@users.noreply.github.com') or m == 'noreply@github.com'
def tapar(m): u, _, d = m.partition('@'); return (u[:1] + '***@' + d) if d else '***'
CERO = '0' * 40
antes = os.environ.get('ANTES', ''); base = os.environ.get('BASE', '')
desde = base or antes
if desde and desde != CERO and git('cat-file', '-t', desde).strip() == 'commit':
    nuevos = set(git('rev-list', '%s..HEAD' % desde).split())
else:
    nuevos = {git('rev-parse', 'HEAD').strip()}
COMO_MAIL = ('Activá «Keep my email addresses private» y «Block command line pushes that expose my email» en '
             'https://github.com/settings/emails y en la terminal corré: git config --global user.email '
             '"<tu email noreply de esa página>". El próximo commit ya sale bien.')
viejos_mal = 0
for l in git('log', '--format=%H%x09%P%x09%an%x09%ae%x09%cn%x09%ce').split('\n'):
    if not l: continue
    h, padres, an, ae, cn, ce = l.split('\t')
    malos = [m for m in (ae, ce) if not ok_mail(m)]
    if not malos: continue
    if not padres and ce.lower() == 'noreply@github.com':
        aviso('(commit %s)' % h[:7], 0, 'El primer commit lo creó GitHub con tu email personal (%s): ya es público y no se puede '
              'cambiar sin reescribir la historia.' % tapar(malos[0]),
              'No hace falta tocar nada. Para que no vuelva a pasar: ' + COMO_MAIL)
    elif h in nuevos:
        error('(commit %s)' % h[:7], 0, 'Este commit usa un email que no es el noreply de GitHub (%s): queda público.' % tapar(malos[0]), COMO_MAIL)
    else:
        viejos_mal += 1
if viejos_mal:
    aviso('(historial)', 0, '%d commit(s) anteriores usan un email que no es noreply.' % viejos_mal,
          'No hace falta reescribir nada. Desde ahora: ' + COMO_MAIL)

# ---------- salida ----------
def anotar(tipo, f, n, que, como):
    if not EN_ACTIONS: return
    nivel = 'error' if tipo == 'ERROR' else 'warning'
    msg = (que + ' Cómo arreglarlo: ' + como).replace('%', '%25').replace('\n', '%0A')
    if f.startswith('('): print('::%s title=Check de entrega::%s %s' % (nivel, f, msg))
    else: print('::%s file=%s,line=%d,title=Check de entrega::%s' % (nivel, f, max(n, 1), msg))

print('=' * 70)
print('CHECK DE ENTREGA · %s' % ('repo de referencia (sin reglas de Lucía ni de copia)' if ES_REFERENCIA else 'tu repo'))
print('=' * 70)
for tipo, f, n, que, como in errores + avisos:
    donde = f if f.startswith('(') else ('%s, línea %d' % (f, n) if n > 1 else f)
    print('\n%s · %s\n  Qué pasa: %s\n  Cómo arreglarlo: %s' % (tipo, donde, que, como))
    anotar(tipo, f, n, que, como)
print('\n' + '-' * 70)
if errores:
    print('RESULTADO: %d error(es) y %d aviso(s). Arreglá los ERROR y volvé a subir. Los AVISO no hacen fallar el check.' % (len(errores), len(avisos)))
else:
    print('RESULTADO: todo bien (%d aviso(s)). ¡Tu entrega pasó el check!' % len(avisos))
if os.environ.get('GITHUB_STEP_SUMMARY'):
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as s:
        s.write('## Check de entrega: %s\n\n' % ('%d error(es)' % len(errores) if errores else 'todo bien'))
        if errores or avisos:
            s.write('| Tipo | Dónde | Qué pasa | Cómo arreglarlo |\n|---|---|---|---|\n')
            for tipo, f, n, que, como in errores + avisos:
                donde = f if f.startswith('(') else '%s:%d' % (f, max(n, 1))
                s.write('| %s | `%s` | %s | %s |\n' % (tipo, donde, que.replace('|', '/'), como.replace('|', '/')))
sys.exit(1 if errores else 0)
