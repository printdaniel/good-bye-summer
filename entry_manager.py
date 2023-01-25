import sqlite3
from base import run_query
from scrap import AccuWeather


class DataEntry:

    def __init__(self, scrap=AccuWeather(), db_file='db.sqlite3'):
        self.scrap = scrap
        self.db_file = db_file

    def variables(self):
        self.temp =  self.scrap.temperatura()
        self.salida = self.scrap.salida_sol()
        self.entrada = self.scrap.entrada_sol()
        print(f"Temperatura {self.temp} Amanecer {self.salida} Atardecer {self.entrada}")

    def entrada_datos(self):
        self.variables()
        insert_query = "INSERT INTO medidas (temperatura, salida, entrada) VALUES (?, ?, ?)"
        result = run_query(insert_query, (self.temp, self.salida, self.entrada), self.db_file)
        if result:
            print("Data inserted successfully into medidas table")
        else:
            print("Error while inserting data into medidas table")

    def mostrar_todos(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            show_query = "SELECT * FROM medidas"
            result = cursor.execute(show_query)
            conn.commit()

        print("+---------------------------------+")
        print("ID TEMPERATURA  AMANECER  ATARDECER")
        print("+---------------------------------+")


        for row in result:
            string = "|{:<2}|{:<12}|{:<8}|{:<3}".format(row[0],row[1],row[2],row[3])
            print(string)
            print('-'*31)
