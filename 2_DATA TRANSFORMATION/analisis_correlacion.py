
# Análisis de Correlación entre Capítulos de un Libro y Episodios de una Serie

import os
import zipfile
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# === 1. Extracción de archivos de texto ===

def extraer_zip(ruta_zip, carpeta_destino):
    with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
        zip_ref.extractall(carpeta_destino)

# Extraer episodios
ruta_zip_episodios = "EPISODIOS_LIMPIOS.zip"
carpeta_destino = "episodios_limpios"
extraer_zip(ruta_zip_episodios, carpeta_destino)

# Leer archivos de episodios
carpeta_episodios = os.path.join(carpeta_destino, "EPISODIOS_LIMPIOS", "temporada_1")
episodios = {}
for archivo in sorted(os.listdir(carpeta_episodios)):
    with open(os.path.join(carpeta_episodios, archivo), 'r', encoding='utf-8') as f:
        episodios[archivo] = f.read()

# === 2. Lectura de capítulos desde documento Word ===

from docx import Document

def leer_capitulos_desde_docx(ruta_docx):
    doc = Document(ruta_docx)
    full_text = "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])
    partes = re.split(r"\nC\.(\d+)\s+", full_text)
    capitulos = {}
    for i in range(1, len(partes), 2):
        cap = f"C{partes[i]}"
        texto = partes[i + 1].strip()
        capitulos[cap] = texto
    return capitulos

capitulos = leer_capitulos_desde_docx("Resumenes_EDA.docx")

# === 3. Vectorización y cálculo de similitud TF-IDF ===

cap_keys = list(capitulos.keys())
cap_texts = [capitulos[k] for k in cap_keys]
ep_keys = list(episodios.keys())
ep_texts = [episodios[k] for k in ep_keys]

vectorizer = TfidfVectorizer(max_features=10000)
tfidf_matrix = vectorizer.fit_transform(cap_texts + ep_texts)
cap_matrix = tfidf_matrix[:len(cap_texts)]
ep_matrix = tfidf_matrix[len(cap_texts):]

similarity_matrix = cosine_similarity(cap_matrix, ep_matrix)
sim_df = pd.DataFrame(similarity_matrix, index=cap_keys, columns=ep_keys)

# === 4. Generación de resumen por episodio ===

resumen = pd.DataFrame({
    "Episodio": sim_df.columns,
    "Capítulo Principal": sim_df.idxmax().values,
    "Capítulos Combinados (>0.60)": [sim_df[ep][sim_df[ep] > 0.60].index.tolist() for ep in sim_df.columns]
})
resumen["N° Capítulos Combinados"] = resumen["Capítulos Combinados (>0.60)"].apply(len)

# === 5. Visualización: gráfico de barras ===

plt.figure(figsize=(10, 6))
sns.barplot(data=resumen.sort_values("Episodio"), x="Episodio", y="N° Capítulos Combinados", color="skyblue")
plt.title("Cantidad de Capítulos Combinados por Episodio")
plt.ylabel("Capítulos con Similitud > 0.60")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("barras_episodios.png")
plt.close()

# === 6. Visualización: heatmap de similitud ===

heatmap_df = sim_df[[col for col in sorted(sim_df.columns)]]
cap_filtro = heatmap_df.max(axis=1)[heatmap_df.max(axis=1) > 0.60].index.tolist()
filtered = heatmap_df.loc[cap_filtro]

plt.figure(figsize=(12, 10))
sns.heatmap(filtered, annot=True, cmap="YlGnBu", fmt=".2f", cbar_kws={'label': 'Similitud TF-IDF'})
plt.title("Mapa de Calor: Similitud entre Capítulos y Episodios")
plt.xlabel("Episodios")
plt.ylabel("Capítulos del Libro")
plt.tight_layout()
plt.savefig("heatmap_correlacion.png")
plt.close()

# === 7. Guardar resumen como CSV para repositorio ===
resumen.to_csv("resumen_correlacion.csv", index=False)
