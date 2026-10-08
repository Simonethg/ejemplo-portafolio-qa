> **Repo de referencia: no lo clones.** Armá el tuyo y usá este para comparar cómo debería verse después de cada paso.
> Estás viendo **`v07-bugs`**: BUG-001 y BUG-002 con evidencia + plantilla de Issue.
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
| 👉 **v07-bugs** | BUG-001 y BUG-002 con evidencia + plantilla de Issue | [abrir](https://github.com/Simonethg/ejemplo-portafolio-qa/tree/v07-bugs) |
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

**2. Sumá el `.gitignore` (una sola vez, desde la web).** En tu repo: **Add file** → **Create new file** → nombre `.gitignore` → pegá el contenido de [.gitignore](.gitignore) → **Commit changes**. Así `node_modules/`, `.env` y `auth/` nunca se suben.

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
git add README.md .github/ bug-reports/ docs/ evidence/ test-cases/ test-runs/
git commit -m "Reporte de BUG-001 y BUG-002 con evidencia y plantilla de Issue"
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

Proyecto de QA sobre el catálogo, los filtros, el carrito y el checkout de una tienda online. **En progreso:** voy sumando cada artefacto a medida que avanzo.

> **Contexto:** MiniModa (https://minimoda-navy.vercel.app) es una tienda demo de AcademiaQA para pruebas, con datos y tarjetas ficticios. No es un cliente real: es un proyecto personal para mostrar cómo trabajo.

## Objetivo
Saber si el flujo de compra (filtro → carrito → checkout) funciona sin generar órdenes incorrectas y si la tienda está lista para vender.

## Qué encontré

| ID | Bug | Severidad | Evidencia |
|---|---|---|---|
| [BUG-001](bug-reports/BUG-001-checkout-carrito-vacio.md) | Entrar directo a `/checkout` con el carrito vacío confirma la compra y da número de orden (solo cobra el envío, $ 3.500) | Alta | [captura](evidence/checkout-carrito-vacio.png) |
| [BUG-002](bug-reports/BUG-002-carrito-supera-stock.md) | El carrito acepta 12 unidades del "Conjunto Deportivo Comodín", que tiene stock 4 | Alta | [captura](evidence/carrito-supera-stock.png) |

**Observación (todavía no es bug):** el checkout no muestra el detalle ni el total de los productos antes de confirmar; quedó como pregunta abierta en el [análisis de requisitos](docs/analisis-de-requisitos.md).

## Riesgos y cobertura

| Riesgo | Prioridad | Cómo lo cubrí | Resultado |
|---|---|---|---|
| R-01 · El checkout confirma órdenes inválidas (sin productos, o sin mostrar qué se compra ni el total) | Alta | CP-016 · exploratoria | ❌ [BUG-001](bug-reports/BUG-001-checkout-carrito-vacio.md) |
| R-02 · El carrito acepta más unidades que el stock | Alta | CP-010 · CP-011 | ❌ [BUG-002](bug-reports/BUG-002-carrito-supera-stock.md) |
| R-04 · Una tarjeta rechazada genera una orden igual | Alta | CP-013 · CP-014 | ✅ Pasa |
| R-06 · Se pueden agregar productos sin stock | Alta | CP-006 | ✅ Pasa (botón "Sin stock" deshabilitado) |
| R-03 · El filtro por edad muestra productos de otra edad | Media | CP-001 a CP-005 | ✅ Pasa |

Matriz completa (9 riesgos, 3 descartados con motivo): [docs/matriz-de-riesgos.md](docs/matriz-de-riesgos.md).

## Lo que hay hasta ahora

| Qué | Qué demuestra | Link |
|---|---|---|
| Plan de pruebas | Objetivo, stakeholders, flujo de defectos, alcance y enfoque | [docs/plan-de-pruebas.md](docs/plan-de-pruebas.md) |
| Matriz de riesgos | Pruebas priorizadas por riesgo (ISO/IEC 25010) | [docs/matriz-de-riesgos.md](docs/matriz-de-riesgos.md) |
| Análisis de requisitos | Criterios ambiguos detectados antes de probar | [docs/analisis-de-requisitos.md](docs/analisis-de-requisitos.md) |
| Gestión ágil | Tablero Kanban con límite WIP y sprint de 1 semana | [docs/gestion/](docs/gestion/) |
| Casos de prueba | 16 casos: positivos, negativos y de valores límite, con trazabilidad a riesgos | [test-cases/](test-cases/) |
| Ejecución | Qué pasó, qué falló y qué quedó bloqueado, con fecha | [test-runs/registro-de-ejecucion.md](test-runs/registro-de-ejecucion.md) |
| Bugs | Pasos, esperado vs. obtenido, severidad, evidencia | [bug-reports/](bug-reports/) |
| Uso de IA | Qué hizo mal la IA y cómo lo corregí | [docs/uso-de-ia.md](docs/uso-de-ia.md) |

## Cómo trabajo con IA
- La IA me da un primer borrador; yo decido qué sirve, lo verifico en la app y sumo lo que no vio.
- Los 2 riesgos más importantes (checkout y stock) los encontré yo probando, no la IA.
- Nunca le paso datos personales, claves ni información de clientes o de mi trabajo. Registro: [docs/uso-de-ia.md](docs/uso-de-ia.md).

## Autora
Lucía Pereyra (ficticia) · Córdoba, Argentina · lucia.qa@example.com

## Datos y seguridad
Solo datos ficticios y tarjetas de prueba que publica la propia tienda. En este repo no hay contraseñas, tokens, `.env` ni archivos de sesión (ver [.gitignore](.gitignore)).
