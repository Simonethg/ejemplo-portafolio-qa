# Gestión del trabajo · tablero y sprint

> Ejemplo con Lucía (ficticia). En tu repo van tus capturas: `tablero-kanban.png` (Trello o Jira) y `sprint-jira.png`.
> Captura del tablero de Lucía: [NO ESTÁ EN LA FICHA] (Lucía es ficticia; acá se muestra el contenido en texto).

## Tablero Kanban · "Filtrar productos por edad"

Límite WIP: **En curso 2** · **En revisión 1**.

| Por hacer | En curso (WIP 2) | En revisión (WIP 1) | Hecho |
|---|---|---|---|
| Probar filtros combinados (edad + color + precio) | Diseñar casos de partición de equivalencia del filtro | Revisar criterios de aceptación con el analista | Recorrer la tienda y listar las opciones reales del filtro |
| Probar productos sin stock dentro del filtro | Preparar datos de prueba ficticios | | Matriz de riesgos inicial |
| Medir el tiempo de respuesta del filtro | | | |

**Qué corregí del borrador de la IA:** propuso 12 tarjetas; uní 3 repetidas ("Probar filtro Niño", "Validar filtro Niño", "Test filtro Niño") y reescribí 2 vagas ("Probar todo el filtro" → "Diseñar casos de partición de equivalencia del filtro").

## Sprint 1 · 1 semana

**Objetivo del sprint:** dejar probado el flujo filtro → carrito → checkout y reportar lo que lo rompa.

| Ticket | Tipo | Estimación | Estado al cierre |
|---|---|---|---|
| Revisar el requisito del filtro por edad | Historia | 2 | Hecho |
| Diseñar y ejecutar casos del filtro, el carrito y el checkout | Historia | 5 | Hecho |
| Reportar los bugs encontrados con evidencia | Bug | 2 | Hecho |
| Probar la API de productos | Historia | 3 | Pasa al sprint 2 |
| Automatizar el smoke del flujo de compra | Historia | 5 | Pasa al sprint 2 |

**Ceremonias y rol de QA:** en la planning estimo el esfuerzo de prueba; en la daily aviso bloqueos; en la review muestro bugs y evidencia; en la retro propongo mejoras del flujo de defectos.
