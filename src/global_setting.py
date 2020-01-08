import pandas as pd
import glob
import os
import numpy as np
# import wrds
# conn = wrds.Connection(wrds_username='dachxiu')

# Parameters
DICT_SIZE = 866
PORTFOLIO_LONG_SIZE = 50
PORTFOLIO_SHORT_SIZE = 50

DELAY = 4

TRAIN_LEN = 10
CROSS_LEN = 5
TEST_LEN = 1

YEAR_MIN = 1989
YEAR_MAX = 2016
YEAR_TRAIN_MIN = YEAR_MIN
YEAR_TRAIN_MAX = YEAR_MAX - TRAIN_LEN - CROSS_LEN - TEST_LEN + 1
YEAR_TRAIN_LIST_I = list(np.arange(YEAR_TRAIN_MIN, YEAR_TRAIN_MAX + 1))
YEAR_TRAIN_LIST_F = list(np.arange(YEAR_TRAIN_MIN + TRAIN_LEN - 1, YEAR_TRAIN_MAX + TRAIN_LEN - 1 + 1))
YEAR_TRAIN_LIST = [[YEAR_TRAIN_LIST_I[i], YEAR_TRAIN_LIST_F[i]] for i in range(len(YEAR_TRAIN_LIST_I))]

YEAR_TEST_MIN = YEAR_TRAIN_MIN + TRAIN_LEN + CROSS_LEN
YEAR_TEST_MAX = YEAR_TRAIN_MAX + TRAIN_LEN + CROSS_LEN
YEAR_TEST_LIST_I = list(np.arange(YEAR_TEST_MIN, YEAR_TEST_MAX + 1))
YEAR_TEST_LIST_F = list(np.arange(YEAR_TEST_MIN + TEST_LEN - 1, YEAR_TEST_MAX + TEST_LEN - 1 + 1))
YEAR_TEST_LIST = [[YEAR_TEST_LIST_I[i], YEAR_TEST_LIST_F[i]] for i in range(len(YEAR_TEST_LIST_I))]

# Parent Directories
DATA_FOLDER = '/floyd/input'
LOOK_UP_FOLDER = '/floyd/input/lookup'
CRSP_FOLDER = '/floyd/input/crsp'  # '/Volumes/Seagate_2T/word_power/crsp'
NEWS_FOLDER = '/floyd/input/news'  # '/Volumes/Seagate_2T/word_power/news'
TEMP_FOLDER = '/floyd/homme/src/temp'
SCORE_FOLDER = '/Volumes/Seagate_2T/word_power/score'
PARAMS_FOLDER = '/Volumes/Seagate_2T/word_power/params'
RETURN_FOLDER = '/Volumes/Seagate_2T/word_power/return'
ANALYSIS_FOLDER = '/Volumes/Seagate_2T/word_power/analysis'

# Lookup Directories
LINK_TABLE = pd.read_csv(os.path.join(LOOK_UP_FOLDER, 'link.txt'), sep='\t', encoding='latin1', dtype='str')
LINK_TABLE.set_index('sym_root', inplace=True)
DICTIONARY_FILE = LOOK_UP_FOLDER + '/Loughran_McDonald_SentimentWordLists_2018.xlsx'
DICTIONARY_ = list(pd.read_excel(DICTIONARY_FILE, 'Clean', header=None, dtype=str).iloc[:, 0])
DICTIONARY = [word.lower() for word in DICTIONARY_]
NEGATIVE_DICTIONRARY_ = list(pd.read_excel(DICTIONARY_FILE, 'Clean_Negative', header=None, dtype=str).iloc[:, 0])
NEGATIVE_DICTIONRARY = [word.lower() for word in NEGATIVE_DICTIONRARY_]
POSITIVE_DICTIONRARY_ = list(pd.read_excel(DICTIONARY_FILE, 'Clean_Positive', header=None, dtype=str).iloc[:, 0])
POSITIVE_DICTIONRARY = [word.lower() for word in POSITIVE_DICTIONRARY_]
SP500_TABLE = pd.read_csv(LOOK_UP_FOLDER + '/sp500.csv', index_col=0, encoding='utf-8')

# NEWS Path List
NEWS_PATH_LIST = []
for path in glob.glob(os.path.join(NEWS_FOLDER, '*.pkl')):
    NEWS_PATH_LIST.append(str(path))

# TEMP Path Lists
TEMP_PATH_LIST = []
for path in glob.glob(os.path.join(TEMP_FOLDER, '*.pkl')):
    TEMP_PATH_LIST.append(str(path))
