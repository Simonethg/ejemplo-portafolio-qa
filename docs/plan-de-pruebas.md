# Plan de pruebas · MiniModa

> Ejemplo con Lucía (ficticia). Reemplazalo con tu propio plan.

| | |
|---|---|
| **Producto** | MiniModa · tienda online de ropa infantil (demo de AcademiaQA, datos ficticios) |
| **URL** | https://minimoda-navy.vercel.app |
| **Autora** | Lucía Pereyra |
| **Versión del plan** | 0.8 · 2026-10-07 |

## 1. Objetivo
Saber si el flujo de compra (filtro → carrito → checkout) funciona sin generar órdenes incorrectas y si la tienda está lista para vender.

## 2. Contexto, stakeholders y flujo de defectos
| Persona | Rol | Qué necesita de QA |
|---|---|---|
| Clara | Dueña / cliente | Saber si se puede salir a vender |
| Pablo | Product Manager | Qué bugs frenan la salida y cuáles pueden esperar |
| Maritza | Backend (carrito y pagos) | Bugs reproducibles con pasos, datos y evidencia |
| Lucía | QA | — |

**Flujo de un defecto:** 1. QA lo detecta y lo reporta (Issue + `bug-reports/`) → 2. el PM lo prioriza → 3. Dev lo corrige → 4. se despliega en el entorno de prueba → 5. QA lo vuelve a probar y lo cierra.

## 3. Alcance
- **Dentro:** catálogo, filtros (edad, color, precio), carrito (agregar, quitar, cantidades), checkout (validaciones, tarjetas de prueba aprobadas y rechazadas, costo de envío), API pública de productos.
- **Fuera:** pagos reales, pruebas de carga y de seguridad, registro, créditos y bandeja. Motivo: es una app demo de terceros y no hay permiso para carga ni seguridad; el resto queda para una próxima iteración.

## 4. Base de prueba
- Requisito: "Como mamá quiero filtrar productos por edad" → [analisis-de-requisitos.md](analisis-de-requisitos.md).
- Comportamiento observado en la tienda el 2026-10-07.
- Reglas de negocio confirmadas con el PM (ficticio): no se vende sin productos y no se vende más que el stock.

## 5. Riesgos
Ver [matriz-de-riesgos.md](matriz-de-riesgos.md): 9 riesgos, 4 de prioridad alta. Se prueba primero lo de prioridad alta.

## 6. Enfoque
| Tipo de prueba | Técnica | Dónde queda |
|---|---|---|
| Funcional | Partición de equivalencia (filtro por edad), valores límite (stock 4), casos negativos (tarjetas rechazadas, email inválido, carrito vacío) | [test-cases/](../test-cases/) |
| Exploratoria | Sesión de 30 min con charter sobre checkout y carrito | [test-runs/](../test-runs/) |
| Accesibilidad / compatibilidad | Lighthouse, DevTools, costo de envío por país | [accesibilidad-y-compatibilidad.md](accesibilidad-y-compatibilidad.md) |
| Datos | SQL sobre el catálogo (stock) | Pendiente |
| API | Postman/Newman: status, tiempo, campos, caso negativo 404 | Pendiente |
| Regresión (smoke) | Playwright + TypeScript en GitHub Actions | Pendiente |

## 7. Entorno y datos
- Navegador: Chromium · SO: Linux.
- Datos: solo ficticios ([test-data/](../test-data/)). Tarjetas de prueba de la tienda: aprueban `4111111111111111`; rechazan `4000000000000002` (rechazada) y `4000000000009995` (fondos insuficientes).

## 8. Criterios de entrada y salida
- **Entrada:** la URL responde 200 y el requisito del filtro está revisado.
- **Salida:** 100 % de los casos de prioridad alta ejecutados · todos los bugs de severidad alta reportados con evidencia.

## 9. Gestión de defectos
- Cada bug va como Issue con la plantilla de [.github/ISSUE_TEMPLATE/bug_report.md](../.github/ISSUE_TEMPLATE/bug_report.md) y con una copia en `bug-reports/`.
- **Severidad** (impacto técnico): Crítica / Alta / Media / Baja. **Prioridad** (urgencia de negocio): la decide el PM.

## 10. Gestión del trabajo
Tablero Kanban y sprint de 1 semana: [gestion/](gestion/).

## 11. Entregables
[Matriz de riesgos](matriz-de-riesgos.md) · [análisis de requisitos](analisis-de-requisitos.md) · [casos](../test-cases/) · [registro de ejecución](../test-runs/registro-de-ejecucion.md) · [bugs](../bug-reports/) · [accesibilidad](accesibilidad-y-compatibilidad.md) · (el resto se suma en los próximos avances)

## 12. Uso de IA
La IA hace borradores; la revisión y la decisión son mías. Registro de lo que corregí: [uso-de-ia.md](uso-de-ia.md).
