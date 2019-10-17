from MachineLearning import execute_model

params = [
    [22584, 2, 178, 95.0, 130, 90, 3, 3, 0, 0, 1],  # Y
    [17668, 1, 158, 71.0, 110, 70, 1, 1, 0, 0, 1],  # N
    [16782, 2, 172, 112.0, 120, 80, 1, 1, 0, 0, 0],  # Y
    [19109, 2, 180, 84.0, 120, 80, 1, 1, 0, 0, 0],  # N
    [10866, 2, 170, 78.0, 120, 80, 3, 1, 0, 1, 1],  # ?
    [8622, 2, 188, 90.0, 130, 90, 1, 1, 0, 0, 1],  # ?
]

# Decision Tree
print("\nTestando modelo Decision Tree")
response = execute_model('cardio_dt', params)
print(response)

# Logistic Regression
print("\nTestando modelo Logistic Regression")
response = execute_model('cardio_lr', params)
print(response)

# Random Forest
print("\nTestando modelo Random Forest")
response = execute_model('cardio_rf', params)
print(response)

# SVM kernel linear
print("\nTestando modelo SVM Kernel Linear")
response = execute_model('cardio_svm_linear', params)
print(response)

# SVM kernel poly
print("\nTestando modelo SVM Kernel Poly")
response = execute_model('cardio_svm_poly', params)
print(response)
