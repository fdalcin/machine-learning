from MachineLearning import execute_model
from trabalho_final.evaluator import evaluate_best_model

model, inductor = evaluate_best_model()

print("\nInforma os dados para inferência:")

age = input('Idade (em dias): ')
gender = input("Gênero (1- Feminino; 2- Masculino): ")
height = input("Altura (em centimetros): ")
weight = input("Peso (em kilogramas): ")
ap_hi = input("Pressão sistolica: ")
ap_lo = input("Pressão diastolica: ")
cholesterol = input("Colesterol (1- Normal; 2- Levemente alto; 3- Muito alto): ")
gluc = input("Glucose (1- Normal; 2- Levemente alto; 3- Muito alto): ")
smoke = input("Fumante (0- Nao; 1- Sim): ")
alco = input("Alcoolotra (0- Nao; 1- Sim): ")
active = input("Pratica Atividades Fisicas (0- Nao; 1- Sim): ")

params = [
    [age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]
]

# Execute predict with best model evaluate
print("\nTestando modelo " + inductor)
response = execute_model(model, params)
print(response)
