import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from global_setting import RETURN_FOLDER


def plot_cumulative_return():
    import glob
    import pandas as pd
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    import numpy as np
    import os
    return_file_list = []
    for file in glob.glob(os.path.join('/Volumes/Seagate_2T/word_power/return', '*.pkl')):
        return_file_list.append(file)
    return_file_list = sorted(return_file_list)

    year_list = np.arange(2004, 2018)
    year_return_df_list = []
    year_num_day_list = []
    for file in return_file_list:
        year_return_df = pd.read_pickle(file)
        year_num_day = np.shape(year_return_df)[0]
        year_return_df_list.append(year_return_df)
        year_num_day_list.append(year_num_day)
    return_df_combined = pd.concat(year_return_df_list, axis=0)
    cumulative_num_day_list = np.cumsum(year_num_day_list)
    cumulative_num_day_list = np.append(1, cumulative_num_day_list)

    # Calculate cumulative return
    long_equal_return = np.array(return_df_combined['long_equal_return']) + 1
    cumulative_long_equal_return = np.log(np.cumprod(long_equal_return))
    short_equal_return = -np.array(return_df_combined['short_equal_return']) + 1
    cumulative_short_equal_return = np.log(np.cumprod(short_equal_return))
    equal_return = long_equal_return + short_equal_return - 1
    cumulative_equal_return = np.log(np.cumprod(equal_return))

    long_value_return = np.array(return_df_combined['long_value_return']) + 1
    cumulative_long_value_return = np.log(np.cumprod(long_value_return))
    short_value_return = -np.array(return_df_combined['short_value_return']) + 1
    cumulative_short_value_return = np.log(np.cumprod(short_value_return))
    value_return = long_value_return + short_value_return - 1
    cumulative_value_return = np.log(np.cumprod(value_return))

    sp500_return = np.array(return_df_combined['sp500_return']) + 1
    cumulative_sp500_return = np.log(np.cumprod(sp500_return))

    # Plot cumulative return
    plt.figure(1, figsize=(14, 7))
    plt.xlim(cumulative_num_day_list[0], cumulative_num_day_list[-1])
    plt.xticks(cumulative_num_day_list[0::2], year_list[0::2])
    plt.grid('on')
    plt.plot(cumulative_equal_return, 'k-')
    plt.plot(cumulative_long_equal_return, 'b-')
    plt.plot(-cumulative_short_equal_return, 'r-')
    plt.plot(cumulative_value_return, 'k--')
    plt.plot(cumulative_long_value_return, 'b--')
    plt.plot(-cumulative_short_value_return, 'r--')
    plt.plot(cumulative_sp500_return, 'y-')
    plt.legend(['L-S EW', 'L EW', 'S EW', 'L-S VW', 'L VW', 'S VW', 'SP500'])
    plt.show()

    return cumulative_equal_return, cumulative_long_equal_return, cumulative_short_equal_return, \
           cumulative_value_return, cumulative_long_value_return, cumulative_short_value_return
