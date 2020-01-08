import pandas as pd
import numpy as np
import datetime
import os
import sklearn.preprocessing as pro
from tools.utils import combine_word_occur_return, combine_datetime, combine_permno
from global_setting import DICT_SIZE, DELAY
from global_setting import SP500_TABLE
from global_setting import PORTFOLIO_LONG_SIZE, PORTFOLIO_SHORT_SIZE
from global_setting import LOOK_UP_FOLDER, RETURN_FOLDER, ANALYSIS_FOLDER


# 0 1 2 | 3 4 5 6 7
# 0-1 1-2 2-3 | 3-4 4-5 5-6 6-7

# TODO: Change date of holiday to the next working day
# TODO: Combine news from adjacent days


def predict_year_return(params, year_test_i, year_test_f):
    # Combine word_occur_return_df
    word_occur_return_df_test = combine_word_occur_return(year_test_i, year_test_f)
    word_occur_return_df_test = combine_datetime(word_occur_return_df_test, year_test_i, year_test_f)
    print(f'{datetime.datetime.now()} Finished Combining word_occur_return_df!')

    # Find business date and unique date + get sp500 and ff_df
    unique_est_date_list = sorted(word_occur_return_df_test['est_date'].unique())
    business_date_list_full = np.array(SP500_TABLE.index)
    sp500_list_full = np.array(SP500_TABLE['Adj Close'])
    business_date_list = []
    sp_500_list = []
    for index, business_date in enumerate(business_date_list_full):
        if int(business_date.split('-')[0]) in np.arange(year_test_i, year_test_f + 1):
            business_date_list.append(business_date_list_full[index])
            sp_500_list.append((sp500_list_full[index + 1] - sp500_list_full[index]) / sp500_list_full[index])
    ff_df = pd.read_csv(os.path.join(LOOK_UP_FOLDER, 'FF.csv'), index_col=0).loc[business_date_list]

    # Initialize return and turnover list
    long_equal_return_list = []
    short_equal_return_list = []
    long_value_return_list = []
    short_value_return_list = []
    long_turnover_list = []
    short_turnover_list = []

    # Initialize portfolio
    long_permno_array_ = np.array([])
    short_permno_array_ = np.array([])
    long_equal_return_day_ = np.array([])
    short_equal_return_day_ = np.array([])
    long_cap_day_ = np.array([])
    short_cap_day_ = np.array([])

    for id, business_date in enumerate(business_date_list):
        if business_date in unique_est_date_list:
            word_occur_return_df_day = word_occur_return_df_test.loc[word_occur_return_df_test['est_date'] == business_date]
            word_occur_return_df_day = combine_permno(word_occur_return_df_day)
            long_equal_return_day, short_equal_return_day, long_cap_day, short_cap_day, \
            long_permno_array, short_permno_array = predict_day_return(params, word_occur_return_df_day, 1)

            # Daily return
            if len(long_equal_return_day) == 0:
                long_equal_return_list.append(0)
                long_value_return_list.append(0)
            else:
                long_equal_return = np.mean(long_equal_return_day)
                long_equal_return_list.append(long_equal_return)
                long_value_weight = len(long_cap_day) * long_cap_day / np.sum(long_cap_day)
                long_value_return = np.mean(np.multiply(long_equal_return_day, long_value_weight))
                long_value_return_list.append(long_value_return)

            if len(short_equal_return_day) == 0:
                short_equal_return_list.append(0)
                short_value_return_list.append(0)
            else:
                short_equal_return = np.mean(short_equal_return_day)
                short_equal_return_list.append(short_equal_return)
                short_value_weight = short_cap_day / np.sum(short_cap_day)
                short_value_return = np.mean(np.multiply(short_equal_return_day, short_value_weight))
                short_value_return_list.append(short_value_return)

            # Daily turnover: permno_array denotes t+1 while permno_array_ denotes t
            # len(long_permno_array_) = 0 correspond to no transaction on day t
            if len(long_permno_array_) != 0:
                long_turnover = 0
                for long_permno_ in long_permno_array_:
                    arg_ = np.argwhere(long_permno_array_ == long_permno_)
                    long_value_weight_ = long_cap_day_ / np.sum(long_cap_day_)
                    if long_permno_ in long_permno_array:
                        print('match')
                        arg = np.argwhere(long_permno_array == long_permno_)
                        long_value_weight = long_cap_day / np.sum(long_cap_day)
                        long_turnover += np.abs(np.float(long_value_weight[arg] - long_value_weight_[arg_] * (1 + long_equal_return_day_[arg_])))
                    else:
                        long_turnover += np.abs(np.float(0 - long_value_weight_[arg_] * (1 + long_equal_return_day_[arg_])))
                print(long_turnover)
                long_turnover_list.append(long_turnover)
            else:
                long_turnover_list.append(1)

            # len(short_permno_array_) = 0 correspond to no transaction on day t
            if len(short_permno_array_) != 0:
                short_turnover = 0
                for short_permno_ in short_permno_array_:
                    arg_ = np.argwhere(short_permno_array_ == short_permno_)
                    short_value_weight_ = short_cap_day_ / np.sum(short_cap_day_)
                    if short_permno_ in short_equal_return_day:
                        print('match')
                        arg = np.argwhere(short_equal_return_day == short_permno_)
                        short_value_weight = short_cap_day / np.sum(short_cap_day)
                        short_turnover += np.abs(np.float(short_value_weight[arg] - short_value_weight_[arg_] * (1 - short_equal_return_day_[arg_])))
                    else:
                        short_turnover += np.abs(np.float(0 - short_value_weight_[arg_] * (1 - short_equal_return_day_[arg_])))
                print(short_turnover)
                short_turnover_list.append(short_turnover)
            else:
                short_turnover_list.append(1)

            # Save the portfolio return for turnover calculation of the next day
            long_permno_array_ = long_permno_array
            short_permno_array_ = short_permno_array
            long_equal_return_day_ = long_equal_return_day
            short_equal_return_day_ = short_equal_return_day
            long_cap_day_ = long_cap_day
            short_cap_day_ = short_cap_day

        # else correspond to no transaction on day t+1
        else:
            long_equal_return_list.append(0)
            long_value_return_list.append(0)
            short_equal_return_list.append(0)
            short_value_return_list.append(0)
            long_value_weight_ = long_cap_day_ / np.sum(long_cap_day_)
            short_value_weight_ = short_cap_day_ / np.sum(short_cap_day_)
            long_turnover = np.sum(np.multiply(long_value_weight_, 1 + long_equal_return_day_))
            short_turnover = np.sum(np.multiply(short_value_weight_, 1 - short_equal_return_day_))
            long_turnover_list.append(long_turnover)
            short_turnover_list.append(short_turnover)
            long_permno_array_ = np.array([])
            short_permno_array_ = np.array([])
            long_equal_return_day_ = np.array([])
            short_equal_return_day_ = np.array([])
            long_cap_day_ = np.array([])
            short_cap_day_ = np.array([])

    long_turnover_list.append(1)
    short_turnover_list.append(1)
    long_turnover_list = long_turnover_list[1:]
    short_turnover_list = short_turnover_list[1:]

    return_df = pd.DataFrame({'long_equal_return': long_equal_return_list,
                              'short_equal_return': short_equal_return_list,
                              'long_value_return': long_value_return_list,
                              'short_value_return': short_value_return_list,
                              'sp500_return': sp_500_list,
                              'long_turnover': long_turnover_list,
                              'short_turnover': short_turnover_list}, index=business_date_list)
    return_df = pd.concat([return_df, ff_df], axis=1)
    pd.to_pickle(return_df, os.path.join(RETURN_FOLDER, str(year_test_i) + '-' + str(year_test_f) + '.pkl'))


