from config.connection import Connection

class Alumno:
    def __init__(self, nombres, codigo_alumno, edad, correo, celular, dni, salon_id):
        self.nombres = nombres
        self.codigo_alumno = codigo_alumno
        self.edad = edad
        self.correo = correo
        self.celular = celular
        self.dni = dni
        self.salon_id = salon_id

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS alumnos(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombres character varying(50) NOT NULL,
                    codigo_alumno integer NOT NULL,
                    edad character varying(2) NOT NULL,
                    correo character varying(35) NOT NULL,
                    celular character varying(9) NOT NULL,
                    dni character varying(8) NOT NULL,
                    salon_id integer NOT NULL,
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_alumnos(self):
        try:
            conn = Connection('alumnos')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'nombres: {record[1]}')
                print(f'codigo_alumno: {record[2]}')
                print(f'edad: {record[3]}')
                print(f'correo: {record[4]}')
                print(f'celular: {record[5]}')
                print(f'dni: {record[6]}')
                print(f'salon_id: {record[7]}')
                print('=====================')
        except Exception as e:
            print(e)

    def insert_alumnos(self):
        try:
            conn = Connection('alumnos')
            conn.insert({
                'nombres': self.nombres,
                'codigo_alumno': self.codigo_alumno,
                'edad': self.edad,
                'correo': self.correo,
                'celular': self.celular,
                'dni': self.dni,
                'salon_id': self.salon_id
            })
            print(f'Se registro el alumno: {self.nombres} con el codigo {self.codigo_alumno}, edad: {self.edad}, correo {self.correo}, celular {self.celular}, dni {self.dni} y salon {self.salon_id}')
        except Exception as e:
            print(e)

Jean = Alumno("Jean", 10, 25, 'a@gmail', 123456789, 12345678, 1)
Jean.all_alumnos()
