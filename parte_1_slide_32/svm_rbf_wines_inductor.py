from MachineLearning import MachineLearning

from parte_1_slide_32.preprocessing import get_data

machine_learning = MachineLearning()

attributes, classes = get_data()

# Módulo indutor
print("\nGerando modelo SVM RBF")
response = machine_learning.generate_svm(attributes, classes, 'wines_svm_rbf', kernel='rbf')

print(response)

# Módulo de validação
print("\nValidando modelo de SVM RBF")
response = machine_learning.validate_model('wines_svm_rbf', attributes, classes)

print(response)
