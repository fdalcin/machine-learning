from MachineLearning import MachineLearning

from parte_1_slide_32.preprocessing import get_data

machine_learning = MachineLearning()

attributes, classes = get_data()

# Módulo indutor
print("\nGerando modelo SVM Linear")
response = machine_learning.generate_svm(attributes, classes, 'wines_svm_linear')

print(response)

# Módulo de validação
print("\nValidando modelo de SVM Linear")
response = machine_learning.validate_model('wines_svm_linear', attributes, classes)

print(response)
