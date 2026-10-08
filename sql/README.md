# Validación de datos con SQL

> Ejemplo con Lucía (ficticia). Consultas ejecutadas el 2026-10-07.

MiniModa no da acceso a su base de datos. Por eso [productos.sql](productos.sql) arma la tabla `productos` con la respuesta real de `GET /api/products` (2026-10-07) y una tabla `carrito` con el carrito observado en BUG-002.

| Archivo | Qué tiene |
|---|---|
| [productos.sql](productos.sql) | Crea y carga las tablas (SQLite) |
| [validaciones-stock.sql](validaciones-stock.sql) | 6 consultas: sin stock por edad, total sin stock, stock por edad, stock bajo, integridad, carrito que supera el stock |

Cada consulta tiene un comentario con la pregunta de negocio, el resultado esperado, el obtenido y, si aplica, qué corregí de la IA.
**Resultado clave:** la consulta 6 devuelve el producto 12 (pide 12, stock 4): la regla "no vender más que el stock" no se cumple → [BUG-002](../bug-reports/BUG-002-carrito-supera-stock.md).

Cómo correrlas (gratis): pegá los dos archivos, en orden, en https://sqliteonline.com, o en la terminal, **desde la carpeta del repo** (`ls` tiene que mostrar `README.md`):
```bash
cd ~/qa-minimoda-ecommerce   # la carpeta de tu repo
sqlite3 :memory: ".read sql/productos.sql" ".read sql/validaciones-stock.sql"
```
