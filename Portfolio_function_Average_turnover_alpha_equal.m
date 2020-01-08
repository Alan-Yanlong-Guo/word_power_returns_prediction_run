%% Local Beginning
function [] = Portfolio_function_Average_turnover_alpha_equal(day_i,alpha)

tic
% warning('off','all')
% day_ind = 0;

Trading_Signal_Collect1 = [];

for year = 2000:2016
    for month = 1:12
        file = strcat('/project2/dachxiu/mye/Text/Score_MA/DJN_MA/Data_Match/alpha',...
                      num2str(alpha),'pct/DJN_SCOREMA_',num2str(year),'_',num2str(month),'.csv');
        opts = detectImportOptions(file);
        opts = setvartype(opts,{'Score_MA'},'double');
        opts.SelectedVariableNames = {'Score_MA'};

        table = readtable(file,opts);
        TradeSig = table2array(table(:,1));
        Trading_Signal_Collect1 = [Trading_Signal_Collect1;TradeSig];
    end
end

for year = 2017
    for month = 1:7
        file = strcat('/project2/dachxiu/mye/Text/Score_MA/DJN_MA/Data_Match/alpha',...
                      num2str(alpha),'pct/DJN_SCOREMA_',num2str(year),'_',num2str(month),'.csv');
        opts = detectImportOptions(file);
        opts = setvartype(opts,{'Score_MA'},'double');
        opts.SelectedVariableNames = {'Score_MA'};

        table = readtable(file,opts);
        TradeSig = table2array(table(:,1));
        Trading_Signal_Collect1 = [Trading_Signal_Collect1;TradeSig];
    end
end

disp(size(Trading_Signal_Collect1));

load('/project2/dachxiu/Kangying/Rolling/OOS/Rolling_1530_1600_10Days/Data/TradeDate_Company_Signal.mat');
load(strcat('/project2/dachxiu/Kangying/Rolling/OOS/Rolling_1530_1600_10Days/Data/Trading_Signal_OOS_1994_2017_day',...
            num2str(day_i),'.mat'));
load(strcat('/project2/dachxiu/Kangying/Rolling/OOS/Rolling_1530_1600_10Days/Data/hf_TradeReturn/hf_TradeReturn_OOS_2000_2017_-5.mat'));

disp(size(Company_OOS_Collect));
disp(size(TradeDate_OOS_Collect));

na_index = find(isnan(hf_TradeReturn_OOS_Collect));
News_Ret_OOS_Collect(na_index,:) = [];
TradeDate_OOS_Collect(na_index,:) = [];
MarketCap_OOS_Collect(na_index,:) = [];
Last_Tradedate_Company_Collect(na_index,:) = [];
Company_OOS_Collect(na_index,:) = [];
ET_hour_OOS_Collect(na_index,:) = [];
Trading_Signal_Collect1(na_index,:) = [];

News_Ret_OOS_Ori = News_Ret_OOS_Collect;
TradeDate_OOS_Ori = TradeDate_OOS_Collect;
MarketCap_OOS_Ori = MarketCap_OOS_Collect;
Last_Tradedate_Company_OOS_Ori = Last_Tradedate_Company_Collect;
Company_OOS_Ori = Company_OOS_Collect;
ET_hour_OOS_Ori = ET_hour_OOS_Collect;
Trading_Signal_Collect = Trading_Signal_Collect1;

index = find(ET_hour_OOS_Ori>930|ET_hour_OOS_Ori<900);

Return_Trading_OOS = News_Ret_OOS_Ori(index,:);
TradeDate_OOS = TradeDate_OOS_Ori(index,:);
MarketCap_OOS = MarketCap_OOS_Ori(index,:);
Last_Tradedate_Company_OOS = Last_Tradedate_Company_OOS_Ori(index,:);
Company_OOS = Company_OOS_Collect(index,:);
Trading_Signal_Collect = Trading_Signal_Collect(index,:);
ET_hour_OOS_Ori = ET_hour_OOS_Ori(index,:);
m = size(Return_Trading_OOS,1);


%% Market Cap Trading

MarketCap= MarketCap_OOS;
MarketCap(find(isnan(MarketCap))) = 0;
MarketCap(find(MarketCap<0)) = 0;

Trading_Return = Return_Trading_OOS;
Trading_Return(find(isnan(Trading_Return))) = 0;

Trading_Date = TradeDate_OOS;
Trading_Signal = Trading_Signal_Collect;
Trading_Company = Company_OOS;

unique_trading_date = unique(Trading_Date);
Long_return = zeros(size(unique_trading_date,1),1);
Long_cum_return = zeros(size(unique_trading_date,1),1);
Short_return = zeros(size(unique_trading_date,1),1);
Short_cum_return = zeros(size(unique_trading_date,1),1);
Combined_return = zeros(size(unique_trading_date,1),1);
Combined_cum_return = zeros(size(unique_trading_date,1),1);

Long_transaction_cost = zeros(size(unique_trading_date,1),1);
Short_transaction_cost = zeros(size(unique_trading_date,1),1);

