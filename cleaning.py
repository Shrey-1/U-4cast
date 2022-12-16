def clean_data(data):
    data = data.iloc[:,1:] # Removing the first column
    data.columns = ['Date'] # Renaming column
    data = data['Date'].str.split(" ", expand=True) # Splitting Date and Time
    # data.drop(data.columns[[3,5]], axis=1, inplace=True) # Removing unnecessary columns
    data.columns = [['Date','Time','AQI','Temp_in_C','Humidity','Temp_in_C','Baro_Pressure','Altitude','Temp_in_F','Temp_in_C']] # Renaming columns
    data.to_csv('D:\\Projects\\U-4cast\\data\\clean_data.csv',index=False, header=True) # Saving the cleaned data to a new file
    return data
