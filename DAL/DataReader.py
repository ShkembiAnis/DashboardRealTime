import wget
import time
import os

start = time.time()


def get_original_data(Start):
    URL = "https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD&bom=true&query=select+*"
    response = wget.download(URL, "DAL/nyc.csv")
    print('----------  Get original data from API  ----------')
    print('Finished in: ', round(time.time() - Start, 3), " seconds")
    print('--------------------------------------------------\n\n\n')


def delete_old_data(Start):
    if os.path.exists("DAL/nyc.csv"):
        os.remove("DAL/nyc.csv")
        print('---------------  Delete old data  ----------------')
        print('Finished in: ', round(time.time() - Start, 3), " seconds")
        print('--------------------------------------------------\n\n\n')
    else:
        print("The file does not exist!")
