# Repositorio de Prompts para el Proyecto "Los Californios"

importante: todo lo que tenga (validar), se tiene que discutir con el equipo

## Introducción
Este documento README_prompts tiene como finalidad documentar y organizar los **prompts** diseñados para el proyecto *“Los Californios”*, el cual utiliza **Modelos de Lenguaje de Gran Escala (LLMs)** para optimizar y enriquecer guiones audiovisuales. Los prompts son las instrucciones que permiten interactuar con estos modelos, guiándolos para generar resultados alineados con las necesidades narrativas, históricas y técnicas del proyecto.

El objetivo principal de este repositorio es disponer de **diferentes versiones y categorías de prompts** que sean reutilizables y ajustables para los diversos aspectos del proyecto. Esto permitirá mantener un enfoque estructurado y mejorar continuamente los resultados generados por los modelos.

---

## Contenido del documento README_prompts

### 1. Objetivo de los Prompts
Los prompts almacenados en este repositorio se centran en:
- **Mejorar los guiones** mediante el ajuste de narrativa, diálogos y ambientaciones.
- **Brindar contexto histórico y cultural** a los modelos para garantizar precisión y coherencia con el periodo.
- **Eficientizar el desarrollo y revisión** de guiones alineados con estándares cinematográficos.
- **Construir instrucciones reutilizables** para otros procesos relacionados, como la generación de imágenes o videos (segunda etapa del proyecto).
- **Limpieza de datos** mediante el uso de prompts, se limpiaran los datos (texto) del libro y se clasificaran por capitulos. 

---

### 2. Organización por Categorías
Los prompts están organizados en **categorías** según su propósito y etapa del proceso creativo. A continuación, se presentan las principales categorías disponibles en el repositorio:


1. **Prompts de Limpieza de Datos**
   - Enfocado en la limpieza de los datos, los cuales, son el libro, el guión de la serie, asi como diferentes fuentes historicas.
   - El objetivo es separar los capitulos para previos analisis.
   - Ejemplo:  ¨Reestructura el texto, ya que se ha pegado con un mal formato, NO cambies alguna palabra, solo ajusta el formato por favor, no cambies ninguna palabra, por favor¨

1. **Prompts de Análisis Narrativo**  (validar)
   - Diseñados para evaluar y mejorar la estructura de la trama o identificar inconsistencias narrativas.  
   - Ejemplo: "¿Cómo un evento específico puede ser mejor conectado al conflicto principal de la historia?"
   
2. **Prompts de Desarrollo de Personajes** (validar)
   - Enfocados en profundizar características de los personajes, como motivaciones, diálogo y consistencia con el periodo histórico.  
   - Ejemplo: "¿Cómo un personaje con estas características puede expresar X emoción adaptada al contexto del siglo XIX?"

3. **Prompts de Corrección de Diálogos** (validar)
   - Orientados en revisar y optimizar la calidad de los diálogos, asegurando coherencia histórica, cultural y estilística.  
   - Ejemplo: "Reescribe el siguiente diálogo en español de 1840 con un tono formal y expresivo."

4. **Prompts de Contexto Histórico y Cultural** (validar)
   - Prompts destinados a incorporar vocabulario, expresiones o detalles históricos relevantes para una mayor fidelidad cultural.  
   - Ejemplo: "Describe la vestimenta típica de una persona en California durante 1842 teniendo en cuenta influencias españolas."

5. **Prompts de Estilo Narrativo** (validar)
   - Prompts que ajustan el tono, estilo y lenguaje general del guión a las expectativas del género histórico y dramático.  
   - Ejemplo: "Convierte el siguiente párrafo a un tono más poético que refleje melancolía y nostalgia: [párrafo]."

6. **Prompts de Estructura y Formato Audiovisual** (validar)
   - Pensados para transformar descripciones narrativas en formato técnico de guión audiovisual.  
   - Ejemplo: "Convierte esta narración en un formato de guión técnico con descripciones de escena y diálogos."