cum_long = 1;
cum_short = 1;
cum_combined = 1;

Number_stock_long = zeros(size(unique_trading_date,1),1);
Number_stock_short = zeros(size(unique_trading_date,1),1);

Scored_Number_Article_positive = zeros(size(unique_trading_date,1),1);
Scored_Number_Article_negative = zeros(size(unique_trading_date,1),1);
Scored_Number_Article_total = zeros(size(unique_trading_date,1),1);

company_pool = cell(size(unique_trading_date,1),1);
trade_company_long = cell(size(unique_trading_date,1),1);
trade_company_short = cell(size(unique_trading_date,1),1);

Stock_number = 50;

turnover_long_daily = zeros(size(unique_trading_date,1),1);
turnover_short_daily = zeros(size(unique_trading_date,1),1);

date_company_pos_pre = [];
date_weight_pos_pre = [];
date_ret_pos_pre = [];

date_company_neg_pre = [];
date_weight_neg_pre = [];
date_ret_neg_pre = [];

pos_mid_signal = zeros(size(unique_trading_date,1),1);
neg_mid_signal = zeros(size(unique_trading_date,1),1);


for i_day = 1:size(unique_trading_date,1)
    disp(i_day);
    date = unique_trading_date(i_day,:);
    date_index = find(Trading_Date == date);
    Number_article(i_day, 1) = length(date_index);

    date_return = Trading_Return(date_index,:);
    date_signal = Trading_Signal(date_index,:);
    date_marketcap = MarketCap(date_index,:);
    date_company = Trading_Company(date_index,:);

    [~,date_company_index,~] = unique(date_company);
    date_return = date_return(date_company_index,:);
    date_signal = date_signal(date_company_index,:);
    date_marketcap = date_marketcap(date_company_index,:);
    date_company = date_company(date_company_index,:);

    article_pos = find(date_signal > 0.5);
    date_signal_pos = date_signal(article_pos,:);
    date_return_pos = date_return(article_pos,:);
    date_marketcap_pos = date_marketcap(article_pos,:);
    date_company_pos = date_company(article_pos,:);

    article_neg = find(date_signal < 0.5);
    date_signal_neg = date_signal(article_neg,:);
    date_return_neg = date_return(article_neg,:);
    date_marketcap_neg = date_marketcap(article_neg,:);
    date_company_neg = date_company(article_neg,:);

    Scored_Number_Article_total(i_day, 1) = length(date_signal);
    Scored_Number_Article_positive(i_day, 1) = length(article_pos);
    Scored_Number_Article_negative(i_day, 1) = length(article_neg);


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % This section for long
    if length(article_pos)<Stock_number

        date_long = mean(date_return_pos);
        long_number = length(date_return_pos);
        date_weight_pos = ones(long_number,1)/long_number;% date_marketcap_pos./sum(date_marketcap_pos);

        pos_mid_signal(i_day, 1) = median(date_signal_pos);

    else
        [max_val max_ind] = sort(date_signal_pos,'descend');
        top_article_index = max_ind(1:Stock_number);
        long_marketcap = date_marketcap_pos(top_article_index);
        long_return = date_return_pos(top_article_index);
        % date_long = long_marketcap*long_return/sum(long_marketcap);
        date_long = mean(long_return);
        long_number = Stock_number;

        date_weight_pos =ones(long_number,1)/long_number; % long_marketcap./sum(long_marketcap);
        date_return_pos = long_return;
        date_company_pos = date_company_pos(top_article_index);
        pos_mid_signal(i_day, 1) = median(date_signal_pos(top_article_index));

    end


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% turnover calculation %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if i_day ==1
        turnover_long_daily(i_day, 1) = 0.5;
        transaction_cost_pos = 0.001;
    else

        twoday_ticker = unique([date_company_pos;  date_company_pos_pre]);
        [~,inside_company_index,inside_company_index2] = intersect(date_company_pos, twoday_ticker);
        [~,inside_company_index_pre,inside_company_index_pre2] = intersect(date_company_pos_pre, twoday_ticker);
        turnover_weight_pos = zeros(length(twoday_ticker),1);
        turnover_weight_pos(inside_company_index2,1) = date_weight_pos(inside_company_index,1);

        turnover_weight_pos_lag = zeros(length(twoday_ticker),1);
        turnover_weight_pos_lag(inside_company_index_pre2,1) = date_weight_pos_pre(inside_company_index_pre,1);

        turnover_ret_pos = zeros(length(twoday_ticker),1);
        turnover_ret_pos(inside_company_index_pre2,1) = date_ret_pos_pre(inside_company_index_pre,1);

        transaction_cost_pos = sum(abs(turnover_weight_pos-turnover_weight_pos_lag.*(1+turnover_ret_pos)))*0.001;
        turnover_pos = 0.5*sum(abs(turnover_weight_pos-turnover_weight_pos_lag));
        turnover_long_daily(i_day, 1) = turnover_pos;
    end

    date_company_pos_pre = date_company_pos;
    date_weight_pos_pre = date_weight_pos;
    date_ret_pos_pre = date_return_pos;


    if isnan(date_long)
        date_long = 0;
    end

    if isempty(date_long)
        date_long = 0;
    end

    Long_return(i_day, 1) = date_long;
    Long_transaction_cost(i_day, 1) = transaction_cost_pos;

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    if length(article_neg)<Stock_number
        % date_short = date_marketcap_neg'*date_return_neg/sum(date_marketcap_neg);
        date_short = mean(date_return_neg);
        short_number = length(date_return_neg);

        % date_weight_neg = date_marketcap_neg./sum(date_marketcap_neg);
        date_weight_neg = ones(short_number,1)/short_number;
        date_return_neg = date_return_neg;

        neg_mid_signal(i_day, 1) = median(date_signal_neg);

    else
        [min_val min_ind] = sort(date_signal_neg,'ascend');
        bottom_article_index = min_ind(1:Stock_number);
        short_marketcap = date_marketcap_neg(bottom_article_index);
        short_return = date_return_neg(bottom_article_index);
        % date_short = short_marketcap'*short_return/sum(short_marketcap);
        date_short = mean(short_return);
        short_number = Stock_number;

        % date_weight_neg = short_marketcap./sum(short_marketcap);
        date_weight_neg = ones(short_number,1)/short_number;
        date_return_neg = short_return;
        date_company_neg = date_company_neg(bottom_article_index);

        neg_mid_signal(i_day, 1) = median(date_signal_neg(bottom_article_index));

    end

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% turnover calculation %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % This section for short
    if i_day ==1
        turnover_short_daily(i_day, 1) = 0.5;
        transaction_cost_neg = 0.001;
    else

        twoday_ticker = unique([date_company_neg;  date_company_neg_pre]);
        [~,inside_company_index,inside_company_index2] = intersect(date_company_neg, twoday_ticker);
        [~,inside_company_index_pre,inside_company_index_pre2] = intersect(date_company_neg_pre, twoday_ticker);
        turnover_weight_neg = zeros(length(twoday_ticker),1);
        turnover_weight_neg(inside_company_index2,1) = date_weight_neg(inside_company_index,1);

        turnover_weight_neg_lag = zeros(length(twoday_ticker),1);
        turnover_weight_neg_lag(inside_company_index_pre2,1) = date_weight_neg_pre(inside_company_index_pre,1);

        turnover_ret_neg = zeros(length(twoday_ticker),1);
        turnover_ret_neg(inside_company_index_pre2,1) = date_ret_neg_pre(inside_company_index_pre,1);

        transaction_cost_neg = sum(abs(turnover_weight_neg-turnover_weight_neg_lag.*(1+turnover_ret_neg)))*0.001;
        turnover_neg = 0.5*sum(abs(turnover_weight_neg-turnover_weight_neg_lag));
        turnover_short_daily(i_day, 1) = turnover_neg;
    end

    date_company_neg_pre = date_company_neg;
    date_weight_neg_pre = date_weight_neg;
    date_ret_neg_pre = date_return_neg;


    if isnan(date_short)
        date_short = 0;
    end

    if isempty(date_short)
        date_short = 0;
    end

    Short_return(i_day, 1) = date_short;
    Short_transaction_cost(i_day, 1) = transaction_cost_neg;

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    Number_stock_long(i_day, 1) = long_number;
    Number_stock_short(i_day, 1) = short_number;

    Combined_return(i_day, 1) = date_long-1*date_short;