def return_with_delay(params, year_test_i, year_test_f):
    word_occur_return_df_test_ = combine_word_occur_return(year_test_i, year_test_f)
    word_occur_return_df_test = combine_datetime(word_occur_return_df_test_, year_test_i, year_test_f)
    print(f'{datetime.datetime.now()} Finished Combining word_occur_return_df!')
    unique_est_date_list = sorted(word_occur_return_df_test['est_date'].unique())
    returns_delay = []
    for unique_est_date in unique_est_date_list:
        word_occur_return_df_day = combine_permno(word_occur_return_df_test
                                                  [word_occur_return_df_test.est_date == unique_est_date])
        returns = []
        for day in range(-1, 2):
            long_equal_return_array, short_equal_return_array, _, _, _, _ = predict_day_return(params,
                                                                                         word_occur_return_df_day,
                                                                                         day=day)
            long_equal_return = np.mean(long_equal_return_array)
            short_equal_return = np.mean(short_equal_return_array)
            returns.append(1 + long_equal_return - short_equal_return)
        returns_delay.append(returns)
    return_delay_df = pd.DataFrame(np.array(returns_delay), columns=['day' + str(i) for i in range(-1, 2)],
                                   index=unique_est_date_list)
    return_delay_df.to_pickle(
        os.path.join(ANALYSIS_FOLDER, str(year_test_i) + '-' + str(year_test_f) + '_return_with_delay.pkl'))
    print(f'{datetime.datetime.now()} Finished return_with_delay', year_test_i)


