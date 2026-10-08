> **Repo de referencia: no lo clones.** Armá el tuyo y usá este para comparar cómo debería verse después de cada paso.
> Estás viendo **`v12-informe-final`**: Informe final y README como caso de estudio.
> Ejemplo con **Lucía Pereyra (QA ficticia)**: corridas, bugs y números reales (MiniModa, 2026-10-07). Reemplazá con tus propios hallazgos (mínimo 1 bug, 2 riesgos y 3 casos propios).

| Etapa | Qué se suma | Ver |
|---|---|---|
| `v00-repo-vacio` | Repo creado con README inicial y .gitignore | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v00-repo-vacio) |
| `v01-contexto` | README con el contexto del proyecto y perfil inicial | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v01-contexto) |
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
| 👉 **v12-informe-final** | Informe final y README como caso de estudio | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v12-informe-final) |
| `v13-perfil` | Perfil de GitHub con proyectos, métricas y habilidades con evidencia (versión final) | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v13-perfil) |

<details>
<summary><b>📘 Cómo armar y subir TU repo</b> (paso a paso, para copiar y pegar)</summary>

¿Primera vez con la terminal, Git o GitHub? Antes hacé [docs/00-primeros-pasos.md](docs/00-primeros-pasos.md) (terminal, Git, login en GitHub, IA gratis). Esa guía no va en tu repo.

**1. Creá tu repo vacío (una sola vez).** En GitHub: **+** → **New repository** → nombre `qa-minimoda-ecommerce` → **Public** → tildá **Add a README file** → **Create repository**. Es público porque es tu portafolio: nunca subas tu teléfono ni tu dirección.

