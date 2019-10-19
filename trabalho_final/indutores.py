from trabalho_final.preprocessing import get_data
from MachineLearning import MachineLearning, accuracy, sensitivity, specificity, validate_model
import json
import config

machine_learning = MachineLearning()
attributes, classes = get_data()
x_training, x_testing, y_training, y_testing = machine_learning.train_test_split(attributes, classes)

json_data = {'results': []}

# Decision Tree
print("\nGerando modelo de Decision Tree")
filename = 'cardio_dt'
response, matrix, auc_roc = machine_learning.generate_decision_tree(
    x_training, x_testing, y_training, y_testing, filename
)
print(response)

print("\nAcurácia")
acc = accuracy(matrix)
print(acc)

print("\nSensibilidade")
sen = sensitivity(matrix)
print(sen)

print("\nEspecificidade")
spe = specificity(matrix)
print(spe)

# print("\nValidação")
# validate = validate_model(filename, x_testing, y_testing)
# print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'Decision Tree',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})


# Logistic Regression
print("\nGerando modelo de Logistic Regression")
filename = 'cardio_lr'
response, matrix, auc_roc = machine_learning.generate_logistic_regression(
    x_training, x_testing, y_training, y_testing, filename
)
print(response)

print("\nAcurácia")
acc = accuracy(matrix)
print(acc)

print("\nSensibilidade")
sen = sensitivity(matrix)
print(sen)

print("\nEspecificidade")
spe = specificity(matrix)
print(spe)

# print("\nValidação")
# validate = validate_model(filename, x_testing, y_testing)
# print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'Logistic Regression',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})


# Random Forest
print("\nGerando modelo de Random Forest")
filename = 'cardio_rf'
response, matrix, auc_roc = machine_learning.generate_random_forest(
    x_training, x_testing, y_training, y_testing, filename
)
print(response)

print("\nAcurácia")
acc = accuracy(matrix)
print(acc)

print("\nSensibilidade")
sen = sensitivity(matrix)
print(sen)

print("\nEspecificidade")
spe = specificity(matrix)
print(spe)

# print("\nValidação")
# validate = validate_model(filename, x_testing, y_testing)
# print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'Random Forest',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})


# SVM kernel linear
print("\nGerando modelo de SVM Kernel Linear")
filename = 'cardio_svm_linear'
response, matrix, auc_roc = machine_learning.generate_svm(
    x_training, x_testing, y_training, y_testing, filename
)
print(response)

print("\nAcurácia")
acc = accuracy(matrix)
print(acc)

print("\nSensibilidade")
sen = sensitivity(matrix)
print(sen)

print("\nEspecificidade")
spe = specificity(matrix)
print(spe)

# print("\nValidação")
# validate = validate_model(filename, x_testing, y_testing)
# print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'SVM Kernel Linear',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})


# SVM kernel poly
print("\nGerando modelo de SVM Kernel Poly")
filename = 'cardio_svm_poly'
response, matrix, auc_roc = machine_learning.generate_svm(
    x_training, x_testing, y_training, y_testing, filename, kernel='poly'
)
print(response)

print("\nAcurácia")
acc = accuracy(matrix)
print(acc)

print("\nSensibilidade")
sen = sensitivity(matrix)
print(sen)

print("\nEspecificidade")
spe = specificity(matrix)
print(spe)

# print("\nValidação")
# validate = validate_model(filename, x_testing, y_testing)
# print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'SVM Kernel Poly',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})


# SVM kernel RBF
print("\nGerando modelo de SVM Kernel RBF")
filename = 'cardio_svm_rbf'
response, matrix, auc_roc = machine_learning.generate_svm(
    x_training, x_testing, y_training, y_testing, filename, kernel='rbf'
)
print(response)

print("\nAcurácia")
acc = accuracy(matrix)
print(acc)

print("\nSensibilidade")
sen = sensitivity(matrix)
print(sen)

print("\nEspecificidade")
spe = specificity(matrix)
print(spe)

# print("\nValidação")
# validate = validate_model(filename, x_testing, y_testing)
# print(validate)

json_data['results'].append({
    'model': filename,
    'inductor': 'SVM Kernel RBF',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})


filename = config.EVALUATE_PATH + 'results.json'
with open(filename, 'w') as outfile:
    json.dump(json_data, outfile)
