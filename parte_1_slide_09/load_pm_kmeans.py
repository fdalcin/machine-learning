import pickle
import config

# Modelo do Kmeans
model_file = config.MODEL_PATH + 'pm25_kmeans.sav'

kmeans_pm25 = pickle.load(open(model_file, 'rb'))

# Executa o predict
result = kmeans_pm25.predict(
    [
        [2010, 1, 2, 0, -16, -4, 1020.0, 1.79, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [2014, 1, 2, 0, -10, -5, 120.0, 1.05, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
    ]
)

# Resultado do cluster
print(result)
