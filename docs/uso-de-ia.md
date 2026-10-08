# Uso de IA en este proyecto

> Ejemplo con Lucía (ficticia). Tu registro tiene que contar lo que pasó con TU IA.

**Herramientas:** asistentes de IA en plan gratuito (chat).
**Regla:** la IA propone, yo verifico en la app y decido. Nunca le paso datos personales, claves ni información de clientes o de mi trabajo.

## Qué hizo mal la IA y cómo lo corregí

| Fecha | Para qué | Qué le pedí | Qué hizo mal | Cómo lo corregí | Cómo lo verifiqué |
|---|---|---|---|---|---|
| 2026-10-07 | Riesgos | 10 riesgos de MiniModa por ISO/IEC 25010 | 3 riesgos no aplican: app móvil, pagos con cripto, cambio de idioma. No vio los riesgos del checkout ni del stock | Descarté 3 y sumé 2 propios (R-01 y R-02) | Recorriendo la tienda: no hay app, ni cripto, ni selector de idioma; capturé el carrito y el checkout |
| 2026-10-07 | Gestión ágil | Partir "Filtrar productos por edad" en tarjetas y redactar un backlog | 3 tarjetas repetidas y 2 vagas ("Probar todo el filtro") | Las uní y las reescribí con un resultado verificable | Revisé tarjeta por tarjeta contra la tienda |
| 2026-10-07 | Requisitos | Criterios de aceptación del filtro por edad | Inventó opciones del filtro ("Niños 3 a 8 años") y dejó "rápido" sin número | Usé las 5 opciones reales y medí "rápido" (< 1 s) | Abrí el filtro en /tienda |

<details>
<summary>Prompts principales</summary>

### Riesgos
```text
Sos QA. Esta es una tienda online de ropa infantil con catálogo, filtro por edad, color y precio,
carrito y checkout con tarjetas de prueba. Proponé 10 riesgos de calidad usando ISO/IEC 25010.
Para cada uno: característica, riesgo, probabilidad, impacto y cómo lo probarías.
```

</details>
