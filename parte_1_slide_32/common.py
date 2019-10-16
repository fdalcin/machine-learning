import pandas
import config
from sklearn.utils import resample


def get_wine_class(value):
    if value <= 3:
        return 'C_WINE'

    if value <= 6:
        return 'B_WINE'

    return 'A_WINE'


def get_inductor_params():
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


def get_testing_params():
    return [
        [6.7, 0.76, 0.02, 1.8, 0.078, 6, 12, 0.996, 3.55, 0.63, 9.95],  # C_WINE
        [6.6, 0.61, 0.01, 1.9, 0.08, 8, 25, 0.99746, 3.69, 0.73, 10.5],  # B_WINE
        [10.7, 0.52, 0.38, 2.6, 0.066, 29, 56, 0.99577, 3.15, 0.79, 12.1],  # A_WINE
        [9.5, 0.72, 0.24, 2.3, 0.07, 21, 47, 0.9962, 3.54, 0.70, 11.3]  # ?
    ]
