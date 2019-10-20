import pandas
import config
import MachineLearning

ml = MachineLearning.MachineLearning()

data = pandas.read_csv(config.DATA_PATH + 'diabetes.csv')

attributes = data.drop('class', axis=1)
classes = data['class']

print(classes.value_counts())

# LOGISTIC REGRESSION
filename = 'diabetes_lr'

x_training, x_testing, y_training, y_testing = ml.train_test_split(attributes, classes)

# Módulo indutor
print("\nGerando modelo de Regressão Logística")
response, y_predict = ml.generate_logistic_regression(
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
