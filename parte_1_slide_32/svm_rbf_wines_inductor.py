from MachineLearning import MachineLearning, validate_model

from parte_1_slide_32.preprocessing import get_data

machine_learning = MachineLearning()

attributes, classes = get_data()

filename = 'wines_svm_rbf'

x_training, x_testing, y_training, y_testing = machine_learning.train_test_split(attributes, classes)

# Módulo indutor
print("\nGerando modelo SVM RBF")
response, matrix = machine_learning.generate_svm(
    x_training, x_testing, y_training, y_testing, filename, kernel='rbf'
)

print(response)

# Módulo de validação
print("\nValidando modelo de SVM RBF")
response = validate_model(filename, x_testing, y_testing, categorical=True)

print(response)
