from helpers import *

class Salon:
    def __init__(self, grado_id, seccion_id, nivel_id):
        self.grado_id = grado_id
        self.seccion_id = seccion_id
        self.nivel_id = nivel_id

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS salon(
                    id SERIAL PRIMARY KEY NOT NULL,
                    grado_id integer NOT NULL,
                    seccion_id integer NOT NULL,
                    salon_id integer NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_salon(self):
        try:
            conn = Connection('salon')
            records = conn.select([])
            
            p = PrettyTable()
            print("-- LISTA DE PROFESORES --".center(50))
            p.field_names = ["ID", "Grado_id", "Seccion_id", "Salon_id"]

            for record in records:
                p.add_row([record[0], record[1], record[2], record[3]])
            print(p)

        except Exception as e:
            print(e)
    
    def all_salon_xx(self):
        pass
        # try:
        #     conn = Connection('salon')
        #     records = conn.selectSearch([])
            
        #     for record in records:
        #         print(f'ID: {record[0]}')
        #         print(f'grado_id: {record[1]}')
        #         print(f'seccion_id: {record[2]}')
        #         print(f'salon_id: {record[3]}')
        #         print('=====================')
        # except Exception as e:
        #     print(e)

    def insert_salon(self):
        try:
            conn = Connection('salon')
            conn.insert({
                'grado_id': self.grado_id,
                'seccion_id': self.seccion_id,
                'nivel_id': self.nivel_id
            })
            print(f'Se registro el grado_id: {self.grado_id} con la seccion_id {self.seccion_id} y nivel_id: {self.nivel_id}')
        except Exception as e:
            print(e)
