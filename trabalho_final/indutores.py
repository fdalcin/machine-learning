from trabalho_final.preprocessing import get_data
from MachineLearning import MachineLearning

machine_learning = MachineLearning()
attributes, classes = get_data()

# Decision Tree
print("\nGerando modelo de Decision Tree")
response = machine_learning.generate_decision_tree(attributes, classes, 'cardio_dt')
print(response)

# Logistic Regression
print("\nGerando modelo de Logistic Regression")
response = machine_learning.generate_logistic_regression(attributes, classes, 'cardio_lr')
print(response)

# Random Forest
print("\nGerando modelo de Random Forest")
response = machine_learning.generate_random_forest(attributes, classes, 'cardio_rf')
print(response)

# SVM kernel linear
print("\nGerando modelo de SVM Kernel Linear")
response = machine_learning.generate_svm(attributes, classes, 'cardio_svm_linear')
print(response)

# SVM kernel poly
print("\nGerando modelo de SVM Kernel Poly")
response = machine_learning.generate_svm(attributes, classes, 'cardio_svm_poly', kernel='poly')
print(response)