def novelty_and_heterogeneity_analysis(params, year_test_i, year_test_f, run=(True, True, True)):
    word_occur_return_df_test_ = combine_word_occur_return(year_test_i, year_test_f)
    word_occur_return_df_test = combine_datetime(word_occur_return_df_test_, year_test_i, year_test_f)
    print(f'{datetime.datetime.now()} Finished Combining word_occur_return_df!')
    unique_est_date_list = sorted(word_occur_return_df_test.est_date.unique())
    # create 5 lists of lists (of length 3) of empty list of length DELAY to represent long, short, and returns of test
    total, stale, fresh, big, small = [[[[] for i in range(DELAY)] for j in range(3)] for k in range(5)]
    for n, unique_est_date in enumerate(unique_est_date_list):
        word_return_df_today = word_occur_return_df_test[word_occur_return_df_test.est_date == unique_est_date]
        word_return_today = combine_permno(word_return_df_today)

        if run[0] == True:
            # assimilation_analysis
            total_day = assimilation_speed(params, word_return_today)
            total = [[total[m][k] + total_day[m][k] for k in range(DELAY)] for m in range(3)]

        if run[1] == True:
            # novelty_analysis
            five_days = unique_est_date_list[min(0, n - 5):n]
            word_return_five_days = word_occur_return_df_test[word_occur_return_df_test.est_date.isin(five_days)]
            novelty_series = word_return_df_today.groupby('Permno').apply(calculate_novelty, word_return_five_days)
            stale_company_list = novelty_series[novelty_series <= 0.99].index
            fresh_company_list = novelty_series[novelty_series > 0.99].index
            stale_news_return_df_day = word_return_today[word_return_today.index.isin(stale_company_list)]
            fresh_news_return_df_day = word_return_today[word_return_today.index.isin(fresh_company_list)]
            stale_day = assimilation_speed(params, stale_news_return_df_day)
            fresh_day = assimilation_speed(params, fresh_news_return_df_day)
            # append today's long, short, and returns with various delays to the test list
            stale = [[stale[m][k] + stale_day[m][k] for k in range(DELAY)] for m in range(3)]
            fresh = [[fresh[m][k] + fresh_day[m][k] for k in range(DELAY)] for m in range(3)]

        if run[2] == True:
            # heterogeneity analysis
            capital_median = word_return_today.open_cap.apply(lambda p: p[3]).median()
            big_return_df_day = word_return_today[word_return_today.open_cap.apply(lambda p: p[3]) >= capital_median]
            small_return_df_day = word_return_today[word_return_today.open_cap.apply(lambda p: p[3]) < capital_median]
            big_day = assimilation_speed(params, big_return_df_day)
            small_day = assimilation_speed(params, small_return_df_day)
            big = [[big[m][k] + big_day[m][k] for k in range(DELAY)] for m in range(3)]
            small = [[small[m][k] + small_day[m][k] for k in range(DELAY)] for m in range(3)]

    # calculate mean and confidence interval of long, short and returns with different delays

    if run[0] == True:
        total_array = np.array(total).reshape(3 * DELAY, -1)
        assimilation_arrays_df = pd.DataFrame(total_array.T,
                                              columns=[char + str(i + 1) for char in ['long', 'short', 'returns']
                                                       for i in range(DELAY)], index=unique_est_date_list)
        assimilation_arrays_df.to_pickle(
            os.path.join(ANALYSIS_FOLDER, str(year_test_i) + '-' + str(year_test_f) + '_assimilation_analysis.pkl'))
        print(f'{datetime.datetime.now()} Finished assimilation analysis', year_test_i)

    if run[1] == True:
        stale_array = np.array(stale).reshape(3 * DELAY, -1)
        fresh_array = np.array(fresh).reshape(3 * DELAY, -1)
        novelty_arrays_df = pd.DataFrame(np.concatenate((stale_array, fresh_array)).T,
                                         columns=[t + char + str(i + 1) for t in ['stale_', 'fresh_'] for char
                                                  in ['long', 'short', 'returns'] for i in range(DELAY)],
                                         index=unique_est_date_list)
        novelty_arrays_df.to_pickle(
            os.path.join(ANALYSIS_FOLDER, str(year_test_i) + '-' + str(year_test_f) + '_novelty_analysis.pkl'))
        print(f'{datetime.datetime.now()} Finished novelty analysis', year_test_i)

    if run[2] == True:
        big_array = np.array(big).reshape(3 * DELAY, -1)
        small_array = np.array(small).reshape(3 * DELAY, -1)
        heterogeneity_arrays_df = pd.DataFrame(np.concatenate((big_array, small_array)).T,
                                               columns=[t + char + str(i + 1) for t in ['big_', 'small_'] for char
                                                        in ['long', 'short', 'returns'] for i in range(DELAY)],
                                               index=unique_est_date_list)
        heterogeneity_arrays_df.to_pickle(
            os.path.join(ANALYSIS_FOLDER, str(year_test_i) + '-' + str(year_test_f) + '_heterogeneity_analysis.pkl'))
        print(f'{datetime.datetime.now()} Finished heterogeneity analysis', year_test_i)


