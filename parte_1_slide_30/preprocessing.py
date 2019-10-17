import pandas
import config


def get_data():
    data = pandas.read_csv(config.DATA_PATH + 'diabetes.csv')

    attributes = data.drop('class', axis=1)
    classes = data['class']

    print(classes.value_counts())

    return attributes, classes

