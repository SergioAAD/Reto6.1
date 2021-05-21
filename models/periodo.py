from helpers import *

class Periodo:
    def __init__(self, id):
        self.id = id

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS periodo(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(25) NOT NULL
                    ano integer NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_periodo(self):
        try:
            conn = Connection('periodo')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE PERIODOS --".center(80))
            p.field_names = ["ID", "Nombres", "Año"]

            for record in records:
                p.add_row([record[0], record[1], record[2]])
            print(p)

        except Exception as e:
            print(e)
