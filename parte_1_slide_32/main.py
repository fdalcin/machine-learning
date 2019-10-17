from MachineLearning import execute_model, probability
from parte_1_slide_32.common import get_testing_params

testing_params = get_testing_params()

print("\nCalculando probabilidade SVM Linear")
response = probability('wines_svm_linear', testing_params)

print(response)

print("\nTestando valores para modelo SVM Linear")
response = execute_model('wines_svm_linear', testing_params)

print(response)

print("\nCalculando probabilidade SVM RBF")
response = probability('wines_svm_rbf', testing_params)

print(response)

print("\nTestando valores para modelo SVM RBF")
response = execute_model('wines_svm_rbf', testing_params)

print(response)

print("\nCalculando probabilidade Random Forest")
response = probability('wines_rf', testing_params)

print(response)

print("\nTestando valores para modelo Random Forest")
response = execute_model('wines_rf', testing_params)

print(response)
