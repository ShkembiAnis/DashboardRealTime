import time

from DAL.DataCleaner import clean_data
from DAL.DataDeleter import delete_data_set_from_mysql
from DAL.DataReader import get_original_data, delete_old_data
from DAL.DataSetter import set_data_to_mysql
from UI.Layout import start_app

Start = time.time()

print("Update data thread has been started. Every day the data will be updated.")
def dataUpdate():
    while True:
        print("Update data thread has been started. Every day the data will be updated.")
        #time.sleep(86400)  # 86400 = 1 DAY
        # This function delete the old dataset
        delete_old_data(Start)
        # This function delete the database from mysql
        delete_data_set_from_mysql(Start)
        # This function read the dataset from API
        get_original_data(Start)
        # This function take the necessary columns from dataset and past it to a dataframe
        df_to_set = clean_data(Start)
        # This function set the dataframe to the mysql database
        set_data_to_mysql(Start, df_to_set)


start_app()



