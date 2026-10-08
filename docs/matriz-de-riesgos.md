# Matriz de riesgos · MiniModa

> Ejemplo con Lucía (ficticia). En tu repo: al menos 2 riesgos tienen que ser tuyos.

Riesgos de calidad por característica de ISO/IEC 25010. **Prioridad = Probabilidad × Impacto** (Alta / Media / Baja).
**Origen:** IA = lo propuso la IA y lo revisé · Propio = lo encontré yo probando la app. Fecha de revisión: 2026-10-07.

| ID | Característica | Riesgo | Prob. | Impacto | Prioridad | Origen | ¿Se mantiene? ¿Por qué? | Cómo lo pruebo | Resultado / evidencia |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | Adecuación funcional | El checkout confirma órdenes inválidas (sin productos, o sin mostrar qué se compra ni el total) | Alta | Alto | **Alta** | Propio | Sí: se puede entrar a `/checkout` por URL o desde el menú, y el checkout no muestra el total | CP-016 · exploratoria · test automatizado (`test.fail`) | ❌ [BUG-001](../bug-reports/BUG-001-checkout-carrito-vacio.md) |
| R-02 | Adecuación funcional | El carrito acepta más unidades que el stock | Alta | Alto | **Alta** | Propio | Sí: el producto 12 tiene stock 4 y el botón sigue activo | CP-010 · CP-011 · [SQL 6](../sql/validaciones-stock.sql) | ❌ [BUG-002](../bug-reports/BUG-002-carrito-supera-stock.md) |
| R-04 | Seguridad (integridad del pago) | Una tarjeta rechazada genera una orden igual | Media | Alto | **Alta** | IA | Sí: la tienda tiene tarjetas de prueba que rechazan | CP-013 · CP-014 · smoke automatizado | ✅ Pasa |
| R-06 | Adecuación funcional | Se pueden agregar productos sin stock | Media | Alto | **Alta** | IA | Sí: hay 3 productos con stock 0 | CP-006 · [SQL 2](../sql/validaciones-stock.sql) | ✅ Pasa (botón "Sin stock" deshabilitado) |
| R-03 | Adecuación funcional | El filtro por edad muestra productos de otra edad | Baja | Alto | Media | IA | Sí: es la forma principal de buscar | CP-001 a CP-005 · API request 02 · smoke automatizado | ✅ Pasa |
| R-05 | Usabilidad | El formulario de checkout no avisa los datos inválidos | Media | Medio | Media | IA | Sí | CP-015 | ✅ Pasa ("El formato de email no es válido.") |
| R-07 | Usabilidad (accesibilidad) | Textos y botones con bajo contraste | Alta | Medio | Media | IA | Sí | Lighthouse en /tienda y /checkout | ⚠️ 34 elementos con bajo contraste en /tienda ([detalle](accesibilidad-y-compatibilidad.md)) |
| R-08 | Compatibilidad (interoperabilidad) | La API devuelve datos distintos a los que muestra la tienda | Baja | Alto | Media | IA | Sí: la tienda y la API exponen el mismo catálogo | [api-tests/](../api-tests/) (4 requests, 15 aserciones) | ✅ Pasa |
| R-09 | Eficiencia de desempeño | El catálogo tarda en cargar | Baja | Medio | Baja | IA | Sí, pero solo como medición liviana (no carga) | Tiempo de respuesta en Postman (< 2000 ms) | ✅ Promedio 422 ms (Newman, 2026-10-07) |

## Descartados y por qué
- **"La app móvil se cierra al pagar"** (IA): MiniModa no tiene app móvil.
- **"Fallan los pagos con criptomonedas"** (IA): la tienda solo acepta tarjeta.
- **"El cambio de idioma rompe los precios"** (IA): no hay selector de idioma.

## Resumen
9 riesgos: 4 de prioridad alta, 4 media, 1 baja. 9 de 9 cubiertos. 2 terminaron en bug (los 2 que encontré yo, no la IA).
