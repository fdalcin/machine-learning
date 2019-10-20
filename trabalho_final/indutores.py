from trabalho_final.preprocessing import get_data
import MachineLearning
import json
import config

ml = MachineLearning.MachineLearning()

attributes, classes = get_data()
x_training, x_testing, y_training, y_testing = ml.train_test_split(attributes, classes)

json_data = {'results': []}

# Decision Tree
print("\nGerando modelo de Decision Tree")
filename = 'cardio_dt'
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

print("\nValidação")
validate = MachineLearning.validate_model(filename, x_testing, y_testing)
print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'Decision Tree',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': validate['auc_roc']
})


# Logistic Regression
print("\nGerando modelo de Logistic Regression")
filename = 'cardio_lr'
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

print("\nValidação")
validate = MachineLearning.validate_model(filename, x_testing, y_testing)
print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'Logistic Regression',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': validate['auc_roc']
})


# Random Forest
print("\nGerando modelo de Random Forest")
filename = 'cardio_rf'
response, y_predict = ml.generate_random_forest(
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

print("\nValidação")
validate = MachineLearning.validate_model(filename, x_testing, y_testing)
print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'Random Forest',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': validate['auc_roc']
})


# SVM kernel linear
print("\nGerando modelo de SVM Kernel Linear")
filename = 'cardio_svm_linear'
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

print("\nValidação")
validate = MachineLearning.validate_model(filename, x_testing, y_testing)
print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'SVM Kernel Linear',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': validate['auc_roc']
})


# SVM kernel poly
print("\nGerando modelo de SVM Kernel Poly")
filename = 'cardio_svm_poly'
response, y_predict = ml.generate_svm(
    x_training, x_testing, y_training, filename, kernel='poly'
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

print("\nValidação")
validate = MachineLearning.validate_model(filename, x_testing, y_testing)
print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'SVM Kernel Poly',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': validate['auc_roc']
})


# SVM kernel RBF
print("\nGerando modelo de SVM Kernel RBF")
filename = 'cardio_svm_rbf'
response, y_predict = ml.generate_svm(
    x_training, x_testing, y_training, filename, kernel='rbf'
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

print("\nValidação")
validate = MachineLearning.validate_model(filename, x_testing, y_testing)
print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'SVM Kernel RBF',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': validate['auc_roc']
})


filename = config.EVALUATE_PATH + 'results.json'
with open(filename, 'w') as outfile:
    json.dump(json_data, outfile)
