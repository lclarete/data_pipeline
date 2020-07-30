"""
Uncover trends using time series.

"""


# decompose time series
from statsmodels.tsa.seasonal import seasonal_decompose
n_videos_series = seasonal_decompose(df.n_videos, 
                                     freq=12, 
                                     model='additive')


from statsmodels.tsa.seasonal import seasonal_decompose


# Plot the decomposed time series of `rotationRate.x` also with a frequency of 60.
rotationRate_sd = seasonal_decompose(sensor['rotationRate.x'], 
                                     freq=60,
                                    model='additive')



def time_series(serie):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(15,8))
    serie.observed.plot(ax=ax1)
    serie.trend.plot(ax=ax2)
    serie.resid.plot(ax=ax3)
    serie.seasonal.plot(ax=ax4)
    sns.despine()

# autocorrection
from pandas.plotting import lag_plot
lag_plot(df.n_videos)
sns.despine()

# testing stationarity
from statsmodels.tsa.stattools import adfuller

def adf_test(series,title=''):
    """
    Pass in a time series and an optional title, returns an ADF report
    """
    print(f'Augmented Dickey-Fuller Test: {title}')
    result = adfuller(series.dropna(),autolag='AIC') # .dropna() handles differenced data
    
    labels = ['ADF test statistic','p-value','# lags used','# observations']
    out = pd.Series(result[0:4],index=labels)

    for key,val in result[4].items():
        out[f'critical value ({key})']=val
        
    print(out.to_string())          # .to_string() removes the line "dtype: float64"
    
    if result[1] <= 0.05:
        print("Strong evidence against the null hypothesis")
        print("Reject the null hypothesis")
        print("Data has no unit root and is stationary")
    else:
        print("Weak evidence against the null hypothesis")
        print("Fail to reject the null hypothesis")
        print("Data has a unit root and is non-stationary")

# AR Model
# Assumptions:
# 1. Stationarity
# 2. Invertibility

from statsmodels.tsa.arima_model import ARMA
# split data into train and test
train = df.n_videos.iloc[:-10, ]
test = df.n_videos.iloc[-10:, ]

print(f'train data has {train.shape[0]} cases and test data has {test.shape[0]} cases.')

# instantiate the model
model_ar = ARMA(train, order=(2,1))

# fit the model
model_ar_fit = model_ar.fit(disp=False)

# predict
predict = model_ar_fit.predict(len(df)-10,
                              len(df)-1)


# evaluate the model
from statsmodels.tools.eval_measures import rmse
rmse(predict, test)

pd.DataFrame({'observed': test, 
              'predicted':round(predict), 
              'diff':round(test-predict)})

