# Pruebas de API · MiniModa

> Ejemplo con Lucía (ficticia). Resultados reales del 2026-10-07.

| Archivo | Qué tiene |
|---|---|
| [minimoda.postman_collection.json](minimoda.postman_collection.json) | 4 requests con tests (`pm.test`) de status, tiempo de respuesta, campos y un caso negativo |
| [minimoda.postman_environment.json](minimoda.postman_environment.json) | Variable `baseUrl`. **Sin claves ni tokens** (la API es pública y de solo lectura) |

| Request | Qué valida | Resultado (Newman, 2026-10-07) |
|---|---|---|
| `GET {{baseUrl}}/api/products` | 200 · < 2000 ms · `ok` true · 12 productos · cada uno con edad, precio > 0 y stock ≥ 0 | ✅ 5/5 |
| `GET {{baseUrl}}/api/products?edad=Niño (3-8)` | 200 · < 2000 ms · 3 productos, todos Niño (3-8) | ✅ 4/4 |
| `GET {{baseUrl}}/api/products/4` | 200 · < 2000 ms · es la Remera Dino Aventurero · stock entero | ✅ 4/4 |
| `GET {{baseUrl}}/api/products/999` (negativo) | 404 · `ok` false · mensaje de error con el id | ✅ 2/2 |

**Total:** 4 requests · 15 aserciones · 15 pasan · tiempo promedio 422 ms.

**Test roto a propósito:** cambié "12 productos" por 13 y Newman marcó `AssertionError El catálogo tiene 12 productos` (1 de 15 falló). Así sé que el test valida de verdad. Después lo volví a 12.

Para correrla sin abrir Postman (gratis, Newman ya está en las dependencias del repo):

> **Ojo: los comandos se corren dentro de la carpeta del repo.** Si los corrés desde otra carpeta fallan con `ENOENT` / *no such file*. Chequeá con `pwd` (dónde estás) y `ls` (tenés que ver `README.md`).

```bash
cd ~/qa-minimoda-ecommerce   # la carpeta de tu repo
npm install                  # solo la primera vez
npm run test:api
```

`npm run test:api` ejecuta: `newman run api-tests/minimoda.postman_collection.json -e api-tests/minimoda.postman_environment.json`.
