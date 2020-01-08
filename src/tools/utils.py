import pandas as pd 
import os
import pickle
from global_setting import TEMP_FOLDER
import numpy as np
import scipy.stats as st
from global_setting import SP500_TABLE, RETURN_FOLDER, DICT_SIZE
import datetime
import glob


def combine_word_occur_return(year_i, year_f, oc='open'):
    word_occur_return_df_list = []
    for year in range(year_i, year_f + 1):
        max_month = 7 if year == 2017 else 12
        for month in range(1, max_month+1):
            temp_path = os.path.join(TEMP_FOLDER, str(year) + '_' + str(month).zfill(2) + '.pkl')
            with open(temp_path, 'rb') as handle:
                content = pickle.load(handle)
                word_occur_return_df_list.append(content)
    word_occur_return_df_combined = pd.concat(word_occur_return_df_list, axis=0)

    if oc == 'open':
        word_occur_return_df_combined.dropna(inplace=True,
                                             subset=['worthy', 'open_price', 'open_cap', 'open_sp500',
                                                     'open_price_return', 'open_sp500_return'])
    else:
        word_occur_return_df_combined.dropna(inplace=True,
                                             subset=['worthy', 'close_price', 'close_cap', 'close_sp500',
                                                     'close_price_return', 'close_sp500_return'])
    return word_occur_return_df_combined


def combine_datetime(word_occur_return_df_combined, year_i, year_f):
    business_date_list_full = list(SP500_TABLE.index)
    business_date_list = [business_day for business_day in business_date_list_full
                          if year_i <= int(business_day.split('-')[0]) <= year_f + 1]
    est_date_list = list(word_occur_return_df_combined['est_date'])
    est_time_list = list(word_occur_return_df_combined['est_time'])
    est_date_list_reassigned = []
    est_time_list_reassigned = []
    for i in range(len(est_date_list)):
        est_date = est_date_list[i]
        est_time = est_time_list[i]
        hour = est_time.split(':')[0]

        # If the date is a business day and hour before 9:00, keep the datetime unchanged, else find the next business
        # day and set the time to 5:00am of that day
        if (est_date in business_date_list) and (int(hour) < 9):
            est_date_list_reassigned.append(est_date)
            est_time_list_reassigned.append(est_time)
        else:
            delta_day = 1
            est_date_delta = get_date(est_date, delta_day)
            while est_date_delta not in business_date_list:
                delta_day += 1
                est_date_delta = get_date(est_date, delta_day)
            est_date_list_reassigned.append(est_date_delta)
            est_time_list_reassigned.append('05:00')

    word_occur_return_df_combined['est_date'] = est_date_list_reassigned
    word_occur_return_df_combined['est_time'] = est_time_list_reassigned

    return word_occur_return_df_combined


def combine_permno(word_occur_return_df_day):
    unique_permno_list = np.unique(word_occur_return_df_day.index)
    word_occur_return_matrix = []
    for unique_permno in unique_permno_list:
        word_occur_array = word_occur_return_df_day.loc[[unique_permno], :].iloc[:, :DICT_SIZE].values.sum(axis=0)
        return_array = word_occur_return_df_day.loc[[unique_permno], :].iloc[:, DICT_SIZE:].values[0]
        word_occur_return_array = np.append(word_occur_array, return_array)
        word_occur_return_matrix.append(word_occur_return_array)

    word_occur_return_df_day = pd.DataFrame(word_occur_return_matrix, index=unique_permno_list,
                                            columns=word_occur_return_df_day.columns)

    return word_occur_return_df_day


def combine_return():
    file_list = sorted(glob.glob(os.path.join(RETURN_FOLDER, '*.pkl')))
    content_list = []
    for file in file_list:
        content = pd.read_pickle(file)
        content_list.append(content)
    content_full = pd.concat(content_list, axis=0)
    content_full.to_pickle('/Users/mingyu/Desktop/return_df_combined.pkl')


def get_date(old_date, delta_day):
    """
    :param str old_date: the old date in 'YYYYMMDD' format
    :param int delta_day: the difference between old day and new day
    :return str new_day: the new date in 'YYYYMMDD' format
    """
    year = int(old_date.split('-')[0].lstrip('0'))
    month = int(old_date.split('-')[1].lstrip('0'))
    day = int(old_date.split('-')[2].lstrip('0'))
    old_date = datetime.date(year, month, day)
    delta_date = datetime.timedelta(days=delta_day)
    new_date = old_date + delta_date

    new_date = str(new_date.year).rjust(4, '0') + '-' + str(new_date.month).rjust(2, '0') + '-' + str(new_date.day).rjust(2, '0')

    return new_date


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), st.sem(a)
    h = se * st.t.ppf((1 + confidence) / 2., n-1)
    return m, [m-h, m+h]


# def clean_reduced_dsf(reduced_df):
#     date_list = np.array(reduced_df['DATE'])
#     year = [int(str(date)[0:4]) for date in date_list]
#     boo = np.array(year) >= 1987
#     reduced_reduced_df = reduced_df[boo]
#     reduced_reduced_df.reset_index(inplace=True, drop=True)
#     permno_list = np.array(reduced_reduced_df['PERMNO']).astype(int).astype(str)
#     date_list = np.array(reduced_reduced_df['DATE'])
#     prc_list = np.array(reduced_reduced_df['PRC'])
#     openprc_list = np.array(reduced_reduced_df['OPENPRC'])
#     shrout_list = reduced_reduced_df['SHROUT'].astype(int).astype(str)
#     sid_list = reduced_reduced_df['HSICCD'].astype(int).astype(str)
#     reduced_reduced_df = pd.DataFrame({'PERMNO': permno_list, 'DATE': date_list, 'PRC': prc_list,
#                                        'OPENPRC': openprc_list, 'SHROUT': shrout_list, 'SID': sid_list})
#     reduced_reduced_df.to_hdf('dsf.h5', key='df', mode='w')

# def split_reduced_dsf(reduced_df):
#     year_list = [str(date)[:4] for date in np.array(reduced_df['DATE'])]
#     year_list = np.array(year_list).astype(int)
#     unique_years = list(set(year_list))
#     for year in unique_years:
#         index = (year_list == year)
#         small_dsf = reduced_df[index]
#         small_dsf.reset_index(inplace = True, drop = True)
#         small_dsf.to_hdf(f'/Users/mingyu/Desktop/small_dsf/dsf_{year}.h5', key='df', mode='w')

# def combine_reduced_dsf():
#     df = pd.DataFrame()
#     for files in glob.glob('/Volumes/Seagate_2T/word_power/dsf/*.pkl'):
#         print(files)
#         with open(files, 'rb') as handle:
#             content = pickle.load(handle)
#         df = pd.concat([df, content])
#     with open('/Volumes/Seagate_2T/word_power/dsf.pkl', 'wb') as handle:
#         pickle.dump(df, handle)

