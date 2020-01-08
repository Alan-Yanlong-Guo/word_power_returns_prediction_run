from global_setting import NEWS_PATH_LIST
import pandas as pd
import numpy as np
from multiprocessing import Pool
from global_setting import NEWS_FOLDER, DICTIONARY
from tools.word_filter import word_filter


def dict_count(news_word_list):
    # Remove Negator
    negator = ['no', 'not', 'never']
    news_remove_list = []
    for id, word_raw in enumerate(news_word_list):
        if word_raw in negator:
            news_remove_list.append(id - 3)
            news_remove_list.append(id - 2)
            news_remove_list.append(id - 1)
            news_remove_list.append(id)
            news_remove_list.append(id + 1)
            news_remove_list.append(id + 2)
            news_remove_list.append(id + 3)
    news_remove_list = list(set(news_remove_list))

    # Create Dictionary Count List
    dict_count_list = np.zeros(len(DICTIONARY), dtype='int')
    for id, word in enumerate(news_word_list):
        root_word = word_filter(word)
        if (id not in news_remove_list) and (root_word in DICTIONARY):
            index = DICTIONARY.index(root_word)
            dict_count_list[index] += 1

    return dict_count_list


def build_word_occur_return(news_df):
    # Initialize word_occur_matrix
    permno_list = np.array(news_df['permno'])
    return_df = news_df[['est_date', 'est_time',
                         'open_price', 'open_cap', 'open_sp500', 'open_price_return', 'open_sp500_return',
                         'close_price', 'close_cap', 'close_sp500', 'close_price_return', 'close_sp500_return']]

    num_news = np.shape(news_df)[0]
    dict_size = len(DICTIONARY)
    word_occur_matrix = np.zeros((num_news, dict_size))

    # Build word_occur_matrix
    for i, permno in enumerate(permno_list):
        news_article_list = news_df.loc[i, 'Article']
        news_title_list = news_df.loc[i, 'Title']
        news_word_list = news_article_list + news_title_list
        num_word = len(news_word_list)
        dict_count_list = dict_count(news_word_list)

        # open_return_b2 = news_df.loc[i, 'open_return'][0]
        # open_return_b1 = news_df.loc[i, 'open_return'][1]
        # open_return_0 = news_df.loc[i, 'open_return'][2]
        # open_return_1 = news_df.loc[i, 'open_return'][3]
        # open_return_2 = news_df.loc[i, 'open_return'][4]
        # open_return_3 = news_df.loc[i, 'open_return'][5]
        # open_return_4 = news_df.loc[i, 'open_return'][6]
        #
        # close_return_b2 = news_df.loc[i, 'close_return'][0]
        # close_return_b1 = news_df.loc[i, 'close_return'][1]
        # close_return_0 = news_df.loc[i, 'close_return'][2]
        # close_return_1 = news_df.loc[i, 'close_return'][3]
        # close_return_2 = news_df.loc[i, 'close_return'][4]
        # close_return_3 = news_df.loc[i, 'close_return'][5]
        # close_return_4 = news_df.loc[i, 'close_return'][6]

        for j, word in enumerate(dict_count_list):
            word_occur_matrix[i, j] = dict_count_list[j] / num_word

    # Build word_occur_ret_df
    word_occur_df = pd.DataFrame(word_occur_matrix, columns=DICTIONARY)
    word_occur_return_df = pd.concat([word_occur_df, return_df], axis=1)
    word_occur_return_df['Permno'] = permno_list
    word_occur_return_df.set_index('Permno', inplace=True)

    return word_occur_return_df


if __name__ == '__main__':
    pool = Pool(4)
    pool.map(build_word_occur_return, NEWS_PATH_LIST)
