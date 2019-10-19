import pandas
import config
from MachineLearning import MachineLearning, accuracy, validate_model

machine_learning = MachineLearning()

data = pandas.read_csv(config.DATA_PATH + 'diabetes.csv')

attributes = data.drop('class', axis=1)
classes = data['class']

print(classes.value_counts())

# LOGISTIC REGRESSION
filename = 'diabetes_lr'

x_training, x_testing, y_training, y_testing = machine_learning.train_test_split(attributes, classes)

# Módulo indutor
print("\nGerando modelo de Regressão Logística")
response, matrix = machine_learning.generate_logistic_regression(
    x_training, x_testing, y_training, y_testing, filename
)

print(response)

# Módulo de validação
print("\nValidando modelo de Regressão Logística")
response = validate_model(filename, x_testing, y_testing)

print(response)
