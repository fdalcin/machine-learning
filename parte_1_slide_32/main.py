from MachineLearning import execute_model, probability

testing_params = [
    [6.7, 0.76, 0.02, 1.8, 0.078, 6, 12, 0.996, 3.55, 0.63, 9.95],  # C_WINE
    [6.6, 0.61, 0.01, 1.9, 0.08, 8, 25, 0.99746, 3.69, 0.73, 10.5],  # B_WINE
    [10.7, 0.52, 0.38, 2.6, 0.066, 29, 56, 0.99577, 3.15, 0.79, 12.1],  # A_WINE
    [9.5, 0.72, 0.24, 2.3, 0.07, 21, 47, 0.9962, 3.54, 0.70, 11.3]  # ?
]

print("\nTestando valores para modelo SVM Linear")
response = execute_model('wines_svm_linear', testing_params)

print(response)

print("\nTestando valores para modelo SVM RBF")
response = execute_model('wines_svm_rbf', testing_params)

print(response)

print("\nTestando valores para modelo Random Forest")
response = execute_model('wines_rf', testing_params)

print(response)
