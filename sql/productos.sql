-- Datos: copia del catálogo que devuelve GET /api/products el 2026-10-07 (12 productos).
-- MiniModa no expone su base de datos: esta tabla se arma con la respuesta de la API para practicar validaciones.
-- Motor: SQLite (sirve en https://sqliteonline.com o con el comando sqlite3).

DROP TABLE IF EXISTS carrito;
DROP TABLE IF EXISTS productos;

CREATE TABLE productos (
  id        INTEGER PRIMARY KEY,
  nombre    TEXT    NOT NULL,
  edad      TEXT    NOT NULL,
  color     TEXT    NOT NULL,
  precio    INTEGER NOT NULL,
  talla     TEXT    NOT NULL,
  stock     INTEGER NOT NULL,
  destacado INTEGER NOT NULL  -- 1 = sí, 0 = no
);

INSERT INTO productos (id, nombre, edad, color, precio, talla, stock, destacado) VALUES
  (1, 'Body Manga Larga Estrellitas', 'Bebé (0-2)', 'Azul', 8500, '6M', 12, 1),
  (2, 'Enterito de Algodón Nubes', 'Bebé (0-2)', 'Rosa', 12000, '12M', 0, 0),
  (3, 'Gorrito de Lana Osito', 'Bebé (0-2)', 'Amarillo', 5600, 'Único', 25, 0),
  (4, 'Remera Dino Aventurero', 'Niño (3-8)', 'Verde', 9800, '4', 18, 1),
  (5, 'Pantalón Cargo Explorador', 'Niño (3-8)', 'Gris', 15400, '6', 9, 0),
  (6, 'Buzo con Capucha Cohete', 'Niño (3-8)', 'Azul', 18900, '8', 0, 0),
  (7, 'Vestido Floral Primavera', 'Niña (3-8)', 'Rosa', 16700, '5', 14, 1),
  (8, 'Pollera Plisada Arcoíris', 'Niña (3-8)', 'Amarillo', 11200, '6', 7, 0),
  (9, 'Campera Rompeviento Deportiva', 'Pre-teen (9-12)', 'Rojo', 24500, '10', 6, 1),
  (10, 'Jean Slim Urbano', 'Pre-teen (9-12)', 'Azul', 21000, '12', 11, 0),
  (11, 'Remera Estampada Skater', 'Pre-teen (9-12)', 'Verde', 10300, '10', 0, 0),
  (12, 'Conjunto Deportivo Comodín', 'Pre-teen (9-12)', 'Gris', 27800, '12', 4, 1);

-- Carrito observado en la sesión exploratoria del 2026-10-07 (ver BUG-002):
-- el carrito aceptó 12 unidades del producto 12, que tiene stock 4.
CREATE TABLE carrito (
  producto_id INTEGER NOT NULL REFERENCES productos(id),
  cantidad    INTEGER NOT NULL
);

INSERT INTO carrito (producto_id, cantidad) VALUES
  (4, 1),
  (12, 12);
