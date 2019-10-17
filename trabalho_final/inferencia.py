from trabalho_final.common import get_testing_params
from MachineLearning import execute_model

params = get_testing_params()

# Decision Tree
response = execute_model('cardio_dt', params)
print(response)

# Logistic Regression
response = execute_model('cardio_lr', params)
print(response)

# Random Forest
response = execute_model('cardio_rf', params)
print(response)

# SVM kernel linear
response = execute_model('cardio_svm_linear', params)
print(response)

# SVM kernel poly
response = execute_model('cardio_svm_poly', params)
print(response)
