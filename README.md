> **Repo de referencia: no lo clones.** Armá el tuyo y usá este para comparar cómo debería verse después de cada paso.
> Estás viendo **`v01-contexto`**: README con el contexto del proyecto y perfil inicial.
> Ejemplo con **Lucía Pereyra (QA ficticia)**: corridas, bugs y números reales (MiniModa, 2026-10-07). Reemplazá con tus propios hallazgos (mínimo 1 bug, 2 riesgos y 3 casos propios).

| Etapa | Qué se suma | Ver |
|---|---|---|
| `v00-repo-vacio` | Repo creado con README inicial y .gitignore | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v00-repo-vacio) |
| 👉 **v01-contexto** | README con el contexto del proyecto y perfil inicial | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v01-contexto) |
| `v02-riesgos` | Matriz de riesgos (ISO/IEC 25010), evidencia y registro de uso de IA | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v02-riesgos) |
| `v03-plan-de-pruebas` | Plan de pruebas: objetivo, stakeholders, flujo de defectos y alcance | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v03-plan-de-pruebas) |
| `v04-gestion-agil` | Tablero Kanban con límite WIP y sprint de 1 semana | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v04-gestion-agil) |
| `v05-requisitos` | Análisis de requisitos del filtro por edad | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v05-requisitos) |
| `v06-casos-de-prueba` | 16 casos de prueba y primera ejecución | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v06-casos-de-prueba) |
| `v07-bugs` | BUG-001 y BUG-002 con evidencia + plantilla de Issue | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v07-bugs) |
| `v08-accesibilidad-y-datos` | Lighthouse, DevTools, envío por país y datos ficticios | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v08-accesibilidad-y-datos) |
| `v09-sql` | Consultas SQL de validación de stock | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v09-sql) |
| `v10-api` | Colección de Postman + `npm run test:api` | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v10-api) |
| `v11-playwright-ci` | Smoke con Playwright + TypeScript y CI con badge | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v11-playwright-ci) |
| `v12-informe-final` | Informe final y README como caso de estudio | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v12-informe-final) |
| `v13-perfil` | Perfil de GitHub con proyectos, métricas y habilidades con evidencia (versión final) | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v13-perfil) |

<details>
<summary><b>📘 Cómo armar y subir TU repo</b> (paso a paso, para copiar y pegar)</summary>

¿Primera vez con la terminal, Git o GitHub? Antes hacé [docs/00-primeros-pasos.md](docs/00-primeros-pasos.md) (terminal, Git, login en GitHub, IA gratis). Esa guía no va en tu repo.

**1. Creá tu repo vacío (una sola vez).** En GitHub: **+** → **New repository** → nombre `qa-minimoda-ecommerce` → **Public** → tildá **Add a README file** → **Create repository**. Es público porque es tu portafolio: nunca subas tu teléfono ni tu dirección.

**2. Sumá el `.gitignore` (una sola vez, en tu compu, cuando termines el paso 4).** Como en la guía T1: en VS Code **File → Open Folder** → `qa-minimoda-ecommerce` → **File → New File** → pegá el contenido de [.gitignore](.gitignore) → guardalo como `.gitignore` (con el punto adelante y sin `.txt`) → `git add .gitignore`, `git commit` y `git push`. No lo crees también desde la web: si lo hacés en los dos lados, Git da un conflicto. Así `node_modules/`, `.env` y `auth/` nunca se suben.

**Check de entrega (automático).** Después del `.gitignore`, sumá el check de la guía T1. En cada push, **Actions** → «Check de entrega» revisa que no queden `[corchetes]` de plantilla, teléfonos ni direcciones, archivos copiados de este ejemplo, secretos (`.env`, `node_modules`, claves) ni commits con tu email personal, y te dice en qué archivo y línea está el problema y cómo arreglarlo.

**3. Bajalo a tu compu (una sola vez).** Botón verde **Code** → **HTTPS** → copiá la URL. En la terminal (cambiá `TU-USUARIO`):

```bash
cd ~
git clone https://github.com/TU-USUARIO/qa-minimoda-ecommerce.git
```

**4. Entrá a la carpeta del repo.** Todos los comandos se corren adentro; si no, fallan con `ENOENT` / *no such file*. Con `pwd` ves dónde estás y con `ls` tenés que ver `README.md`:

```bash
cd ~/qa-minimoda-ecommerce
pwd
ls
```

**5. Subí el avance de este paso.** Creá o editá los archivos (mirá cómo quedan en esta versión) y subilos. Antes de `git add`, corré `git status` y revisá que **no** aparezcan `.env`, `auth/` ni `node_modules/`:

```bash
cd ~/qa-minimoda-ecommerce
git status
git add README.md
git commit -m "README: contexto del proyecto de QA sobre MiniModa"
git push
```

Tu perfil (CV público) va en **otro** repo que se llama igual que tu usuario (`TU-USUARIO/TU-USUARIO`). Modelo: [perfil-ejemplo/README.md](perfil-ejemplo/README.md).

**Errores comunes**

| Ves esto | Qué pasa | Qué hacer |
|---|---|---|
| `ENOENT` o `no such file or directory` | No estás en la carpeta del repo | `cd ~/qa-minimoda-ecommerce` y chequeá con `ls` que se vea `README.md` |
| `command not found: git` / `node` / `npm` | Falta instalar esa herramienta, o la terminal se abrió antes de instalarla | Instalala ([primeros pasos](docs/00-primeros-pasos.md)), cerrá y volvé a abrir la terminal |
| `npm warn deprecated …` o `found N vulnerabilities` | Avisos de dependencias, no errores | Se pueden ignorar. No corras `npm audit fix --force` |
| `rejected … (fetch first)` al hacer `git push` | En GitHub hay cambios que no tenés (por ejemplo, editaste desde la web) | `git pull --rebase` y después `git push` |

</details>

---

**⬇️ Desde acá, el README de Lucía en esta etapa** (en el tuyo va tu versión, con tus datos):

# QA de MiniModa · e-commerce de ropa infantil

Proyecto de QA sobre el catálogo, los filtros, el carrito y el checkout de una tienda online. **En progreso:** voy sumando cada artefacto a medida que avanzo.

> **Contexto:** MiniModa (https://minimoda-navy.vercel.app) es una tienda demo de AcademiaQA para pruebas, con datos y tarjetas ficticios. No es un cliente real: es un proyecto personal para mostrar cómo trabajo.

## Objetivo
Saber si el flujo de compra (filtro → carrito → checkout) funciona sin generar órdenes incorrectas y si la tienda está lista para vender.

## Autora
Lucía Pereyra (ficticia) · Córdoba, Argentina · lucia.qa@example.com

## Datos y seguridad
Solo datos ficticios y tarjetas de prueba que publica la propia tienda. En este repo no hay contraseñas, tokens, `.env` ni archivos de sesión (ver [.gitignore](.gitignore)).
