import pandas as pd
from sqlalchemy import create_engine
import time

def read_data_from_database(Start):
    username = "root"
    password = "root"
    port = 3306
    database = "inno"
    engine = create_engine('mysql+mysqldb://%s:%s@localhost:%i/%s'
                           % (username, password, port, database))
    sql = "SELECT * FROM nyc_collisions;"
    df = pd.read_sql_query(sql, engine)
    print('------------  Read data from database  -----------')
    print('Finished in: ', round(time.time() - Start, 3), " seconds")
    print('--------------------------------------------------\n\n\n')
    return df
