## Atividade Final

1. Selecionar uma base de dados de seu interesse (própria, de empresa, da UCI, do Kaggle, do KdNuggets ou outra) . Aponte a fonte da base e descreva-a de forma a permitir sua compreensão. Esta base representa um domínio ou contexto que enseja um questionamento ou problema a ser resolvido. Que problema é esse?

2. Desenvolva uma aplicação de Machine Learning para responder a alguma questão / problema relacionada com a base de dados, com as seguintes funcionalidades:
  
    2.1 Módulo de indução (obter padrões) capaz de rodar mais de um modelo e selecionar qual modelo é mais adequado.
      
    2.2 Módulo de avaliação da acurácia dos modelos (atenção aos indicadores de especificidade e sensibilidade, caso necessário)
  
    2.3 Módulo de inferência, com um sensor, a partir do qual seja possível classificar novas instâncias.

## Resultados

1. [Cardiovascular Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset)

    - 1.1 Nossa base provem da área da saúde, disponibilizada pelo kaggle. Nela estão contidos e distribuídos cerca de 72 mil pessoas com e sem doenças cardíacas, estes são os atributos contidos:

        -  1.1.1  Age | Objective Feature | age | int (days)    
    
        -  1.1.2  Height | Objective Feature | height | int (cm)
    
        -  1.1.3  Weight | Objective Feature | weight | float (kg)
    
        -  1.1.4  Gender | Objective Feature | gender | categorical code
    
        -  1.1.5  Systolic blood pressure | Examination Feature | ap_hi | int 
    
        -  1.1.6  Diastolic blood pressure | Examination Feature | ap_lo | int
    
        -  1.1.7  Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal
    
        -  1.1.8  Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal
    
        -  1.1.9  Smoking | Subjective Feature | smoke | binary
    
        -  1.1.10 Alcohol intake | Subjective Feature | alco | binary
    
        -  1.1.11 Physical activity | Subjective Feature | active | binary
    
        -  1.1.12 Presence or absence of cardiovascular disease | Target Variable | cardio | binary

    - 1.2 De acordo com nossa análise dos dados, as colunas de 1.1.1 à 1.1.11 foram utilizadas para geração dos modelos, sendo que a coluna 1.1.12 é a classificação do registro.
    
    - 1.3 O objetivo da aplicação é gerar o melhor modelo possível que seja capaz de inferir se o indivídio possui ou não doença cardiovascular.

2. Aplicação

    - 2.1 Ordem de Execução
        - 2.1.1 Executar o arquivo indutores.py
        
            Responsável por gerar os modelos Decision Tree, Logistic Regression, Random Forest e SVM (Linear, RBF e Poly) e salvar as informações de acurácia do mesmo para futura avaliação.
         
        - 2.1.2 Executar o arquivo inferencia.py
        
            Responsável por buscar qual o melhor modelo gerado nos indutores, pedir para o usuário preencher os valores necessários e executar a predição. Respondendo 'Y' para 'Possui Doença Cardiovascular' e 'N' para 'Não Possui Doença Cardiovascular'.
            
    - 2.2 Modelo de avaliação
        - 2.2.1 O arquivo evaluator.py é responsável por retornar o melhor modelo gerado, é chamado antes de ser realizada a inferência e depois da geração de modelos e da geração do arquivos results.json.
