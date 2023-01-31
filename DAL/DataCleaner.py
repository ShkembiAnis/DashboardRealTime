import time

import pandas as pd


def clean_data(Start):
    df = pd.read_csv('DAL/nyc.csv', low_memory=False)
    df[["month", "day", "year"]] = df["CRASH DATE"].str.split("/", expand=True)
    df = df[
        ["month", "day", "year", "COLLISION_ID", "BOROUGH", "CRASH DATE", "CRASH TIME", "ON STREET NAME", "LATITUDE",
         "LONGITUDE", "NUMBER OF PERSONS INJURED", "NUMBER OF PERSONS KILLED", "VEHICLE TYPE CODE 1",
         "VEHICLE TYPE CODE 2"]]
    df.rename(columns={'month': 'MONTH',
                       'day': 'DAY',
                       'year': 'YEAR',
                       'COLLISION_ID': 'COLLISION_ID',
                       'BOROUGH': 'BOROUGH',
                       'CRASH DATE': 'CRASH_DATE',
                       'CRASH TIME': 'CRASH_TIME',
                       'ON STREET NAME': 'ON_STREET_NAME',
                       'LATITUDE': 'LATITUDE',
                       'LONGITUDE': 'LONGITUDE',
                       'NUMBER OF PERSONS INJURED': 'NUMBER_OF_PERSONS_INJURED',
                       'NUMBER OF PERSONS KILLED': 'NUMBER_OF_PERSONS_KILLED',
                       'VEHICLE TYPE CODE 1': 'VEHICLE_TYPE_CODE_1',
                       'VEHICLE TYPE CODE 2': 'VEHICLE_TYPE_CODE_2', }, inplace=True)

    print('----------------  Clean data set  ----------------')
    print('Finished in: ', round(time.time() - Start, 3), " seconds")
    print('--------------------------------------------------\n\n\n')
    return df


