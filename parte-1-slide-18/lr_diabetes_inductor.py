import pandas
import config
from MachineLearning import MachineLearning

machine_learning = MachineLearning()

data = pandas.read_csv(config.DATA_PATH + 'diabetes.csv')

attributes = data.drop('class', axis=1)
classes = data['class']

print(classes.value_counts())

# LOGISTIC REGRESSION
filename = 'diabetes_lr'

# Módulo indutor
print("\nGerando modelo de Regressão Logística")
response = machine_learning.generate_logistic_regression(attributes, classes, filename)

print(response)

# Módulo de validação
print("\nValidando modelo de Regressão Logística")
response = machine_learning.validate_model(filename, attributes, classes)

print(response)
