import pandas
import config
from sklearn.utils import resample


def get_wine_class(value):
    if value <= 3:
        return 'C_WINE'

    if value <= 6:
        return 'B_WINE'

    return 'A_WINE'


def get_data():
    # Carrega os dados
    wines = pandas.read_csv(config.DATA_PATH + 'winequality-red.csv', sep=';')
    wines['quality'] = wines['quality'].map(get_wine_class)

    # Verificando balanceamento de classes
    print("Quantidade de registros para cada classificação antes do balanceamento")
    print(wines.quality.value_counts())

    good_wines = wines[wines.quality == 'A_WINE']
    regular_wines = wines[wines.quality == 'B_WINE']
    bad_wines = wines[wines.quality == 'C_WINE']

    good_wines_up_sample = resample(good_wines, replace=True, n_samples=1352, random_state=None)
    bad_wines_up_sample = resample(bad_wines, replace=True, n_samples=1365, random_state=None)

    balanced_wines = pandas.concat([good_wines_up_sample, regular_wines, bad_wines_up_sample])

    print("\nQuantidade de registros para cada classificação após o balanceamento")
    print(balanced_wines.quality.value_counts())

    attributes = balanced_wines.drop('quality', axis=1)
    classes = balanced_wines['quality']

    wines = good_wines = bad_wines = regular_wines = balanced_wines = None

    return attributes, classes
