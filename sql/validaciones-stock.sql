-- Validaciones de stock · MiniModa
-- Antes de correr esto, cargá sql/productos.sql (crea las tablas productos y carrito).
-- Cada consulta tiene: la pregunta de negocio, el resultado esperado y el resultado obtenido el 2026-10-07.

-- 1) ¿Qué productos de Niño (3-8) no tienen stock?
--    Esperado: los que la tienda muestra con "Sin stock" en ese filtro.
--    Obtenido: 1 fila → 6 · Buzo con Capucha Cohete. Coincide con la tienda (botón deshabilitado).
--    IA: la primera versión filtraba con edad = 'Niño' y devolvía 0 filas (el valor real es 'Niño (3-8)').
SELECT id, nombre, stock
FROM productos
WHERE edad = 'Niño (3-8)'
  AND stock = 0;

-- 2) ¿Cuántos productos hay sin stock en todo el catálogo?
--    Esperado: 3 (ids 2, 6 y 11, los que muestran "Sin stock" en /tienda). Obtenido: 3.
SELECT COUNT(*) AS productos_sin_stock
FROM productos
WHERE stock = 0;

-- 3) ¿Cuánto stock hay por edad?
--    Sirve para elegir datos de prueba: Pre-teen (9-12) tiene el producto con menos stock disponible (id 12, stock 4).
--    Obtenido: Bebé (0-2) 37 · Niña (3-8) 21 · Niño (3-8) 27 · Pre-teen (9-12) 21.
SELECT edad,
       COUNT(*)   AS productos,
       SUM(stock) AS unidades
FROM productos
GROUP BY edad
ORDER BY edad;

-- 4) ¿Qué productos tienen stock bajo (entre 1 y 5)? Son los candidatos para probar valores límite.
--    Obtenido: 1 fila → 12 · Conjunto Deportivo Comodín · stock 4 (usado en CP-010 y CP-011).
SELECT id, nombre, stock
FROM productos
WHERE stock BETWEEN 1 AND 5
ORDER BY stock;

-- 5) Integridad: ¿hay precios en cero o negativos, o stock negativo?
--    Esperado: 0 filas. Obtenido: 0 filas.
SELECT id, nombre, precio, stock
FROM productos
WHERE precio <= 0
   OR stock < 0;

-- 6) ¿Hay líneas del carrito que piden más unidades que el stock? (regla de negocio de BUG-002)
--    Esperado si la regla se cumpliera: 0 filas.
--    Obtenido: 1 fila → producto 12 · pide 12 · stock 4 · excede por 8.
SELECT c.producto_id,
       p.nombre,
       c.cantidad,
       p.stock,
       c.cantidad - p.stock AS excede_por
FROM carrito AS c
JOIN productos AS p ON p.id = c.producto_id
WHERE c.cantidad > p.stock;
