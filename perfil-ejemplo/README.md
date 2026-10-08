<!--
EJEMPLO DE README DE PERFIL (CV público en GitHub)
Va en un repo PÚBLICO que se llama EXACTAMENTE como tu usuario: github.com/tu-usuario/tu-usuario
Lucía Pereyra es ficticia. Los links de abajo apuntan a archivos de ESTE repo de ejemplo;
en tu perfil van a ser links completos a tu propio repo (https://github.com/tu-usuario/tu-repo/...).
Reglas: nunca teléfono ni dirección · proyectos en "Proyectos", no en "Experiencia" · la formación solo en "Educación"
· cada habilidad con su evidencia · nada de widgets ni muros de insignias. Borrá este comentario en tu versión.
-->

# Hola, soy Lucía Pereyra

**QA Analyst Jr · Testing funcional, APIs y automatización con Playwright**

📍 Córdoba, Argentina · ✉️ lucia.qa@example.com · LinkedIn: [NO ESTÁ EN LA FICHA]

## Sobre mí

Hace 5 años trabajo en atención al cliente de un e-commerce: reporto incidencias, valido flujos de compra y sigo cada ticket hasta que se cierra. Hoy hago eso como QA: priorizo pruebas por riesgo, diseño casos con valores límite, reporto bugs que se reproducen y automatizo smoke tests con Playwright en CI. Busco mi primer puesto como QA Analyst Jr.

## Proyectos destacados

| Proyecto | Qué hice | Evidencia |
|---|---|---|
| **[QA de e-commerce · MiniModa](../README.md)** [![CI](https://github.com/Simonethg/plantilla-proyecto-qa/actions/workflows/playwright.yml/badge.svg)](https://github.com/Simonethg/plantilla-proyecto-qa/actions/workflows/playwright.yml) | Plan por riesgos · 16 casos (7 negativos y de límite) · 2 bugs de severidad alta · 4 requests de API con 15 aserciones · smoke de 5 tests en Playwright, verde en CI | [Informe final](../reports/informe-final.md) · [Bugs](../bug-reports/) |
| **Beta testing · [segundo proyecto]** | [NO ESTÁ EN LA FICHA] | [NO ESTÁ EN LA FICHA] |

## Experiencia

**Atención al cliente · E-commerce de indumentaria · 2021 – hoy**
- Reporte de incidencias: detecto y documento los problemas que reportan los clientes y los escalo al equipo técnico.
- Validación de flujos: pruebo el flujo de compra antes de responder un reclamo.
- Seguimiento del ciclo de vida de un defecto: sigo cada ticket hasta su cierre.

## Habilidades (con evidencia)

| Habilidad | Dónde se ve |
|---|---|
| Análisis de riesgos (ISO/IEC 25010) | [Matriz de riesgos](../docs/matriz-de-riesgos.md) |
| Revisión de requisitos y criterios de aceptación | [Análisis de requisitos](../docs/analisis-de-requisitos.md) |
| Diseño de casos (partición de equivalencia, valores límite) | [Casos de prueba](../test-cases/) |
| Reporte de bugs reproducibles | [Bugs](../bug-reports/) |
| Pruebas de API (Postman, Newman) | [api-tests/](../api-tests/) |
| SQL para validar datos | [sql/](../sql/) |
| Automatización (Playwright + TypeScript + GitHub Actions) | [tests/](../tests/) · [workflow](../.github/workflows/playwright.yml) |
| Accesibilidad (Lighthouse) y DevTools | [Accesibilidad y compatibilidad](../docs/accesibilidad-y-compatibilidad.md) |

## Cómo trabajo con IA

- La IA me da un primer borrador: riesgos, casos, tests y textos.
- Yo decido qué sirve, lo verifico en la app y sumo lo que no vio. Ejemplo: la IA inventó el test id `order-success`; el real es `checkout-success`. Los 2 bugs que encontré no estaban entre los riesgos que propuso la IA.
- Nunca le paso datos personales, claves ni información de clientes o de mi trabajo. Registro completo: [uso de IA](../docs/uso-de-ia.md).

## Educación

- **Bootcamp QA con IA · AcademiaQA · 2026**
- Inglés: básico (estudiando)

## Contacto

lucia.qa@example.com · LinkedIn: [NO ESTÁ EN LA FICHA] · Córdoba, Argentina
