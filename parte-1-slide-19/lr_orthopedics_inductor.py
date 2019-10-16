import pandas
import config
from sklearn.utils import resample
from MachineLearning import MachineLearning


def binary_to_char(value):
    return 'N' if value == 0 else 'Y'


machine_learning = MachineLearning()

data = pandas.read_csv(config.DATA_PATH + 'ortopedia.csv', sep=';')

# Convertendo coluna de classificação para caractere
data.Fusao_de_Vertebras = data.Fusao_de_Vertebras.map(binary_to_char)

# Verificando balanceamento de classes
print(data.Fusao_de_Vertebras.value_counts())

# Separando dados das classes
minor = data[data['Fusao_de_Vertebras'] == 'Y']
major = data[data['Fusao_de_Vertebras'] == 'N']

# Rebalanceando a classe com menor número de registros
minor_up_sample = resample(minor, replace=True, n_samples=7900, random_state=None)

# Criando novo dataframe com os dados balanceados
balanced_data = pandas.concat([major, minor_up_sample])

# Separando as colunas de dados da coluna de classificação
attributes = balanced_data.drop(['#', 'Fusao_de_Vertebras'], axis=1)
classes = balanced_data['Fusao_de_Vertebras']

data = minor = major = minor_up_sample = balanced_data = None

attributes = pandas.get_dummies(attributes)

# LOGISTIC REGRESSION
filename = 'orthopedics_lr'

# Módulo indutor
print("\nGerando modelo de Regressão Logística")
response = machine_learning.generate_logistic_regression(attributes, classes, filename)

print(response)

# Módulo de validação
print("\nValidando modelo de Regressão Logística")
response = machine_learning.validate_model(filename, attributes, classes)

print(response)
