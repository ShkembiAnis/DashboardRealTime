import time
from sqlalchemy import create_engine

start = time.time()


def delete_data_set_from_mysql(Start):
    username = "root"
    password = "root"
    port = 3306
    database = "inno"
    tableName = "nyc_collisions"
    engine = create_engine('mysql+mysqldb://%s:%s@localhost:%i/%s'
                           % (username, password, port, database))
    dbConnection = engine.connect()

    engine.execute("DROP table IF EXISTS nyc_collisions")

    print('---------  Delete dataset from database  ---------')
    print('Finished in: ', round(time.time() - Start, 3), " seconds")
    print('--------------------------------------------------\n\n\n')
