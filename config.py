import os

BASE_PATH = os.path.abspath(os.pardir)

if not BASE_PATH.endswith('/'):
    BASE_PATH += '/'

DATA_PATH = BASE_PATH + 'data/'
MODEL_PATH = BASE_PATH + 'model/'
