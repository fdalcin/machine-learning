from trabalho_final.preprocessing import get_data
from MachineLearning import MachineLearning, accuracy, sensitivity, specificity

machine_learning = MachineLearning()
attributes, classes = get_data()

# Decision Tree
print("\nGerando modelo de Decision Tree")
response, auc_roc, matrix, report = machine_learning.generate_decision_tree(attributes, classes, 'cardio_dt')
print(response)
print("\nAcurácia")
print(accuracy(matrix))
print("\nSensibilidade")
print(sensitivity(matrix))
print("\nEspecificidade")
print(specificity(matrix))

# Logistic Regression
print("\nGerando modelo de Logistic Regression")
response, auc_roc, matrix, report = machine_learning.generate_logistic_regression(attributes, classes, 'cardio_lr')
print(response)
print("\nAcurácia")
print(accuracy(matrix))
print("\nSensibilidade")
print(sensitivity(matrix))
print("\nEspecificidade")
print(specificity(matrix))

# Random Forest
print("\nGerando modelo de Random Forest")
response, auc_roc, matrix, report = machine_learning.generate_random_forest(attributes, classes, 'cardio_rf')
print(response)
print("\nAcurácia")
print(accuracy(matrix))
print("\nSensibilidade")
print(sensitivity(matrix))
print("\nEspecificidade")
print(specificity(matrix))

# SVM kernel linear
print("\nGerando modelo de SVM Kernel Linear")
response, auc_roc, matrix, report = machine_learning.generate_svm(attributes, classes, 'cardio_svm_linear')
print(response)
print("\nAcurácia")
print(accuracy(matrix))
print("\nSensibilidade")
print(sensitivity(matrix))
print("\nEspecificidade")
print(specificity(matrix))

# SVM kernel poly
print("\nGerando modelo de SVM Kernel Poly")
response, auc_roc, matrix, report = machine_learning.generate_svm(attributes, classes, 'cardio_svm_poly', kernel='poly')
print(response)
print("\nAcurácia")
print(accuracy(matrix))
print("\nSensibilidade")
print(sensitivity(matrix))
print("\nEspecificidade")
print(specificity(matrix))
