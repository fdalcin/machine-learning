from MachineLearning import MachineLearning
from parte_1_slide_30.common import get_inductor_params

machine_learning = MachineLearning()

attributes, classes = get_inductor_params()

# LOGISTIC REGRESSION
filename = 'diabetes_rf'

# Módulo indutor
print("\nGerando modelo de Random Forest")
response = machine_learning.generate_random_forest(attributes, classes, filename)

print(response)

# Módulo de validação
print("\nValidando modelo de Random Forest")
response = machine_learning.validate_model(filename, attributes, classes)

print(response)
