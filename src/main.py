import datetime
import pickle
import os
import pandas as pd
import glob
import numpy as np
from tools.data_processing import load_dsf
from tools.data_processing import filter_news, filter_append_permno, append_est_date_time, append_price_cap_sp500_return
from tools.build_word_occur_return import build_word_occur_return
from model.training import linear_fit
from model.testing import predict_year_return,return_with_delay,novelty_and_heterogeneity_analysis
from evaluation.training_evaluation import word_occur_evaluation, score_evaluation, similarity_evaluation
from global_setting import TEMP_FOLDER, PARAMS_FOLDER, SCORE_FOLDER, NEWS_PATH_LIST
from global_setting import YEAR_TRAIN_LIST, YEAR_TEST_LIST
from global_setting import TRAIN_LEN, CROSS_LEN, TEST_LEN


def run_data_processing(path):
    file = str(path).split('/')[-1]
    date = file.split('.')[0].split('_')[0]
    year = date.split('-')[0]
    month = date.split('-')[1]
    dsf_df = load_dsf(year)
    print(f'{datetime.datetime.now()} Working on {path}')

    with open(str(path), 'rb') as handle:
        news_df = pickle.load(handle)

    news_df = filter_news(news_df)
    news_df = append_est_date_time(news_df)
    news_df = filter_append_permno(news_df)
    news_df = append_price_cap_sp500_return(news_df, dsf_df)
    word_occur_return_df = build_word_occur_return(news_df)
    print(f'{datetime.datetime.now()} Finish Building word_occur_return_df for {file}')

    with open(os.path.join(TEMP_FOLDER, year + '_' + month + '.pkl'), 'wb') as handle:
        pickle.dump(word_occur_return_df, handle)


def run_training(year_train_i, year_train_f):
    print(f'{datetime.datetime.now()} Training on Year {year_train_i} to Year {year_train_f}')
    linear_fit(year_train_i, year_train_f)


def run_training_evaluation():
    tone = np.array(pd.read_csv(glob.glob(os.path.join(SCORE_FOLDER, '*.csv'))[0], index_col=0)['tone'])
    word_occur_dictionary = {}
    score_dictionary = {}
    for score_file in glob.glob(os.path.join(SCORE_FOLDER, '*.csv')):
        WP_df = pd.read_csv(score_file, index_col=0)
        year_train_range = score_file.split('/')[-1].split('.')[0]
        word_occur_dictionary[year_train_range] = np.array(WP_df['word_occur'])
        score_dictionary[year_train_range] = np.array(WP_df['score'])

    word_occur_fig = word_occur_evaluation(word_occur_dictionary)
    score_fig, classification_matrix, f1_scalar = score_evaluation(score_dictionary, tone)
    similarity_fig, similarity_df = similarity_evaluation(word_occur_dictionary)

    return word_occur_fig, score_fig, classification_matrix, f1_scalar, similarity_fig, similarity_df


def run_testing(year_test_i, year_test_f):
    print(f'{datetime.datetime.now()} Testing on Year {year_test_i} to Year {year_test_f}')
    year_train_i = year_test_i - CROSS_LEN - TRAIN_LEN
    year_train_f = year_test_f - TEST_LEN - CROSS_LEN
    params = pd.read_pickle(os.path.join(PARAMS_FOLDER, str(year_train_i) + '-' + str(year_train_f) + '.pkl'))
    predict_year_return(params, year_test_i, year_test_f)


def run_analysis(year_test_i, year_test_f):
    print(f'{datetime.datetime.now()} Analysing on Year {year_test_i} to Year {year_test_f}')
    year_train_i = year_test_i - CROSS_LEN - TRAIN_LEN
    year_train_f = year_test_f - TEST_LEN - CROSS_LEN
    params = pd.read_pickle(os.path.join(PARAMS_FOLDER, str(year_train_i) + '-' + str(year_train_f) + '.pkl'))
    return_with_delay(params,year_test_i, year_test_f)
    novelty_and_heterogeneity_analysis(params,year_test_i, year_test_f)


if __name__ == '__main__':
    # Data Processing
    # news_path_list = [path for path in NEWS_PATH_LIST if
    #                   int(path.split('/')[-1].split('-')[0]) in [2016, 2017]]
    # print(news_path_list)
    # pool = Pool(8)
    # run_data_processing()
    # pool.map(run_data_processing, news_path_list)
    run_data_processing('/Volumes/Seagate_2T/word_power/news/2006-05_cleaned.pkl')
    # Training
    # pool = Pool(8)
    # pool.starmap(run_training, YEAR_TRAIN_LIST)
    # Testing
    # pool = Pool(6)
    # pool.starmap(run_testing, YEAR_TEST_LIST)
    # run_testing(2004, 2004)
    # run_analysis(2004,2004)
    # run_analysis(2005,2005)
    # run_testing(2004, 2004)
