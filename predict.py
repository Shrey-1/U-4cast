import pandas as pd
import warnings
import plotly.express as plt
warnings.filterwarnings('ignore')
df=pd.read_csv('D:\\Projects\\U-4cast\\data\\data.csv')

df=df.dropna()
pre_df = df[['date','time','min_temp', 'avg_temp']]
predict_df = pre_df.groupby('date')['avg_temp'].mean().to_frame().reset_index()
predict_df['avg_temp'] = round(predict_df['avg_temp'],2)
df = predict_df
df=df.set_index('date')


from statsmodels.tsa.stattools import adfuller

def adf_test(dataset):
  dftest = adfuller(dataset, autolag = 'AIC')
  print("1. ADF : ",dftest[0])
  print("2. P-Value : ", dftest[1])
  print("3. Num Of Lags : ", dftest[2])
  print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
  print("5. Critical Values :")
  for key, val in dftest[4].items():
      print("\t",key, ": ", val)

adf_test(df['avg_temp'])


from pmdarima import auto_arima
# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")

stepwise_fit = auto_arima(df['avg_temp'], suppress_warnings=True)           
stepwise_fit.summary()


from statsmodels.tsa.arima_model import ARIMA


# In[49]:


print(df.shape)
train=df.iloc[:-30]
test=df.iloc[-30:]
print(train.shape,test.shape)
print(test.iloc[0],test.iloc[-1])


# In[50]:


from statsmodels.tsa.arima.model import ARIMA
model=ARIMA(train['avg_temp'],order=(1,0,5))
model=model.fit()
model.summary()


# In[51]:


start=len(train)
end=len(train)+len(test)-1
#if the predicted values dont have date values as index, you will have to uncomment the following two commented lines to plot a graph
index_future_dates=pd.date_range(start='2022-11-17',end='2022-12-16')
pred=model.predict(start=start,end=end,typ='levels').rename('ARIMA predictions')
pred.index=index_future_dates
pred.plot(legend=True)
test['avg_temp'].plot(legend=True)


# In[26]:


# pred.plot(legend='ARIMA Predictions')
# test['avg_temp'].plot(legend=True)


# In[52]:


test['avg_temp'].mean()


# In[53]:


from sklearn.metrics import mean_squared_error
from math import sqrt
rmse=sqrt(mean_squared_error(pred,test['avg_temp']))
print(rmse)


# In[54]:


model2=ARIMA(df['avg_temp'],order=(1,0,5))
model2=model2.fit()
df.tail()


# In[57]:


index_future_dates=pd.date_range(start='2022-12-16',end='2022-12-19')
#print(index_future_dates)
pred=model2.predict(start=len(df),end=len(df)+3,typ='levels').rename('ARIMA Predictions')
#print(comp_pred)
pred.index=index_future_dates
print(pred)


# In[58]:


pred.plot(figsize=(12,5),legend=True)


# In[ ]:





# In[ ]:




