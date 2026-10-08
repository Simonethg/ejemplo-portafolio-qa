# Matriz de riesgos · MiniModa

> Ejemplo con Lucía (ficticia). En tu repo: al menos 2 riesgos tienen que ser tuyos.

Riesgos de calidad por característica de ISO/IEC 25010. **Prioridad = Probabilidad × Impacto** (Alta / Media / Baja).
**Origen:** IA = lo propuso la IA y lo revisé · Propio = lo encontré yo probando la app. Fecha de revisión: 2026-10-07.

| ID | Característica | Riesgo | Prob. | Impacto | Prioridad | Origen | ¿Se mantiene? ¿Por qué? | Cómo lo pruebo | Resultado / evidencia |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | Adecuación funcional | El checkout confirma órdenes inválidas (sin productos, o sin mostrar qué se compra ni el total) | Alta | Alto | **Alta** | Propio | Sí: se puede entrar a `/checkout` por URL o desde el menú, y el checkout no muestra el total | Casos negativos sobre el checkout + exploratoria | Pendiente · evidencia inicial: [captura](../evidence/checkout-sin-total.png) |
| R-02 | Adecuación funcional | El carrito acepta más unidades que el stock | Alta | Alto | **Alta** | Propio | Sí: el producto 12 tiene stock 4 y el botón sigue activo | Valores límite sobre el stock | Pendiente · evidencia inicial: [captura](../evidence/carrito-supera-stock.png) |
| R-04 | Seguridad (integridad del pago) | Una tarjeta rechazada genera una orden igual | Media | Alto | **Alta** | IA | Sí: la tienda tiene tarjetas de prueba que rechazan | Casos negativos con tarjetas que rechazan | Pendiente |
| R-06 | Adecuación funcional | Se pueden agregar productos sin stock | Media | Alto | **Alta** | IA | Sí: hay 3 productos con stock 0 | Caso negativo con un producto sin stock | Pendiente |
| R-03 | Adecuación funcional | El filtro por edad muestra productos de otra edad | Baja | Alto | Media | IA | Sí: es la forma principal de buscar | Partición de equivalencia: 1 caso por opción del filtro | Pendiente |
| R-05 | Usabilidad | El formulario de checkout no avisa los datos inválidos | Media | Medio | Media | IA | Sí | Caso negativo con email inválido | Pendiente |
| R-07 | Usabilidad (accesibilidad) | Textos y botones con bajo contraste | Alta | Medio | Media | IA | Sí | Lighthouse en /tienda y /checkout | Pendiente |
| R-08 | Compatibilidad (interoperabilidad) | La API devuelve datos distintos a los que muestra la tienda | Baja | Alto | Media | IA | Sí: la tienda y la API exponen el mismo catálogo | Pruebas de API con Postman | Pendiente |
| R-09 | Eficiencia de desempeño | El catálogo tarda en cargar | Baja | Medio | Baja | IA | Sí, pero solo como medición liviana (no carga) | Tiempo de respuesta en Postman (< 2000 ms) | Pendiente |

## Descartados y por qué
- **"La app móvil se cierra al pagar"** (IA): MiniModa no tiene app móvil.
- **"Fallan los pagos con criptomonedas"** (IA): la tienda solo acepta tarjeta.
- **"El cambio de idioma rompe los precios"** (IA): no hay selector de idioma.

## Resumen
9 riesgos: 4 de prioridad alta, 4 media, 1 baja. Probados hasta ahora: 0 de 9 (el resto queda "Pendiente" y se cubre en los próximos avances).
