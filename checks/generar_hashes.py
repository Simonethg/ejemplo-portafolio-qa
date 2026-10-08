#!/usr/bin/env python3
# Genera checks/hashes-referencia.txt: hash git blob de cada archivo de cada rama del repo de
# referencia (y de su historia), para que el check de entrega detecte copias idénticas.
# Uso (en un clon con todas las ramas): python3 checks/generar_hashes.py [prefijo-de-refs] > checks/hashes-referencia.txt
import re, subprocess, sys
pref = sys.argv[1] if len(sys.argv) > 1 else 'refs/heads/'
def git(*a): return subprocess.run(['git'] + list(a), capture_output=True, text=True, check=True).stdout
EXCLUIR = ('package-lock.json', '.gitignore', 'LICENSE', 'playwright.config.ts', 'tests/example.spec.ts',
           '.github/workflows/playwright.yml', '.github/workflows/entrega.yml')
def excluido(p, tam):
    b = p.rsplit('/', 1)[-1]
    return (p in EXCLUIR or b in ('.gitignore', 'LICENSE', 'package-lock.json') or p.startswith('checks/')
            or 'plantilla' in p.lower() or p.startswith('.github/ISSUE_TEMPLATE/') or tam < 256)
refs = sorted(r for r in git('for-each-ref', '--format=%(refname)', pref).split() if not r.endswith('/HEAD'))
refs.sort(key=lambda r: (re.match(r'v\d\d', r.rsplit('/', 1)[-1]) is None, r))  # primero las etapas vXX
vistos = {}
for ref in refs:
    rama = ref[len(pref):]
    for c in git('rev-list', '--reverse', ref).split():
        for l in git('ls-tree', '-r', '-l', c).splitlines():
            meta, ruta = l.split('\t', 1)
            _, tipo, h, tam = meta.split()
            if tipo == 'blob' and h not in vistos and not excluido(ruta, int(tam) if tam.isdigit() else 0):
                vistos[h] = (rama, ruta)
print('# hash-blob rama ruta · generado con checks/generar_hashes.py · no editar a mano')
for h, (rama, ruta) in sorted(vistos.items(), key=lambda x: (x[1][0], x[1][1], x[0])):
    print(h, rama, ruta)
