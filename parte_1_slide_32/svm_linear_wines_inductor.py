import MachineLearning

from parte_1_slide_32.preprocessing import get_data

ml = MachineLearning.MachineLearning()

attributes, classes = get_data()

filename = 'wines_svm_linear'

x_training, x_testing, y_training, y_testing = ml.train_test_split(attributes, classes)

# Módulo indutor
print("\nGerando modelo SVM Linear")
response, y_predict = ml.generate_svm(
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
validate = MachineLearning.validate_model(filename, x_testing, y_testing, categorical=True)
print(validate)
