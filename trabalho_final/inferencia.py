from MachineLearning import execute_model
from trabalho_final.evaluator import evaluate_best_model

model_exec, name_model = evaluate_best_model()

params = [
    [22584, 2, 178, 95.0, 130, 90, 3, 3, 0, 0, 1],  # Y
    [17668, 1, 158, 71.0, 110, 70, 1, 1, 0, 0, 1],  # N
    [16782, 2, 172, 112.0, 120, 80, 1, 1, 0, 0, 0],  # Y
    [19109, 2, 180, 84.0, 120, 80, 1, 1, 0, 0, 0],  # N
    [10866, 2, 170, 78.0, 120, 80, 3, 1, 0, 1, 1],  # ?
    [8622, 2, 188, 90.0, 130, 90, 1, 1, 0, 0, 1],  # ?
]

# Execute predict with best model evaluate
print("\nTestando modelo "+name_model)
response = execute_model(model_exec, params)
print(response)
