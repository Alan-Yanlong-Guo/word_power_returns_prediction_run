# word_power_returns_prediction
Group Date: 
News that are published within the holiday are group together with 
the news of the next business day, with the date being the next business 
day and time being 5:00am, which is before the market opening (this is 
effectively the same)

Possible data loss: 
- Fetch price uses the dsf of a particular year, price fetch may 
fail at the beginning or the end of the year 
- word_occur_return_df during training is grouped on a yearly basis,  
