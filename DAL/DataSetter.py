import time
from sqlalchemy import create_engine
start = time.time()


def set_data_to_mysql(Start, df):
    username = "root"
    password = "root"
    port = 3306
    database = "inno"
    tableName = "nyc_collisions"
    engine = create_engine('mysql+mysqldb://%s:%s@localhost:%i/%s'
                           % (username, password, port, database))
    dbConnection = engine.connect()

    try:
        df.to_sql(tableName, dbConnection, if_exists='fail')
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    finally:
        dbConnection.close()

    print('------------  Set dataset to database  -----------')
    print('Finished in: ', round(time.time() - Start, 3), " seconds")
    print('--------------------------------------------------\n\n\n')
