# Smoke suite · flujos críticos

> Ejemplo con Lucía (ficticia).

| # | Flujo | Por qué es crítico | Test |
|---|---|---|---|
| 1 | Filtrar por edad (CP-002) | Es la forma principal de encontrar productos | `tests/smoke.spec.ts` |
| 2 | Agregar al carrito (CP-008) | Sin esto no hay venta; además valida el total | `tests/smoke.spec.ts` |
| 3 | Comprar con tarjeta de prueba aprobada (CP-012) | Es donde se pierde plata si falla | `tests/smoke.spec.ts` |
| 4 | Tarjeta rechazada (CP-013) | Una orden con pago rechazado es plata perdida | `tests/smoke.spec.ts` |
| 5 | Checkout con carrito vacío (CP-016) | Bug abierto BUG-001: el test avisa cuando lo corrijan | `tests/bugs-conocidos.spec.ts` (`test.fail`) |

**Descartados:**
- Cambiar de idioma (lo propuso la IA): MiniModa no tiene selector de idioma.
- BUG-002 (carrito por encima del stock): se probó a mano. No se automatizó todavía para no sumar otro test que falla a propósito; queda como próximo paso.

## Corridas
| Fecha | Dónde | Resultado | Flaky |
|---|---|---|---|
| 2026-10-07 21:24 ART | Local (Chromium, Linux) | 5 passed (4,3 s) | Ninguno |
| 2026-10-07 21:24 ART | Local (Chromium, Linux) | 5 passed (5,0 s) | Ninguno |
| 2026-10-07 21:24 ART | Local (Chromium, Linux) | 5 passed (4,1 s) | Ninguno |
| 2026-10-07 | GitHub Actions ([Actions](https://github.com/Simonethg/ejemplo-portafolio-qa/actions/workflows/playwright.yml)) | 5 passed | Ninguno |

"5 passed" incluye el test de BUG-001, que falla como se espera (`test.fail`). En el reporte HTML aparece como pasado.
