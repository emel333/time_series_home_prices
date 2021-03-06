# Creating a function for checking stationarity
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def stationarity_checker(ts):
    
    
    # For Rolling Statistics -- as needed
    roll_mean = ts.rolling(window=12, center=False).mean()
    roll_std = ts.rolling(window=12, center=False).std()
    
    # Dickey Full
    df_test = adfuller(ts) 
    
    # Rolling statistics -- plotting:
    fig = plt.figure(figsize=(12,6))
    original = plt.plot(ts, color='blue',label='Original')
    mean = plt.plot(roll_mean, color='green', label='Rolling Mean')
    std = plt.plot(roll_std, color='red', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    # Print Dickey Full
    print('Results of Dickey-Fuller Test: \n')
    print('---------------------------------')

    df_results = pd.Series(df_test[0:4], index=['Test Statistic', 'p-value', 
                                             '# of Lags Used', 'Number of Observations Used'])
    for key, value in df_test[4].items():
        df_results['The Critical Value (%s)'%key] = value
        
    print(df_results)
    print('---------------------------------')
    
    # Plot Time Series
    ts.plot(figsize=(10,4), color='purple');
    plt.title('Initial Plot of Time Series In Question')
    
    return None