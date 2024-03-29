import pandas
import config
from sklearn.utils import resample
import MachineLearning


def binary_to_char(value):
    return 'N' if value == 0 else 'Y'


ml = MachineLearning.MachineLearning()

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

x_training, x_testing, y_training, y_testing = ml.train_test_split(attributes, classes)

# LOGISTIC REGRESSION
filename = 'orthopedics_dt'

# Módulo indutor
print("\nGerando modelo de Regressão Logística")
response, y_predict = ml.generate_decision_tree(
    x_training, x_testing, y_training, filename
)

print(response)

matrix = MachineLearning.conf_matrix(y_testing, y_predict)

MachineLearning.report(y_testing, y_predict)

print("\nAcurácia")
acc = MachineLearning.accuracy(matrix)
print(acc)

print("\nSensibilidade")
sen = MachineLearning.sensitivity(matrix)
print(sen)

print("\nEspecificidade")
spe = MachineLearning.specificity(matrix)
print(spe)

print("\nValidando modelo")
validate = MachineLearning.validate_model(filename, x_testing, y_testing)
print(validate)