**2. Sumá el `.gitignore` (una sola vez, en tu compu, cuando termines el paso 4).** Como en la guía T1: en VS Code **File → Open Folder** → `qa-minimoda-ecommerce` → **File → New File** → pegá el contenido de [.gitignore](.gitignore) → guardalo como `.gitignore` (con el punto adelante y sin `.txt`) → `git add .gitignore`, `git commit` y `git push`. No lo crees también desde la web: si lo hacés en los dos lados, Git da un conflicto. Así `node_modules/`, `.env` y `auth/` nunca se suben.

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
git add README.md docs/ reports/ test-cases/ test-runs/
git commit -m "Informe final con métricas y README como caso de estudio"
git push
```

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

[![Playwright Tests](https://github.com/Simonethg/ejemplo-portafolio-qa/actions/workflows/playwright.yml/badge.svg?branch=v12-informe-final)](https://github.com/Simonethg/ejemplo-portafolio-qa/actions/workflows/playwright.yml)

Proyecto de QA de punta a punta sobre el catálogo, los filtros, el carrito y el checkout de una tienda online: análisis de riesgos, casos de prueba, bugs reportados con evidencia, pruebas de API, SQL y un smoke automatizado con Playwright que corre en CI.

> **Contexto:** MiniModa (https://minimoda-navy.vercel.app) es una tienda demo de AcademiaQA para pruebas, con datos y tarjetas ficticios. No es un cliente real: es un proyecto personal para mostrar cómo trabajo.

## En 30 segundos

| | |
|---|---|
| **Producto** | Tienda online: 12 productos, filtros por edad, color y precio, carrito y checkout con tarjetas de prueba |
| **Mi rol** | Todo el ciclo de QA, en solitario: planifiqué, diseñé, ejecuté, reporté y automaticé |
| **Riesgo principal** | Que el checkout genere órdenes inválidas o que el carrito venda más de lo que hay en stock |
| **Qué encontré** | **2 bugs de severidad alta**: el checkout confirma compras con el carrito vacío y el carrito acepta 12 unidades de un producto con stock 4 |
| **Métricas** | 16 casos ejecutados (14 pasan, 2 fallan) · 2 bugs · 4 requests de API, 15 aserciones en verde · 5 tests de Playwright: 3 de 3 corridas locales y CI en verde ([run](https://github.com/Simonethg/ejemplo-portafolio-qa/actions/runs/37710326022)) · Lighthouse accesibilidad 94 (/tienda) |
| **Herramientas** | Playwright + TypeScript · GitHub Actions · Postman/Newman · SQL (SQLite) · Lighthouse · Chrome DevTools · IA (con registro de correcciones) |
| **Fecha de las corridas** | 2026-10-07 |

## Qué encontré

| ID | Bug | Severidad | Evidencia |
|---|---|---|---|
| [BUG-001](bug-reports/BUG-001-checkout-carrito-vacio.md) | Entrar directo a `/checkout` con el carrito vacío confirma la compra y da número de orden (solo cobra el envío, $ 3.500) | Alta | [captura](evidence/checkout-carrito-vacio.png) · test automatizado (`test.fail`) |
| [BUG-002](bug-reports/BUG-002-carrito-supera-stock.md) | El carrito acepta 12 unidades del "Conjunto Deportivo Comodín", que tiene stock 4 | Alta | [captura](evidence/carrito-supera-stock.png) · [consulta SQL 6](sql/validaciones-stock.sql) |

**Por qué pasa (DevTools):** al tocar "Confirmar compra" no sale ningún request al servidor. La orden se arma en el navegador, así que nadie valida del lado del servidor que haya productos ni stock. Detalle en [accesibilidad y compatibilidad](docs/accesibilidad-y-compatibilidad.md#devtools-console-y-network).

**Observación (todavía no es bug):** el checkout no muestra el detalle ni el total de los productos antes de confirmar; quedó como pregunta abierta en el [análisis de requisitos](docs/analisis-de-requisitos.md).

## Riesgos y cobertura

| Riesgo | Prioridad | Cómo lo cubrí | Resultado |
|---|---|---|---|
| R-01 · El checkout confirma órdenes inválidas (sin productos, o sin mostrar qué se compra ni el total) | Alta | CP-016 · exploratoria · test automatizado (`test.fail`) | ❌ [BUG-001](bug-reports/BUG-001-checkout-carrito-vacio.md) |
| R-02 · El carrito acepta más unidades que el stock | Alta | CP-010 · CP-011 · [SQL 6](sql/validaciones-stock.sql) | ❌ [BUG-002](bug-reports/BUG-002-carrito-supera-stock.md) |
| R-04 · Una tarjeta rechazada genera una orden igual | Alta | CP-013 · CP-014 · smoke automatizado | ✅ Pasa |
| R-06 · Se pueden agregar productos sin stock | Alta | CP-006 · [SQL 2](sql/validaciones-stock.sql) | ✅ Pasa (botón "Sin stock" deshabilitado) |
| R-03 · El filtro por edad muestra productos de otra edad | Media | CP-001 a CP-005 · API request 02 · smoke automatizado | ✅ Pasa |

Matriz completa (9 riesgos, 3 descartados con motivo): [docs/matriz-de-riesgos.md](docs/matriz-de-riesgos.md).

## Evidencia

| Qué | Qué demuestra | Link |
|---|---|---|
| Plan de pruebas | Objetivo, stakeholders, flujo de defectos, alcance y enfoque | [docs/plan-de-pruebas.md](docs/plan-de-pruebas.md) |
| Matriz de riesgos | Pruebas priorizadas por riesgo (ISO/IEC 25010) | [docs/matriz-de-riesgos.md](docs/matriz-de-riesgos.md) |
| Análisis de requisitos | Criterios ambiguos detectados antes de probar | [docs/analisis-de-requisitos.md](docs/analisis-de-requisitos.md) |
| Gestión ágil | Tablero Kanban con límite WIP y sprint de 1 semana | [docs/gestion/](docs/gestion/) |
| Casos de prueba | 16 casos: positivos, negativos y de valores límite, con trazabilidad a riesgos | [test-cases/](test-cases/) |
| Ejecución | Qué pasó, qué falló y qué quedó bloqueado, con fecha | [test-runs/registro-de-ejecucion.md](test-runs/registro-de-ejecucion.md) |
| Bugs | Pasos, esperado vs. obtenido, severidad, evidencia | [bug-reports/](bug-reports/) |
| Accesibilidad y compatibilidad | Lighthouse, DevTools, envío por país | [docs/accesibilidad-y-compatibilidad.md](docs/accesibilidad-y-compatibilidad.md) |
| Datos de prueba | Clientes ficticios y tarjetas de prueba | [test-data/](test-data/) |
| SQL | Consultas de stock sobre el catálogo real | [sql/](sql/) |
| API | Colección de Postman: status, tiempo, campos y un caso negativo | [api-tests/](api-tests/) |
| Automatización | Smoke de flujos críticos con Playwright, en CI | [tests/](tests/) · [workflow](.github/workflows/playwright.yml) |
| Informe final | Métricas, riesgos que quedan y recomendación | [reports/informe-final.md](reports/informe-final.md) |
| Uso de IA | Qué hizo mal la IA y cómo lo corregí | [docs/uso-de-ia.md](docs/uso-de-ia.md) |

## Cómo correr los tests

> **Primero, entrá a la carpeta del repo** (`cd`). Si corrés los comandos desde otra carpeta fallan con `ENOENT`. Chequeá con `pwd` y `ls` (tenés que ver `README.md`).

```bash
cd ~/qa-minimoda-ecommerce   # la carpeta de tu repo
npm install                  # la primera vez
npx playwright install chromium   # la primera vez
npx playwright test          # Playwright (Chromium)
npx playwright show-report   # reporte HTML
npm run test:api             # API: colección de Postman con Newman
```

Resultado esperado: `5 passed`. El test de BUG-001 está marcado con `test.fail()`: mientras el bug exista, "falla como se espera" y el CI queda en verde. Si lo corrigen, el CI se pone en rojo para avisar que hay que volver a probar y cerrar el bug.

En la API: 4 requests, 15 aserciones, 0 fallidas. Todo corre contra la URL pública de MiniModa, sin usuario, contraseña ni variables de entorno.

## Cómo trabajo con IA
- La IA me da un primer borrador; yo decido qué sirve, lo verifico en la app y sumo lo que no vio.
- Los 2 riesgos más importantes (checkout y stock) los encontré yo probando, no la IA.
- Nunca le paso datos personales, claves ni información de clientes o de mi trabajo. Registro: [docs/uso-de-ia.md](docs/uso-de-ia.md).

## Limitaciones y próximos pasos
- Fuera de alcance: pagos reales, carga y seguridad (app demo de terceros, sin permiso para eso).
- Solo Chromium (en Linux). Próximo: sumar Firefox y WebKit al CI y correr la colección de Postman con Newman en el mismo workflow.
- La base de datos de MiniModa no es accesible: el SQL corre sobre una copia del catálogo que devuelve la API.

## Estructura

```text
docs/            plan, riesgos, requisitos, gestión, accesibilidad y uso de IA
test-cases/      casos de prueba (CSV) y smoke suite
test-runs/       registro de ejecución y sesión exploratoria
bug-reports/     bugs en Markdown (también se cargan como Issues)
api-tests/       colección y entorno de Postman (sin claves)
sql/             datos del catálogo y consultas de validación
test-data/       datos ficticios
tests/           tests de Playwright (TypeScript)
evidence/        capturas sin datos personales
reports/         informe final
```

## Autora
Lucía Pereyra (ficticia) · Córdoba, Argentina · lucia.qa@example.com

## Datos y seguridad
Solo datos ficticios y tarjetas de prueba que publica la propia tienda. En este repo no hay contraseñas, tokens, `.env` ni archivos de sesión (ver [.gitignore](.gitignore)).
