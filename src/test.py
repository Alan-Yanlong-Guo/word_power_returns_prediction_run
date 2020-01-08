import glob
import pandas as pd
import os
from global_setting import TEMP_FOLDER, PARAMS_FOLDER
import numpy as np
import pickle


def permno_test():
    for file in glob.glob(os.path.join(TEMP_FOLDER, '*.pkl')):
        content = pd.read_pickle(file)
        print(file)
        array0 = content['open_price_return'].dropna().apply(lambda p: p[0]).values
        array1 = content['open_price_return'].dropna().apply(lambda p: p[1]).values
        array2 = content['open_price_return'].dropna().apply(lambda p: p[2]).values
        array3 = content['open_price_return'].dropna().apply(lambda p: p[3]).values
        array4 = content['open_price_return'].dropna().apply(lambda p: p[4]).values
        array5 = content['open_price_return'].dropna().apply(lambda p: p[5]).values
        array6 = content['open_price_return'].dropna().apply(lambda p: p[6]).values
        permno = content['open_price_return'].dropna().index
        print(array0[array0 > 10], list(permno[array0 > 10]))
        print(array1[array1 > 10], list(permno[array1 > 10]))
        print(array2[array2 > 10], list(permno[array2 > 10]))
        print(array3[array3 > 10], list(permno[array3 > 10]))
        print(array4[array4 > 10], list(permno[array4 > 10]))
        print(array5[array5 > 10], list(permno[array5 > 10]))
        print(array6[array6 > 10], list(permno[array6 > 10]))


def shuffle_params():
    for file in glob.glob(os.path.join(PARAMS_FOLDER, '*.pkl')):
        file_name = file.split('/')[-1]
        content = pd.read_pickle(file)
        np.random.shuffle(content[:-1])
        with open(os.path.join('/Volumes/Seagate_2T/word_power/params_random', file_name), 'wb') as handle:
            pickle.dump(content, handle)
