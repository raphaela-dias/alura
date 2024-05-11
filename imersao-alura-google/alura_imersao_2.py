import google.generativeai as genai
import numpy as np
import pandas as pd

genai.configure(api_key = google_api_key)

#Lista modelos para geração de embeddings
# for m in genai.list_models():
#     if 'embedContent' in m.supported_generation_methods:
#         print(m.name)

#Listagem de documentos que serão buscados
DOCUMENTO1 = {
    "Título": "Anúbis",
    "Conteúdo": "Anúbis ( /əˈnjuːbᵻs/;[1] em grego clássico: Ἄνουβις) ou Anupo é, no panteão do Antigo Egito, o deus dos mortos e moribundos, que guiava e conduzia as almas ao mundo dos mortos.[2] É representado com cabeça de chacal, embora os egiptólogos mais conservadores afirmem que não há como saber com certeza o animal que o representa."
}

DOCUMENTO2 = {
    "Título": "Saturno",
    "Conteúdo": "Saturno é o sexto planeta a partir do Sol e o segundo maior do Sistema Solar atrás de Júpiter. Pertencente ao grupo dos gigantes gasosos, possui cerca de 95 massas terrestres e orbita a uma distância média de 9,5 unidades astronômicas."
}

DOCUMENTO3 = {
    "Título": "Ornitorrinco",
    "Conteúdo": "O ornitorrinco (nome científico: Ornithorhynchus anatinus, do grego: ornitho, ave + rhynchus, bico; e do latim: anati, pato + inus, semelhante a: 'com bico de ave, semelhante a pato') é um mamífero semiaquático natural da Austrália e Tasmânia. É o único representante vivo da família Ornithorhynchidae, e a única espécie do gênero Ornithorhynchus. Juntamente com as equidnas, formam o grupo dos monotremados, os únicos mamíferos ovíparos existentes. A espécie é monotípica, ou seja, não tem subespécies ou variedades reconhecidas."
}

documents = [DOCUMENTO1, DOCUMENTO2, DOCUMENTO3]

#Transformação dos documentos em dataframes
df = pd.DataFrame(documents)

model = 'models/embedding-001'

# Cria embeddings em uma nova coluna no dataframe
def embed_fn(title, text, model):
    return genai.embed_content(
    model = model,
    title= title,
    content = text,
    task_type = 'RETRIEVAL_DOCUMENT')['embedding']

df['Embeddings'] = df.apply(lambda row: embed_fn(row['Título'], row['Conteúdo'], model), axis=1)

#Geração da resposta
def gerar_e_buscar_consulta(consulta, model):
    embedding_da_consulta = genai.embed_content(
        model = model,
        content = consulta,
        task_type = 'RETRIEVAL_QUERY')['embedding']
    
    #Cálculo da distância entre a pergunta e os embeddings
    produtos_escalares = np.dot(np.stack(df['Embeddings']), embedding_da_consulta)
    indice = np.argmax(produtos_escalares)

    return df.iloc[indice]['Conteúdo']

consulta = "Me fale sobre ornitorrincos"

resposta = gerar_e_buscar_consulta(consulta, df, model)




