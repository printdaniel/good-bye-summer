import sqlite3

def create_base():
    try:
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
    
        # Create table
        create_table_query = '''CREATE TABLE medidas (
                                    id INTEGER PRIMARY KEY,
                                    temperatura REAL,
                                    salida REAL,
                                    entrada REAL
                                );'''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in SQLite ")
    
    except sqlite3.Error as error :
        print ("Error while connecting to SQLite", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("SQLite connection is closed")


def run_query(query, parameters=(), db_file = None):
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            print("Query executed successfully")
    except sqlite3.Error as error:
        print("Error while executing query: ", error)
