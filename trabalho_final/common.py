import pandas
import config


def convert_to_y_or_n(value):
    return 'N' if value == 0 else 'Y'


def get_inductor_params():
    # Carregando dados do CSV
    cardio = pandas.read_csv(config.DATA_PATH + 'cardio_train.csv', sep=';')

    # Removendo coluna de ID
    cardio = cardio.drop('id', axis=1)

    # Convertendo coluna classificadora para caractere
    cardio.cardio = cardio.cardio.map(convert_to_y_or_n)

    print(cardio)

    # Verificando balanceamento das classes
    print("\nVerificando se há problema de balanceamento nas classes")
    print(cardio.cardio.value_counts())

    attributes = cardio.drop('cardio', axis=1)
    classes = cardio.cardio

    return attributes, classes


def get_testing_params():
    return [
        [22584, 2, 178, 95.0, 130, 90, 3, 3, 0, 0, 1],  # Y
        [17668, 1, 158, 71.0, 110, 70, 1, 1, 0, 0, 1],  # N
        [16782, 2, 172, 112.0, 120, 80, 1, 1, 0, 0, 0],  # Y
        [19109, 2, 180, 84.0, 120, 80, 1, 1, 0, 0, 0],  # N
        [10866, 2, 170, 78.0, 120, 80, 3, 1, 0, 1, 1],  # ?
        [8622, 2, 188, 90.0, 130, 90, 1, 1, 0, 0, 1],  # ?
    ]
