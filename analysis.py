import pandas as pd
import numpy as np
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

# DATE WITH THE MAXIMUM TEMPERATURE
def max_temp_date(df):
    df['date'] = pd.to_datetime(df['date'])
    max_date = df[df['max_temp'] == df['max_temp'].max()]['date'].item()
    max_date = dt.datetime.strftime( max_date ,'%Y-%m-%d')
    return max_date

# TEMP ON THE DAY OF MAXIMUM TEMPERATURE
def max_temp(df):
    temp_max = df[df['max_temp'] == df['max_temp'].max()]['max_temp'].item()
    return temp_max

# DATE WITH THE MINIMUM TEMPERATURE
def min_temp_date(df):
    df['date'] = pd.to_datetime(df['date'])
    min_date = df[df['min_temp'] == df['min_temp'].min()]['date'].item()
    min_date = dt.datetime.strftime( min_date ,'%Y-%m-%d')
    return min_date

# TEMP ON THE DAY OF MINIMUM TEMPERATURE
def min_temp(df):
    temp_min = df[df['min_temp'] == df['min_temp'].min()]['min_temp'].item()
    return temp_min

# RAINFALL STATUS
def rain_status(df):
    starter(df)
    status_df = round(df.groupby(['date','rainstatus'])['humidity'].mean(),2).to_frame().reset_index()
    status_df = status_df['rainstatus'].value_counts().to_frame().reset_index().rename(columns={'index':'status', 'rainstatus':'no_of_days'})
    return status_df

# WEATHER COUNT
def weather_count(df):
    starter(df)
    weather_df = round(df.groupby(['date','weather'])['avg_temp'].mean(),2).to_frame().reset_index()
    weather_df = weather_df['weather'].value_counts().to_frame().reset_index().rename(columns={'index':'condition', 'weather':'no_of_days'})
    return weather_df

# CHANCES OF A STORM TO OCCUR ON THE BASIS OF CHANGING BAROMETRIC PRESSURE
def storm_chances(df):
    starter(df)
    baromax1 = df.groupby(['date','rainstatus'])['baro_pressure'].max()
    baromin1 = df.groupby(['date','rainstatus'])['baro_pressure'].min()
    dfbaro = pd.merge(baromax1, baromin1, on=['date','rainstatus'], how='inner').reset_index().rename(columns={'baro_pressure_x':'max baro pressure','baro_pressure_y':'min baro pressure'})
    dfbaro = dfbaro[dfbaro['rainstatus']=='High Chance']
    return dfbaro