from MachineLearning import MachineLearning, validate_model
from parte_1_slide_30.preprocessing import get_data

machine_learning = MachineLearning()

attributes, classes = get_data()

# LOGISTIC REGRESSION
filename = 'diabetes_rf'

x_training, x_testing, y_training, y_testing = machine_learning.train_test_split(attributes, classes)

# Módulo indutor
print("\nGerando modelo de Random Forest")
response, matrix = machine_learning.generate_random_forest(
    x_training, x_testing, y_training, y_testing, filename
)

print(response)

# Módulo de validação
print("\nValidando modelo de Random Forest")
response = validate_model(filename, x_testing, y_testing)

print(response)
