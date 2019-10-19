import pickle
import pandas as pd
from sklearn.cluster import KMeans
import config

# Pega o csv
df = pd.read_csv(config.DATA_PATH + "pm25.csv", sep=";")

# Executa o dummies apra converter as colunas categoricas
df_normalize = pd.get_dummies(df)

# Executa o arquivo do Kmean com 4 cluster - LEVE/MEDIO/ALTO/NOCISVO
kmeans = KMeans(n_clusters=4).fit(df_normalize)

# Salvar modelo
# Finalizar o modelo
filename = config.MODEL_PATH + 'pm25_kmeans.sav'
pickle.dump(kmeans, open(filename, 'wb'))
