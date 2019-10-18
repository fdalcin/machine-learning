from trabalho_final.preprocessing import get_data
from MachineLearning import MachineLearning, accuracy, sensitivity, specificity
import json
import config

machine_learning = MachineLearning()
attributes, classes = get_data()

json_data = {}
json_data['results'] = []

# Decision Tree
print("\nGerando modelo de Decision Tree")
response, auc_roc, matrix, report = machine_learning.generate_decision_tree(attributes, classes, 'cardio_dt')
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

json_data['results'].append({
    'model': 'cardio_dt',
    'inductor': 'Decision Tree',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})

# Logistic Regression
print("\nGerando modelo de Logistic Regression")
response, auc_roc, matrix, report = machine_learning.generate_logistic_regression(attributes, classes, 'cardio_lr')
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

json_data['results'].append({
    'model': 'cardio_lr',
    'inductor': 'Logistic Regression',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})

# Random Forest
print("\nGerando modelo de Random Forest")
response, auc_roc, matrix, report = machine_learning.generate_random_forest(attributes, classes, 'cardio_rf')
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

json_data['results'].append({
    'model': 'cardio_rf',
    'inductor': 'Random Forest',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})

# SVM kernel linear
print("\nGerando modelo de SVM Kernel Linear")
response, auc_roc, matrix, report = machine_learning.generate_svm(attributes, classes, 'cardio_svm_linear')
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

json_data['results'].append({
    'model': 'cardio_svm_linear',
    'inductor': 'SVM Kernel Linear',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})

# SVM kernel poly
print("\nGerando modelo de SVM Kernel Poly")
response, auc_roc, matrix, report = machine_learning.generate_svm(attributes, classes, 'cardio_svm_poly', kernel='poly')
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

json_data['results'].append({
    'model': 'cardio_svm_poly',
    'inductor': 'SVM Kernel Poly',
    'acc': acc,
    'sen': sen,
    'spe': spe,
    'roc': auc_roc,
})

filename = config.EVALUATE_PATH + 'results.json'
with open(filename, 'w') as outfile:
    json.dump(json_data, outfile)
