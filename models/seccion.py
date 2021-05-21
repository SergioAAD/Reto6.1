from helpers import *

class Seccion:
    def __init__(self, id):
        self.id = id

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS seccion(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(25) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_seccion(self):
        try:
            conn = Connection('seccion')
            records = conn.select([])
            
            for record in records:
                print(f'{record[0]}: {record[1]}')
        except Exception as e:
            print(e)
