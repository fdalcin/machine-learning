import joblib
import pandas
from sklearn.preprocessing import MinMaxScaler

import config


def to_yes_or_no(value):
    return 'N' if value == 0 else 'Y'


def convert_input(attributes):
    scaling = joblib.load(config.PREPROCESSING_PATH + 'cardio_scaling.sav')

    return scaling.transform(attributes)


def get_data():
    # Carregando dados do CSV
    cardio = pandas.read_csv(config.DATA_PATH + 'cardio_train.csv', sep=';')

    # Removendo coluna de ID
    cardio = cardio.drop('id', axis=1)

    # Convertendo coluna classificadora para caractere
    cardio.cardio = cardio.cardio.map(to_yes_or_no)

    print(cardio)

    # Verificando balanceamento das classes
    print("\nVerificando se há problema de balanceamento nas classes")
    print(cardio.cardio.value_counts())

    attributes = cardio.drop('cardio', axis=1)
    classes = cardio.cardio

    scaling = MinMaxScaler(feature_range=(-1, 1)).fit(attributes)

    attributes = scaling.transform(attributes)

    joblib.dump(scaling, config.PREPROCESSING_PATH + 'cardio_scaling.sav')

    return attributes, classes
