# Accesibilidad y compatibilidad · MiniModa

> Ejemplo con Lucía (ficticia). Los resultados son reales del 2026-10-07: volvé a medir y poné los tuyos.

## Lighthouse (accesibilidad)
Lighthouse 12.8.2 · Chrome headless · 2026-10-07.

| Página | Puntaje | Captura |
|---|---|---|
| /tienda | **94** | [lighthouse-accesibilidad-tienda.png](../evidence/lighthouse-accesibilidad-tienda.png) |
| /checkout | **96** | — |

| # | Hallazgo | Dónde | Impacto para el usuario | Prioridad | ¿Lo reporté? |
|---|---|---|---|---|---|
| 1 | Contraste insuficiente: botón "Agregar al carrito" y chip de color activo (blanco sobre `#1aa3ff`, 2,71:1; mínimo 4,5:1) | /tienda (34 elementos en total) | Personas con baja visión o con el celular al sol no leen el botón principal de compra | Media | Mejora, no bloquea la salida |
| 2 | Contraste insuficiente: botón "Confirmar compra" (blanco sobre `#189e93`, 3,3:1) | /checkout | Mismo caso, en el paso donde se paga | Media | Mejora |
| 3 | Etiquetas "Stock: N" y "Sin stock" con contraste 3,3:1 y 3,43:1 | /tienda | El dato de stock se lee mal | Baja | Mejora |
| 4 | Encabezados fuera de orden (salta a `<h3>`) | /tienda | Lectores de pantalla navegan peor la página | Baja | Mejora |

**Lo que pasa bien:** imágenes con texto alternativo, campos con etiqueta, botones y links con nombre, `lang` en el HTML.

## DevTools (Console y Network)
- **Network al confirmar la compra:** con el carrito con 1 producto y la tarjeta `4111111111111111`, el clic en "Confirmar compra" **no hace ningún request** al servidor. La orden y el email de confirmación se generan en el navegador (el email queda en `localStorage`, clave `minimoda_inbox`).
- **Qué implica:** nadie valida del lado del servidor que el carrito tenga productos o que haya stock. Es la causa probable de [BUG-001](../bug-reports/BUG-001-checkout-carrito-vacio.md) y [BUG-002](../bug-reports/BUG-002-carrito-supera-stock.md).
- **Console:** sin errores al confirmar la compra.

## Envío a otros países
No se usó VPN: el país se elige en el checkout. Costo de envío observado (2026-10-07):

| País | Costo de envío |
|---|---|
| Argentina | $ 3.500 |
| Brasil · Uruguay | $ 9.000 |
| México | $ 15.000 |
| España · Estados Unidos · Japón | $ 28.000 |

Moneda: siempre pesos ($). Idioma: siempre español. Sin bloqueos.
**Pregunta abierta:** ¿el precio para el exterior se muestra en pesos a propósito?

## Navegadores
| Navegador | Versión | Resultado |
|---|---|---|
| Chrome (headless) | 154 · Linux | Lighthouse y recorrido manual sin errores |
| Firefox · WebKit (Safari) | — | No probado (próximo paso) |
