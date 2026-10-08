# Casos de prueba

> Ejemplo con Lucía (ficticia). En tu repo: al menos 3 casos tienen que ser tuyos.

| Archivo | Qué tiene |
|---|---|
| [casos-de-prueba.csv](casos-de-prueba.csv) | 16 casos (formato importable en Qase o en una planilla) con riesgo, técnica, datos, resultado y bug |

**Técnicas usadas:** partición de equivalencia (1 caso por opción del filtro por edad), valores límite (stock 4: agrego 4 y 5; precio máximo), casos negativos (sin stock, tarjetas rechazadas, email inválido, carrito vacío).
**Trazabilidad:** cada caso indica qué riesgo (R-xx) cubre y, si falló, qué bug abrió.

## Resumen (ejecución del 2026-10-07)

| | Cantidad |
|---|---|
| Casos | 16 (7 negativos o de valores límite) |
| Pasan | 14 |
| Fallan | 2 → CP-011 ([BUG-002](../bug-reports/BUG-002-carrito-supera-stock.md)) y CP-016 ([BUG-001](../bug-reports/BUG-001-checkout-carrito-vacio.md)) |
| Bloqueados | 0 |
