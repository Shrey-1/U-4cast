import pandas as pd
import plotly.express as plt
import plotly.graph_objects as go
import datetime as dt
import warnings
warnings.filterwarnings('ignore')

def starter(df):
    df.loc[df['humidity'] <= 30, 'rainstatus'] = 'No Chance' # No chance of rain
    df.loc[(df['humidity'] > 30) & (df['humidity'] <= 50),'rainstatus'] = 'Low Chance' # Low chance of rain
    df.loc[(df['humidity'] > 50) & (df['humidity'] <= 85),'rainstatus'] = 'Moderate Chance' # Moderate chance of rain
    df.loc[df['humidity'] > 85, 'rainstatus'] = 'High Chance' # High chance of rain

    df.loc[df['avg_temp'] <= 10, 'weather'] = 'Cold' 
    df.loc[(df['avg_temp'] > 10) & (df['avg_temp'] <= 20),'weather'] = 'cool'
    df.loc[(df['avg_temp'] > 20) & (df['avg_temp'] <= 28),'weather'] = 'Mild'
    df.loc[(df['avg_temp'] > 28) & (df['avg_temp'] <= 35),'weather'] = 'Warm'
    df.loc[df['avg_temp'] > 35, 'weather'] = 'Hot'

    df['date'] = pd.to_datetime(df['date'])

# GROUPING DATA FOR VISUALISING DATE VS AVG_TEMP
def date_vs_avg_temp(df):
    starter(df)
    df2 = df.groupby('date')['avg_temp'].mean() 
    df2 = df2.to_frame().reset_index()
    df2['avg_temp'] = round(df2['avg_temp'],2)

    fig = plt.line(df2, x='date', y='avg_temp', template='plotly_white',
        labels={"date": "Date", "avg_temp": "Average Temperature (C)",}, 
        title = "Date V/S Average Temperature"
    )
    fig.update_traces(line = dict(color='#12a4d9',width=1.5),fill="toself")
    return fig

# VISUALISING DATE V/S MAX AND MIN DATES
def date_vs_max_min_temp(df):
    starter(df)
    max1 = df.groupby('date')['max_temp'].max()
    min1 = df.groupby('date')['min_temp'].min()
    df3 = pd.merge(max1, min1, on='date', how='inner').reset_index()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df3['date'], y=df3['max_temp'],line=dict(color='#077b8a',width=1.5),name="max temp", fill="tozeroy"))
    fig.add_trace(go.Scatter(x=df3['date'], y=df3['min_temp'],line=dict(color="#e52165",width=1.5),name="min temp",fill="tozeroy"))
    fig.update_layout(title='Date V/S Min Temp & Max Temp', xaxis_title='Date', yaxis_title='Temperature (degrees C)',
                        legend=dict(orientation="h",title="Temperatures"))
    return fig

# VISUALISING DATE V/S HUMIDITY
def date_vs_humidity(df):
    starter(df)
    df4 = df.groupby('date')['humidity'].mean() 
    df4 = df4.to_frame().reset_index()
    df4['humidity'] = round(df4['humidity'],2)

    fig = plt.line(df4, x='date', y='humidity', title = "Date V/S Humidity")
    fig.update_traces(line = dict(color='#1868ae',width=1.50))
    fig.update_layout(title='Date V/S Humidity', xaxis_title='Date', yaxis_title='Humidity %')
    return fig

# VISUALISING CHANCES OF RAINFALL OCCURRENCES
def rainstatus(df):
    starter(df)
    rstatus = df['rainstatus'].value_counts().to_frame().reset_index()
    colors =['#316879','#f47a60','#7fe7dc','#ced7d8']
    fig = plt.pie(rstatus,values='rainstatus',names='index',title="Chances of Rainfall",hover_data=['index'])
    fig.update_layout(title_x=0.45)
    fig.update_traces(textposition='inside', textinfo='percent+label',marker=dict(colors=colors,line=dict(color='#000000', width=1)))
    return fig

# VISUALISING THE DIFFERENT WEATHER CONDITIONS OCCURRED 
def weather(df):
    starter(df)
    wth = df['weather'].value_counts().to_frame().reset_index()
    colors = [ '#e0cdbe','#edca82', '#097770','#a9c0a6']
    fig = plt.pie(wth,values='weather',names='index',title="Weather Conditions")
    fig.update_layout(title_x=0.47)
    fig.update_traces(textposition='inside', textinfo='percent+label',textfont_size=12,marker=dict(colors=colors,line=dict(color='#000000', width=1)))
    return fig

# PAST WEEK TEMPERATURES 
def pastweek_temp(df):
    starter(df)
    edate = df['date'][len(df)-1]
    sdate = edate - dt.timedelta(days=7)
    week_dates = pd.date_range(sdate,periods=8).to_frame().reset_index()
    datelist = week_dates[0].to_list()
    datelist.pop(0)
    duplicate_df = df
    duplicate_df['pastweek'] = df['date'].isin(datelist).astype(int)
    duplicate_df = duplicate_df[duplicate_df['pastweek']==1]

    colors = ['#408ec6'] 
    fig = go.Figure()
    fig.add_trace(go.Bar(x=duplicate_df['date'], y=duplicate_df['max_temp'],name="max temp",marker_color='#e0cdbe'))
    fig.add_trace(go.Bar(x=duplicate_df['date'], y=duplicate_df['min_temp'],name="min temp",marker_color='#a9c0a6'))
    fig.update_layout(title='Min Temp & Max Temp For the Past Week', xaxis_title='Date', yaxis_title='Temperature (degrees C)',
                    legend=dict(title="Temperature"))
    fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
    return fig

#  AQI IN THE PAST WEEK
def pastweek_aqi(df):
    starter(df)
    edate = df['date'][len(df)-1]
    sdate = edate - dt.timedelta(days=7)
    week_dates = pd.date_range(sdate,periods=8).to_frame().reset_index()
    datelist = week_dates[0].to_list()
    duplicate_df = df
    duplicate_df['pastweek'] = df['date'].isin(datelist).astype(int)
    duplicate_df = duplicate_df[duplicate_df['pastweek']==1]
    aqi = duplicate_df.groupby('date')['AQI'].mean() 
    aqi = aqi.to_frame().reset_index()
    fig = plt.line(x=aqi['date'],y=aqi["AQI"],markers=True)
    fig.update_layout(title='AQI FOR THE PAST WEEK', xaxis_title='Date', yaxis_title='AQI',height=400,width=500)
    fig.update_traces(fill="toself")
    return fig
