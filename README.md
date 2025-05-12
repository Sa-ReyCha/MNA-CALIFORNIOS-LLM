# MNA-CALIFORNIOS-LLM
Repositorio para el proyecto de MNA Los Californios

# Avance2.Californios - Feature Engineering

Este repositorio contiene el primer entregable del proyecto integrador de la Maestría en Inteligencia Artificial Aplicada del Tecnológico de Monterrey. El análisis se enfoca en los datos narrativos del proyecto “Los Californios”, una obra literaria y televisiva de Carlos Peralta Dávila, con el objetivo de optimizar guiones mediante modelos de lenguaje generativos.

## Objetivo del análisis
El objetivo principal de este EDA es:
- Identificar y seleccionar características relevantes del texto.
- Corregir problemas en los datos como valores faltantes o atípicos. (En caso de existir) 
- Detectar patrones narrativos, relaciones entre personajes y aspectos estilísticos relevantes.
- Preparar el conjunto para su posterior uso en tareas de generación de texto o apoyo a guiones visuales.

## Avances realizados
### 1. Procesamiento de texto
- Se implementaron funciones para leer y procesar los capítulos del libro y la serie, eliminando caracteres no deseados como asteriscos y símbolos de gato.
- Se utilizó la biblioteca `nltk` para eliminar las stop words en español, mejorando la calidad del texto procesado.

### 2. Separación de capítulos
- Se desarrolló una función para dividir el texto completo en capítulos basados en la palabra clave "Capítulo".
- Los capítulos fueron exportados a archivos `.txt` individuales para facilitar su análisis.

### 3. Resúmenes generados con LLMs
- Se utilizó el modelo GPT-4 para:
  - Reestructurar el formato de los capítulos sin alterar el contenido.
  - Generar resúmenes simples de los capítulos, destacando los eventos principales y los personajes involucrados.
  - Crear resúmenes contextuales que incluyen listas de personajes y sus acciones.

### 4. Visualización de datos
- Se generaron visualizaciones del conteo de palabras por capítulo.
- Se crearon nubes de palabras (word clouds) para identificar términos clave en cada capítulo.

### 5. Análisis comparativo
- Se realizó un análisis preliminar para comparar los capítulos del libro con los episodios de la serie, evaluando la correlación narrativa entre ambos.

## Contenido del repositorio
- 📘 Libreta Jupyter con análisis paso a paso (`1_EDA/eda_llm.ipynb` y `2_DATA TRANSFORMATION/data_trans_llm.ipynb`)
- 📊 Visualizaciones de frecuencias, relaciones y estructuras narrativas
- 🧹 Procesos de limpieza y preprocesamiento textual
- 📝 Resúmenes generados con LLMs
- 📝 Conclusiones y hallazgos

## Datos utilizados (En Google Drive)
- Guiones de “Los Californios” (temporadas 1 y 2)
- Novela original
- Contexto literario e histórico complementario

## Equipo
- Santiago Reyes Chavez - A01027358
- Emmanuel Gallegos Montiel - A01795311

## Ejecución
Para reproducir los resultados, abre y ejecuta las libretas de principio a fin en orden secuencial. (Se necesita una API key para correr los LLMs)

## Link de Datos: (TEC) 
https://drive.google.com/drive/folders/15Zcz6-t0Ccq1mL-yx2e8B65GlkEskAo2?usp=share_link 

## Link De Resumenes: (TEC)
https://docs.google.com/document/d/1TpOw2zCKSGVX_C3qaXRVm4qELDpj8mLLfeDxh5Qhb7U/edit?tab=t.0

## Videos de Sharepoint (TEC)
https://tecmx-my.sharepoint.com/:f:/g/personal/a01027358_tec_mx/EiGUhiFl_SBEuZAu0p4xE2ABWt4dl80qkWCVgIQck9tLTg?e=oGCRrg

---