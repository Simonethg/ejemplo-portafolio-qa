# Informe final de pruebas · MiniModa

> Ejemplo con Lucía (ficticia). Todos los números salen de corridas reales del 2026-10-07. Los tuyos tienen que salir de tus registros.

| | |
|---|---|
| **Período** | 2026-10-07 |
| **Versión probada** | https://minimoda-navy.vercel.app al 2026-10-07 |
| **Autora** | Lucía Pereyra |

## Resumen
Probé el catálogo, los filtros, el carrito, el checkout y la API de productos de MiniModa. Los filtros, las validaciones del formulario y el rechazo de tarjetas funcionan. Encontré 2 bugs de severidad alta en el flujo de compra: se pueden confirmar compras con el carrito vacío y se puede comprar más que el stock. **Recomiendo no abrir ventas hasta corregir los dos.**

## Métricas
| Métrica | Valor |
|---|---|
| Riesgos identificados / cubiertos | 9 / 9 (más 3 propuestos por la IA y descartados) |
| Casos diseñados / ejecutados | 16 / 16 (7 negativos o de valores límite) |
| Pasaron / fallaron / bloqueados | 14 / 2 / 0 |
| Bugs por severidad | Crítica 0 · Alta 2 · Media 0 · Baja 0 |
| Observaciones abiertas | 1 funcional (checkout sin detalle ni total) · 4 mejoras de accesibilidad |
| Requests de API con tests | 4 (15 aserciones, 15 pasan) · tiempo promedio 422 ms |
| Consultas SQL | 6 (1 detecta la violación de stock de BUG-002) |
| Tests automatizados | 5 en Playwright (4 de smoke + 1 de bug conocido con `test.fail`) |
| Corridas automatizadas | Local: 3 de 3 en verde · CI: en verde en GitHub Actions, 5 passed ([run al cerrar el informe](https://github.com/Simonethg/ejemplo-portafolio-qa/actions/runs/37710326022)) |
| Accesibilidad (Lighthouse) | /tienda 94 · /checkout 96 |

## Hallazgos clave
1. **BUG-001 · Checkout con carrito vacío (Alta):** cualquiera que entre a /checkout desde el menú puede generar una orden sin productos. Para el negocio: órdenes basura, envíos cobrados sin compra y reclamos.
2. **BUG-002 · Carrito por encima del stock (Alta):** se pueden pedir 12 unidades de un producto con 4 en stock. Para el negocio: ventas que no se pueden entregar, devoluciones y mala reputación.
3. **Causa común probable:** la confirmación no pasa por el servidor (DevTools: ningún request al confirmar). Arreglar la validación en un solo lugar puede resolver los dos.

## Riesgos que quedan
- Si se sale así, la tienda va a recibir órdenes sin productos y sobreventas de los productos con poco stock (hoy, el Conjunto Deportivo Comodín, stock 4).
- El cliente no ve el total antes de pagar (OBS-01): riesgo de reclamos por cobros "sorpresa".
- Firefox y Safari no se probaron.

## Recomendación
**No salir** hasta corregir BUG-001 y BUG-002. Después: volver a correr CP-011 y CP-016, sacar el `test.fail()` del test de BUG-001 y confirmar el CI en verde.

## Limitaciones
- Solo Chromium en Linux.
- Sin pruebas de carga ni de seguridad (app de terceros, sin permiso).
- El SQL corre sobre una copia del catálogo de la API, no sobre la base de datos real.
- Registro, créditos y bandeja quedaron fuera de alcance.

## Próximos pasos
- Sumar Firefox y WebKit al CI.
- Automatizar BUG-002 cuando esté corregido (como test de regresión normal).
- Correr la colección de Postman con Newman en el mismo workflow de CI.
