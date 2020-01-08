import numpy as np
from global_setting import DICT_SIZE, SCORE_FOLDER, PARAMS_FOLDER
from global_setting import DICTIONARY, POSITIVE_DICTIONRARY
import pandas as pd
import pickle
import os
import datetime
from sklearn.linear_model import LinearRegression
from tools.utils import combine_word_occur_return


def linear_fit(year_train_i, year_train_f):
    """
    :param int year_train_i: the start of the training year
    :param int year_train_f: the end of the training year
    :return:
    """
    # We use close return for training and open return for testing
    # 0 1 2 | 3 4 5 6 7
    # 0-1 1-2 | 2-3 3-4 4-5 5-6 6-7

    # Combining word_occur_return_df
    word_occur_return_df_train = combine_word_occur_return(year_train_i, year_train_f, oc='close')
    close_return_matrix = word_occur_return_df_train['close_price_return'].values
    print(f'{datetime.datetime.now()} Finished Combining word_occur_return_df!')

    # Build cumulative return
    cumulative_close_return_list = []
    # TODO: Try different sets of cumulative return
    for i in range(np.shape(word_occur_return_df_train)[0]):
        close_return_list = close_return_matrix[i]
        cumulative_close_return = sum(close_return_list[2:3])
        cumulative_close_return_list.append(cumulative_close_return)

    # Clean news
    word_occur_matrix_train = word_occur_return_df_train.iloc[:, :DICT_SIZE].values
    r = np.array(cumulative_close_return_list)
    clean_list = np.any(word_occur_matrix_train != 0, axis=1)  # clean news in which no LM_dict word occurs
    word_occur_matrix_train = word_occur_matrix_train[clean_list, :]
    r = r[clean_list]

    # Remove never occurred words
    filter_list = np.any(word_occur_matrix_train != 0, axis=0)
    word_occur_matrix_train_filtered = word_occur_matrix_train[:, filter_list]
    print(f'{datetime.datetime.now()} Finished Building word_occur_matrix {np.shape(word_occur_matrix_train_filtered)} '
          f'and cumulative_close_return {np.shape(r)}!')

    # Linear regression
    reg = LinearRegression(normalize=False, fit_intercept=True).fit(word_occur_matrix_train_filtered, r)
    weights_filtered = reg.coef_
    bias = reg.intercept_

    weights_filtered_index = 0
    weights = []
    for i, val in enumerate(filter_list):
        if val:
            weights.append(weights_filtered[weights_filtered_index])
            weights_filtered_index += 1
        else:
            weights.append(float(0))
    weights = np.array(weights)
    params = np.append(weights, bias)

    # Save params and weights
    save_params(params, year_train_i, year_train_f)
    save_weights(word_occur_matrix_train, weights, year_train_i, year_train_f)


def save_params(params, year_train_i, year_train_f):
    with open(os.path.join(PARAMS_FOLDER, str(year_train_i) + '-' + str(year_train_f) + '.pkl'), 'wb') as handle:
        pickle.dump(params, handle)


def save_weights(word_occur_matrix_train, weights, year_train_i, year_train_f):
    # Relative word occurrence
    absolute_word_occur = np.sum(word_occur_matrix_train, axis=0)
    relative_word_occur = absolute_word_occur / np.linalg.norm(absolute_word_occur)

    # Word tone
    weights = weights / np.linalg.norm(weights)
    tone_list = []
    for id, word in enumerate(DICTIONARY):
        if word in POSITIVE_DICTIONRARY:
            tone_list.append('positive')
        else:
            tone_list.append('negative')

    # WP dataframe
    WP_df = pd.DataFrame(index=DICTIONARY)
    WP_df['word_occur'] = relative_word_occur
    WP_df['score'] = weights
    WP_df['tone'] = tone_list
    WP_df.to_csv(os.path.join(SCORE_FOLDER, str(year_train_i) + '-' + str(year_train_f) + '.csv'))


if __name__ == '__main__':
    linear_fit(1995, 2004)