7. **Prompts Analíticos y de Métricas Narrativas** (validar)
   - Diseñados para generar resúmenes, analizar coherencia narrativa o identificar patrones en los textos.  
   - Ejemplo: "Resume los eventos principales en esta secuencia del guión, destacando el cambio emocional en los personajes."

---

### 3. Versiones de Prompts
Para este proyecto, los prompts se encuentran en evolución constante. Cada nueva iteración o ajuste en un prompt es importante para optimizar la interacción con los LLMs.

#### Convenciones en las Versiones:
- **v1.x:** Primera versión funcional del prompt, enfoque básico.
- **v2.x:** Modificaciones y mejoras significativas basadas en retroalimentación de los modelos.
- **v3.x en adelante:** Refinamientos avanzados, optimizados según métricas de evaluación cualitativa y perspectiva narrativa.

#### Ejemplos de Nomenclatura:
- `analisis_narrativo_v1.0.md`: Primera versión de un prompt para análisis narrativos.  
- `dialogos_historicos_v2.3.md`: Segunda iteración de prompts relacionados con diálogos de época.  
- `formato_guion_v3.1.md`: Tercera versión refinada para transformar narrativas en formato técnico.

---

### 4. Uso de Prompts para Colaboración (validar)
Además de apoyar el componente narrativo del guión, los prompts generados pueden ser utilizados por el equipo encargado de la generación visual. Estos prompts deben incluir tanto instrucciones técnicas como contexto narrativo para garantizar coherencia entre texto e imagen.

#### Ejemplo:
- **Equipo Narrativo:** Genera un prompt que describe un evento histórico con detalles visuales y emocionales.  
  *"Describe la escena de un atardecer en una misión californiana en 1840. Incluye detalles como la arquitectura, la vestimenta de las personas y la atmósfera pacífica pero cargada de melancolía."*

- **Equipo Visual:** Usa ese prompt como base para introducirlo en un modelo de texto a imagen.  

---

### 5. Contribuciones al Repositorio (validar)
Cualquier modificación, ajuste o nuevo prompt debe seguir estas normas para facilitar su inclusión:
1. Utiliza un nombre descriptivo y la versión correspondiente en el archivo.
2. Incluye una breve introducción sobre el propósito del prompt.
3. Proporciona ejemplos de entrada (`input`) y salida (`output`) esperada para facilitar su comprensión.
4. Documenta las pruebas realizadas o resultados obtenidos en modelos de IA concretos.

---

### 6. Futuras Expansiones (validar)
El repositorio tiene planes de expansión que incluyen:
- **Prompts personalizados por escenas:** Construcción de prompts específicos para eventos clave dentro del guión.  
- **Prompts multi-etapa:** Dividir grandes solicitudes en pasos más pequeños para mejorar la precisión de los modelos.  
- **Historias paralelas:** Creación de prompts que permitan generar spin-offs narrativos sobre personajes secundarios o históricos.  

---

## Conclusión
Este repositorio permite documentar y mejorar continuamente las *instrucciones o prompts*, asegurando que el proyecto *"Los Californios"* maximice el potencial de los modelos de lenguaje en los procesos narrativos y técnicos. Las versiones iterativas y el enfoque de organización por categoría hacen que este repositorio sea un recurso central para la colaboración entre equipos y la creación de un producto final de calidad profesional.

---

## Créditos
### Involucrados:
- **Autor:** *Carlos Peralta Dávila*.  
- **Equipo Técnico:** Colaboradores de la maestría en Inteligencia Artificial Aplicada del **Tecnológico de Monterrey**.  
- **Equipo Visual (Segundo Equipo Californios):** Uso de prompts contextualizados para la generación visual.

---

Bibliografía:  
Se basan fuentes narrativas originales, datos históricos y técnicas de procesamiento de lenguaje natural, incluyendo sistemas **RAG** y adaptaciones como **LoRa** para ajuste de modelos preexistentes.  