# ------------------------------ Helper Function ------------------------------
def predict_day_return(params, word_occur_return_df_day, day=1):
    """
    :param params:
    :param word_occur_return_df_day:
    :param day:
    :return long_equal_return_day: array of long return per day (len = long portfolio size)
    :return short_equal_return_day: array of long return per day (len = short portfolio size)
    :return long_cap_day: array of long capitalization per day (len = long portfolio size)
    :return short_cap_day: array of short capitalization per day (len = long portfolio size)
    :return long_permno_array: array of permno capitalization per day (len = long portfolio size)
    """
    next_open_return_array = word_occur_return_df_day.open_price_return.apply(lambda p: p[2 + day]).values
    next_open_cap_array = word_occur_return_df_day.open_cap.apply(lambda p: p[2 + day]).values
    permno_array = np.array(word_occur_return_df_day.index)

    word_occur_matrix_day = word_occur_return_df_day.iloc[:, :DICT_SIZE].values
    num_news_day, _ = np.shape(word_occur_matrix_day)
    M = np.hstack([word_occur_matrix_day, np.ones(num_news_day).reshape(num_news_day, 1)])
    r = np.matmul(M, params)

    # Get long and short index
    r_sorted = np.sort(r)
    r_arg_sorted = np.argsort(r)
    r_pos_arg_sorted = r_arg_sorted[r_sorted > 0]
    if len(r_pos_arg_sorted) > PORTFOLIO_LONG_SIZE:
        long_index = r_pos_arg_sorted[-PORTFOLIO_LONG_SIZE:]
    else:
        long_index = r_pos_arg_sorted

    r_neg_arg_sorted = r_arg_sorted[r_sorted < 0]
    if len(r_neg_arg_sorted) > PORTFOLIO_SHORT_SIZE:
        short_index = r_neg_arg_sorted[:PORTFOLIO_SHORT_SIZE]
    else:
        short_index = r_neg_arg_sorted

    # Get long and short return
    long_equal_return_day = next_open_return_array[long_index]
    short_equal_return_day = next_open_return_array[short_index]
    long_cap_day = next_open_cap_array[long_index]
    short_cap_day = next_open_cap_array[short_index]
    long_permno_day = permno_array[long_index]
    short_permno_day = permno_array[short_index]

    return long_equal_return_day, short_equal_return_day, long_cap_day, short_cap_day, long_permno_day, short_permno_day


def assimilation_speed(params, return_df_day):
    day_returns, day_long, day_short = [[[] for i in range(DELAY)] for j in range(3)]
    for day in range(1, DELAY + 1):
        long_equal_return_array, short_equal_return_array, _, _, _, _ = predict_day_return(params, return_df_day, day)
        if long_equal_return_array.shape[0] != 0:
            long_equal_return = np.mean(long_equal_return_array)
        else:
            long_equal_return = 0
        if short_equal_return_array.shape[0] != 0:
            short_equal_return = np.mean(short_equal_return_array)
        else:
            short_equal_return = 0
        try:
            sp500_return = return_df_day.open_sp500_return.iloc[0][2 + day]
        except:
            sp500_return = 0
        day_short[day - 1].append(short_equal_return)
        day_long[day - 1].append(long_equal_return - sp500_return)
        day_returns[day - 1].append(long_equal_return - short_equal_return - sp500_return)
    return [day_long, day_short, day_returns]


def calculate_novelty(company_word_return_today, word_return_five_days):
    word_today_matrix = company_word_return_today.iloc[:, :DICT_SIZE]
    word_before_matrix = word_return_five_days[word_return_five_days.index ==
                                               company_word_return_today.index[0]].iloc[:, :DICT_SIZE].values
    if word_before_matrix.shape[0] != 0:
        pro.normalize(word_today_matrix, norm='l1', copy=False)
        pro.normalize(word_before_matrix, norm='l1', copy=False)
        novelty = 1 - np.max(np.dot(word_before_matrix, word_today_matrix.T))
        return novelty
    else:
        return 1
