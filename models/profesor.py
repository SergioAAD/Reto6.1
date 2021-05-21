from helpers import *

class Profesor:
    def __init__(self,id, nombre, dni, edad, correo):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo
        
    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS profesor(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(50) NOT NULL,
                    dni character varying(8) NOT NULL,
                    edad character varying(2) NOT NULL,
                    correo character varying(50) NOT NULL,
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_profesores(self):
        try:
            conn = Connection('profesor')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE PROFESORES --".center(50))
            p.field_names = ["ID", "Nombres", "Dni", "Edad", "Correo"]

            for record in records:
                p.add_row([record[0], record[1], record[2], record[3], record[4]])
            print(p)

        except Exception as e:
            print(e)

    def list_all_profesores(self):
        try:
            conn = Connection('profesor')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE PROFESORES --".center(80))
            p.field_names = ["ID", "Nombres"]

            for record in records:
                p.add_row([record[0], record[1]])
            print(p)

        except Exception as e:
            print(e)
    
    def list_prof_x_curso(self):
        try:
            conn = Connection('profesor')
            records = conn.select_inner()
            p = PrettyTable()
            print("-- PROFESORES / CURSOS --".center(40))
            p.field_names = ["DNI", "Nombres del Profesor", "Curso"]

            for record in records:
                p.add_row([record[0], record[1], record[2]])
            print(p)

        except Exception as e:
            print(e)

    def insert_profesores(self):
        try:
            conn = Connection('profesor')
            conn.insert({
                'nombre': self.nombre,
                'dni': self.dni,
                'edad': self.edad,
                'correo': self.correo
            })
            print(f'Se registro el profesor: {self.nombre} con el dni {self.dni}, edad: {self.edad} y correo {self.correo}')
        except Exception as e:
            print(e)
   
    def update_profesor(self):
        try:
            conn = Connection('profesor')
            conn.update({
                'id': self.id
            }, {
                'nombres': self.nombre,
                'dni': self.dni,
                'edad': self.edad,
                'correo': self.correo,
            })
            print(f'Se modifico el usuario: {self.nombre} con DNI: {self.dni}')
        except Exception as e:
            print(e)
    
    def delete_profesores(self):
        try:
            conn = Connection('profesor')
            conn.delete({
                'id': self.id
            })
            print(f'Se elimino el usuario.')
        except Exception as e:
            print(e)
