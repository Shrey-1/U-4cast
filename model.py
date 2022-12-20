# import pandas as pd
# from neuralprophet import NeuralProphet
# from matplotlib import pyplot as plt
# import warnings
# warnings.filterwarnings('ignore')

# df = pd.read_csv('data/data.csv')
# # df.tail()

# df.drop_duplicates(subset="date", keep="last", inplace=True)

# df ['date'] = pd.to_datetime(df['date'])
# df.tail()

# plt.plot(df['date'], df['avg_temp'])
# plt.show()

# new_column = df[['date', 'avg_temp']] 
# new_column.dropna(inplace=True)
# new_column.columns = ['ds', 'y'] 
# new_column.tail()

# n = NeuralProphet()
# model = n.fit(new_column, freq='D', epochs=3000)

# future = n.make_future_dataframe(new_column, periods=12)
# forecast = n.predict(future)
# forecast.head()

# def plot_forecast(forecast):
#     fig1 = n.plot(forecast)
#     # fig2 = n.plot_components(forecast)
#     return fig1

# plot = n.plot(forecast)
# # n.set_plotting_backend('plotly')
