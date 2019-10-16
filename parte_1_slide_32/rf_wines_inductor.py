from MachineLearning import MachineLearning

from parte_1_slide_32.common import get_inductor_params

machine_learning = MachineLearning()

attributes, classes = get_inductor_params()

# Módulo indutor
print("\nGerando modelo Random Forest")
response = machine_learning.generate_random_forest(attributes, classes, 'wines_rf')

print(response)

# Módulo de validação
print("\nValidando modelo de Random Forest")
response = machine_learning.validate_model('wines_rf', attributes, classes)

print(response)