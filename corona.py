import numpy as np
import pandas as pd

DATA_DIR = 'C:\\Projects\\Python\\covid-19\\data\\'

INFECTED = DATA_DIR + 'time-series-19-covid-combined.csv'
DEATHS = DATA_DIR + 'time-series-19-covid-combined.csv'

#-------------------------------------------------------------------
# Transpose DataFrame
#-------------------------------------------------------------------

# The time series data is in wide format. Move dates and counts to
# row format.

def transpose_df(df):
    data = []
    dates = list(df.columns)[4:]
    for index, row in df.iterrows():
        for date in dates:
            new_row = [date,
                       row[date],
                       row['Province/State'],
                       row['Country/Region'],
                       row['Lat'],
                       row['Long']]
            data.append(new_row)
    new_df = pd.DataFrame(data, columns=columns)
    return new_df

#-------------------------------------------------------------------

def load_corona_data (file=INFECTED):
    df = pd.read_csv (file)
    original = ['Date', 'Country/Region', 'Province/State', 'Lat', 'Long',
                'Confirmed', 'Recovered', 'Deaths']
    new = ['date','country','province','lat','long','cases','recovered','deaths']
    columns = dict(zip(original, new))
    df = df.rename(columns=columns)
    return df

#-------------------------------------------------------------------
# End of File
#-------------------------------------------------------------------
