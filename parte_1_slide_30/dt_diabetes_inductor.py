from MachineLearning import MachineLearning
from parte_1_slide_30.common import get_inductor_params

machine_learning = MachineLearning()

attributes, classes = get_inductor_params()

# LOGISTIC REGRESSION
filename = 'diabetes_dt'

# Módulo indutor
print("\nGerando modelo de Árvore de Decisão")
response = machine_learning.generate_decision_tree(attributes, classes, filename)

print(response)

# Módulo de validação
print("\nValidando modelo de Árvore de Decisão")
response = machine_learning.validate_model(filename, attributes, classes)

print(response)
