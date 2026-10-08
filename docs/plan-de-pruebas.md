# Plan de pruebas · MiniModa

> Ejemplo con Lucía (ficticia). Reemplazalo con tu propio plan.

| | |
|---|---|
| **Producto** | MiniModa · tienda online de ropa infantil (demo de AcademiaQA, datos ficticios) |
| **URL** | https://minimoda-navy.vercel.app |
| **Autora** | Lucía Pereyra |
| **Versión del plan** | 0.4 · 2026-10-07 |

> Documento vivo: empieza con objetivo, contexto y alcance. Enfoque, entorno, criterios y entregables se suman cuando diseño los casos.

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

## 4. Riesgos
Ver [matriz-de-riesgos.md](matriz-de-riesgos.md): 9 riesgos, 4 de prioridad alta. Se prueba primero lo de prioridad alta.

## 5. Gestión del trabajo
Tablero Kanban y sprint de 1 semana: [gestion/](gestion/).

## 6. Uso de IA
La IA hace borradores; la revisión y la decisión son mías. Registro de lo que corregí: [uso-de-ia.md](uso-de-ia.md).
