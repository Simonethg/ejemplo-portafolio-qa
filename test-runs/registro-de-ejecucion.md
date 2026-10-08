# Registro de ejecución

> Ejemplo con Lucía (ficticia). Resultados reales del 2026-10-07: tus corridas van con tus fechas.

| Corrida | Fecha | Entorno | Qué se ejecutó | Ejecutados | Pasaron | Fallaron | Bloqueados | Bugs |
|---|---|---|---|---|---|---|---|---|
| RUN-01 | 2026-10-07 | Chromium · Linux · https://minimoda-navy.vercel.app | Casos funcionales CP-001 a CP-016 | 16 | 14 | 2 | 0 | BUG-001, BUG-002 |
| RUN-02 | 2026-10-07 | Lighthouse 12.8.2 | Accesibilidad de /tienda y /checkout | 2 páginas | — | — | — | Puntajes 94 y 96 · 4 mejoras |

Detalle de cada caso (resultado y bug): [../test-cases/casos-de-prueba.csv](../test-cases/casos-de-prueba.csv).

## Sesión exploratoria
- **Charter:** explorar el carrito y el checkout con carritos vacíos y cantidades en el límite del stock, para descubrir órdenes inválidas.
- **Fecha y duración:** 2026-10-07 · 30 min.
- **Notas:**
  - Entré a `/checkout` desde el menú, sin productos: el formulario no avisa que el carrito está vacío.
  - Completé con datos de prueba y la compra se confirmó con número de orden → BUG-001.
  - Busqué el producto con menos stock (id 12, stock 4) y agregué hasta 12 unidades sin ningún aviso → BUG-002.
  - El checkout no muestra qué estoy comprando ni el total → OBS-01 (pregunta abierta en el análisis de requisitos).
- **Hallazgos:** BUG-001, BUG-002, OBS-01.
