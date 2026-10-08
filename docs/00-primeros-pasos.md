# Primeros pasos: terminal, Git, GitHub e IA

Guía corta para dejar tu compu lista antes de armar tu repo. Copiá y pegá los comandos tal cual. Si un paso ya lo tenés hecho, saltealo.

> Esta guía es parte del repo de referencia: **no va en tu repo**.

## 1. Abrir la terminal

**Windows** (cualquiera de las dos):
- **PowerShell:** tecla Windows → escribí `PowerShell` → Enter.
- **Git Bash:** aparece después de instalar Git (paso 2). Tecla Windows → escribí `Git Bash` → Enter.

**Mac:** `Cmd + Espacio` → escribí `Terminal` → Enter.

**Linux:** `Ctrl + Alt + T` (o buscá "Terminal" en el menú de aplicaciones).

Para probar que funciona:

```bash
echo "Hola, terminal"
```

## 2. Instalar y configurar Git

**Windows** (elegí una opción):
- Descargá el instalador oficial de https://git-scm.com/downloads y dejá las opciones por defecto.
- O en PowerShell:

```powershell
winget install --id Git.Git -e
```

**Mac** (elegí una opción):

```bash
xcode-select --install
```

```bash
brew install git
```

(La segunda solo si ya tenés Homebrew: https://brew.sh)

**Linux (Ubuntu/Debian):**

```bash
sudo apt update && sudo apt install -y git
```

Cerrá y volvé a abrir la terminal, y verificá:

```bash
git --version
```

Configurá tu nombre y tu email (una sola vez):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "ID+tu-usuario@users.noreply.github.com"
```

> **Consejo:** usá el email **noreply** de GitHub, no tu email personal: cada commit publica el email del autor. Lo encontrás en https://github.com/settings/emails (activá también *Keep my email addresses private* y *Block command line pushes that expose my email*).

## 3. Iniciar sesión en GitHub (sin tokens a mano)

Usá siempre la **ventana oficial de login**. Dos opciones:

- **Git Credential Manager** (viene con Git para Windows; en Mac y Linux se instala aparte: https://github.com/git-ecosystem/git-credential-manager). La primera vez que hagas `git push`, se abre el navegador para que entres a GitHub.
- **GitHub CLI** (https://cli.github.com):

```bash
# Windows
winget install --id GitHub.cli -e
# Mac
brew install gh
```

```bash
gh auth login
```

Elegí **GitHub.com** → **HTTPS** → **Login with a web browser** y seguí los pasos en el navegador. Verificá:

```bash
gh auth status
```

> **Nunca** pegues un token o una contraseña en un archivo del repo, en un test, en un `.env` que se suba ni en un chat con IA. Si se te filtró uno, revocalo ya en https://github.com/settings/tokens: borrar el archivo no alcanza, queda en el historial.

## 4. Entrar a una IA gratis

Cualquiera de estas, en su **plan gratuito**, con **tu email propio** y **sin cargar tarjeta**:

- Gemini: https://gemini.google.com
- ChatGPT: https://chatgpt.com
- Claude: https://claude.ai

**Nunca le pegues:**
- Contraseñas, tokens ni claves.
- Datos de clientes ni información de tu empleador (código, URLs internas, capturas de Jira, nombres de clientes).
- Tu teléfono ni tu dirección (ni los de otras personas).

Lo que sí: la URL pública de MiniModa, los textos de la tienda y tus borradores. Lo que la IA te devuelva lo verificás vos en la app y lo anotás en tu `docs/uso-de-ia.md`.

## 5. Crear tu repo y bajarlo a tu compu

1. En GitHub: **+** → **New repository** → nombre `qa-minimoda-ecommerce` → **Public** → tildá **Add a README file** → **Create repository**.
2. Botón verde **Code** → **HTTPS** → copiá la URL.
3. En la terminal (cambiá `TU-USUARIO`):

```bash
cd ~
git clone https://github.com/TU-USUARIO/qa-minimoda-ecommerce.git
cd ~/qa-minimoda-ecommerce
pwd
ls
```

Tenés que ver `README.md`. Desde acá, **todos los comandos se corren dentro de esta carpeta**.

## 6. Subir cada avance

Cada vez que termines un paso:

```bash
cd ~/qa-minimoda-ecommerce
git status
git add README.md docs/
git commit -m "Qué agregaste, en una línea"
git push
```

En `git add` poné los archivos o carpetas de ese paso (cada versión del repo de referencia te dice cuáles). Antes de cada commit, mirá el `git status`: **no** tienen que aparecer `.env`, `auth/`, `playwright/.auth/` ni `node_modules/`.

## 7. Node.js (recién para las pruebas de API y la automatización)

Descargá la versión **LTS** de https://nodejs.org/ (o en Windows: `winget install --id OpenJS.NodeJS.LTS -e`). Cerrá y volvé a abrir la terminal, y verificá:

```bash
node --version
npm --version
```

Más sobre Playwright: https://playwright.dev/docs/intro

## 8. Errores comunes

| Ves esto | Qué pasa | Qué hacer |
|---|---|---|
| `ENOENT` o `no such file or directory` | No estás en la carpeta del repo | `cd ~/qa-minimoda-ecommerce` y chequeá con `ls` que se vea `README.md` |
| `command not found: git` / `node` / `npm` (en Windows: *no se reconoce como nombre de un cmdlet*) | Falta instalar esa herramienta, o la terminal se abrió antes de instalarla | Instalala (pasos 2 y 7), cerrá y volvé a abrir la terminal, y probá `git --version` / `node --version` |
| `npm warn deprecated …` | Avisos de paquetes viejos que usan otras dependencias | Se pueden ignorar: no son errores. Lo que importa es que el comando termine sin `npm error` |
| `found N vulnerabilities` después de `npm install` | Avisos de `npm audit` sobre dependencias de herramientas que corren solo en tu compu | Se pueden ignorar en este proyecto. **No** corras `npm audit fix --force`: puede romper las versiones |
| `rejected … (fetch first)` al hacer `git push` | En GitHub hay cambios que no tenés (por ejemplo, editaste desde la web) | `git pull --rebase` y después `git push` |

## 9. Checklist antes de cada push

- [ ] Ni teléfono ni dirección en README, archivos, capturas, commits ni bio.
- [ ] `git status` sin `.env`, `auth/`, `*.har`, `node_modules/` ni `playwright-report/`.
- [ ] Ningún test ni colección de Postman con usuario, contraseña o token.
- [ ] Solo datos ficticios: emails `@example.com` y tarjetas de prueba.
- [ ] Capturas sin otras pestañas, sin tu mail y sin notificaciones.
- [ ] Nada de tu trabajo actual: ni código, ni URLs internas, ni nombres de clientes.
- [ ] Los proyectos van en "Proyectos", no en "Experiencia"; la formación, solo en "Educación".
- [ ] Cada número tiene una fecha o un run que lo respalda.
- [ ] Si tenés CI, está en verde.
