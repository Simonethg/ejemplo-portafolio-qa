# Análisis de requisitos · Filtrar productos por edad

> Ejemplo con Lucía (ficticia). Reemplazalo con tu propia revisión.

**Requisito original:** "Como mamá quiero filtrar productos por edad".
**Criterio de aceptación original:** "El filtro tiene que ser rápido y mostrar la ropa adecuada para cada edad".
**Opciones reales del filtro (verificadas en /tienda el 2026-10-07):** Todas las edades · Bebé (0-2) · Niño (3-8) · Niña (3-8) · Pre-teen (9-12).

## Hallazgos de la revisión
| Criterio | Problema | Tipo |
|---|---|---|
| "Tiene que ser rápido" | No dice cuánto. No se puede aprobar ni rechazar | No testeable |
| "La ropa adecuada para cada edad" | No dice qué pasa con la ropa unisex: la tienda separa Niño (3-8) y Niña (3-8) | Ambiguo |
| Rangos "3-8" y "9-12" | ¿Un chico de 8 años entra en 3-8? ¿Y uno de 8 años y medio? | Límite dudoso |
| Productos sin stock | No dice si se muestran en el filtro. Hoy se muestran con "Sin stock" | Ambiguo |
| Filtros combinados | No dice si edad + color + precio se suman (Y) o se reemplazan | Falta |

## Historia corregida
Como mamá, quiero filtrar por edad, para ver solo ropa para la edad de mi hijo o hija.

**Criterio 1 · filtra por la opción elegida**
Dado que estoy en /tienda
Cuando elijo "Niño (3-8)" en Edad
Entonces veo solo productos "Niño (3-8)"
Y no veo productos "Bebé (0-2)"

**Criterio 2 · volver a ver todo**
Dado que filtré por una edad
Cuando elijo "Todas las edades"
Entonces vuelvo a ver los 12 productos

**Criterio 3 · productos sin stock**
Dado que un producto de la edad elegida no tiene stock
Entonces aparece con la etiqueta "Sin stock" y su botón está deshabilitado

**Criterio 4 · rapidez (medible)**
Dado que elijo una edad
Entonces la lista se actualiza en menos de 1 segundo, sin recargar la página

## Preguntas abiertas para el analista
- ¿"3-8" incluye a los de 8 años? (si sí, la etiqueta está bien; si no, cambiarla a "3-7").
- ¿Los filtros se combinan entre sí (edad Y color Y precio)?
- **Fuera de este requisito, pero visto al probar (OBS-01):** el checkout no muestra el detalle ni el total de los productos antes de confirmar; solo el costo de envío. El mensaje de confirmación y el email de la Bandeja tampoco muestran el total. ¿Es intencional? Si no, es un bug de severidad media.

<details>
<summary>Borrador generado con IA (como referencia)</summary>

La IA propuso 6 criterios. Me quedé con 2 y reescribí el resto:
- Usaba opciones que no existen ("Niños 3 a 8 años", "Adolescentes") → las cambié por las opciones reales del filtro.
- No preguntaba qué pasa con los productos sin stock ni con los límites de los rangos → los sumé yo.
- Mantenía "rápido" sin número → lo hice medible (menos de 1 segundo).

</details>