end


SR_long = mean(Long_return)/std(Long_return)*sqrt(252);
SR_short = mean(Short_return)/std(Short_return)*sqrt(252);
Combine_return = Combined_return; %0.5*Long_return + 0.5*Short_return;
SR_combine = mean(Combine_return)/std(Combine_return)*sqrt(252);

% Long_cum_return = cumsum(Long_return);
% Short_cum_return = cumsum(Short_return);
% Combined_cum_return = cumsum(Combine_return);

mkdir(strcat('/project2/dachxiu/Kangying/Rolling/OOS/Rolling_1530_1600_10Days/Portfolio_O2O/Portfolio_Alpha_EqualWeight/Portfolio_Alpha',num2str(alpha)));

save(strcat('/project2/dachxiu/Kangying/Rolling/OOS/Rolling_1530_1600_10Days/Portfolio_O2O/Portfolio_Alpha_EqualWeight/Portfolio_Alpha',num2str(alpha),'/Port_1979_2017_Fix100_day',num2str(day_i),'.mat'), ...
    'Long_return', 'Short_return','Combine_return',...
     'unique_trading_date','Number_stock_long','Number_stock_short',...
     'Scored_Number_Article_total','Scored_Number_Article_positive',...
     'Scored_Number_Article_negative','turnover_long_daily','turnover_short_daily',...
     'Long_transaction_cost','Short_transaction_cost',...
     'pos_mid_signal','neg_mid_signal','-v7.3');


disp('Finished');
toc
