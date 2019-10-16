## Atividade

Utilizar a base notas CSV para descrever as diferenças entre os alunos que permanecem e os alunos que evadem.

Realize o experimento utilizando Simple Kmeans e EM.

Compare os dois resultados.

## Resultados

### Simple KMeans

| Cluster | Instances |
| :--- | :---: |
| 0 - Evadido | 168 (40%) |
| 1 - Ativo | 255 (60%) |

Incorrectly clustered instances: 64.0   **15.13%**

### Expectation Maximization

| Cluster | Instances |
| :--- | :---: |
| 0 - Ativo | 204 (48%) |
| 1 - No class | 109 (26%) |
| 2 - Evadido | 110 (26%) |

Incorrectly clustered instances: 155.0  **36.643%**

### Análise
Conforme os experimentos realizados, pode-se perceber que o método **Simple KMeans** obteve uma melhor aplicação no caso das notas, uma vez que o método **Expectation Maximization** não foi capaz de classificar **109 instâncias (26%)**. O método **EM** também classificou **incorretamente** 155 registros (36,64%) contra 64 registros (15,13%) do método **Simple KMeans**.
