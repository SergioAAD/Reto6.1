from helpers import *

class Cursos:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS cursos(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(25) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
    
    def insert_cursos(self):
        try:
            conn = Connection('cursos')
            conn.insert({
                'nombre': self.nombre
            })
            print(f'Se registro el cursos: {self.nombre}')
        except Exception as e:
            print(e)

    def all_cursos(self):
        try:
            conn = Connection('cursos')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE CURSOS --".center(80))
            p.field_names = ["ID", "Nombre"]

            for record in records:
                p.add_row([record[0], record[1]])
            print(p)

        except Exception as e:
            print(e)

    def update_cursos(self):
        try:
            conn = Connection('cursos')
            conn.update({
                'id': self.id
            }, {
                'nombre': self.nombre,
            })
            print(f'Se modifico el curso: {self.nombre}')
        except Exception as e:
            print(e)

    def delete_cursos(self):
        try:
            conn = Connection('cursos')
            conn.delete({
                'id': self.id
            })
            print(f'Se elimino el curso.')
        except Exception as e:
            print(e)
