from config.connection import Connection
from time import sleep

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
    
    def list_all_alumnos(self):
        try:
            conn = Connection('alumnos')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}, nombres: {record[1]}')
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

class Profesor:
    def __init__(self, nombre, dni, edad, correo):
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
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'nombre: {record[1]}')
                print(f'dni: {record[2]}')
                print(f'edad: {record[3]}')
                print(f'correo: {record[4]}')
                print('=====================')

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
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'grado_id: {record[1]}')
                print(f'seccion_id: {record[2]}')
                print(f'salon_id: {record[3]}')
                print('=====================')
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

class Grado:
    def __init__(self, id):
        self.id = id

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS grado(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(25) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_grado(self):
        try:
            conn = Connection('grado')
            records = conn.select([])
            
            for record in records:
                print(f'{record[0]}: {record[1]}')
        except Exception as e:
            print(e)

class Nivel:
    def __init__(self, id):
        self.id = id

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS nivel(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(25) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_nivel(self):
        try:
            conn = Connection('nivel')
            records = conn.select([])
            
            for record in records:
                print(f'{record[0]}: {record[1]}')
        except Exception as e:
            print(e)

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

class Cursos:
    def __init__(self, id):
        self.id = id

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

    def all_cursos(self):
        try:
            conn = Connection('cursos')
            records = conn.select([])
            
            for record in records:
                print(f'{record[0]}: {record[1]}')
        except Exception as e:
            print(e)

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
            
            for record in records:
                print(f'{record[0]}: {record[1]} - {record[2]}')
        except Exception as e:
            print(e)


class Notas:
    def __init__(self, periodo_id, alumno_id, nota, curso_id):
        self.periodo_id = periodo_id
        self.alumno_id = alumno_id
        self.nota = nota
        self.curso_id = curso_id
        
    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS notas(
                    id SERIAL PRIMARY KEY NOT NULL,
                    periodo_id character varying(50) NOT NULL,
                    alumno_id character varying(8) NOT NULL,
                    nota character varying(2) NOT NULL,
                    curso_id character varying(2) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def insert_notas(self):
        try:
            conn = Connection('notas')
            conn.insert({
                'periodo_id': self.periodo_id,
                'alumno_id': self.alumno_id,
                'nota': self.nota,
                'curso_id': self.curso_id
            })
            print(f'Se registro el periodo_id: {self.periodo_id} con el alumno_id {self.alumno_id}, curso_id {self.curso_id} y nota: {self.nota}')
        except Exception as e:
            print(e)


class Reformatorio():
    def __init__(self):
        self.view_principal()

    def view_principal(self):
        while True:
            print(''' !!! BIENVENIDO ATU REFORMATORIO FAVORITO !!! 
            ¿Que deseas realizar?
                1) Ver Alumnos
                2) Ver Docentes
                3) Agregar Notas
                3) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.view_alumno()
            if opcion == "2":
                pass
                # self.view_profesor()
            if opcion == "3":
                self.add_notas()
                pass
            else:
                self.salir()

    def view_alumno(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo Alumno
                2) Lista de Alumnos por Salón
                3) Regresar
                4) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.datos_alumno()
            elif opcion == "2":
                # self.datos_salon()
                Alumno.all_alumnos("Jean")
                sleep(1)
            elif opcion == "3":
                self.view_principal()
            else:
                self.salir()

    def datos_alumno(self):
        print(''' INGRESAR DATOS DEL ALUMNO:''')
        print(''' NOMBRES: ''')
        nombres = input("> ")
        print(''' CODIGO: ''')
        codigo_alumno = input("> ")
        print(''' EDAD: ''')
        edad = input("> ")
        print(''' CORREO: ''')
        correo = input("> ")
        print(''' CELULAR: ''')
        celular = input("> ")
        print(''' DNI: ''')
        dni = input("> ")
        print(''' SALON: ''')
        salon_id = input("> ")

        insert = Alumno(nombres, codigo_alumno, edad, correo, celular, dni, salon_id)
        insert.insert_alumnos()

    def datos_salon(self):
        pass
        # print(''' ESCOGER UN NIVEL:''')
        # Nivel.all_nivel("xx")
        # sleep(1)
        # nivel_id = input("> ")

        # print(''' ESCOGER UN GRADO:''')
        # Grado.all_grado("xx")
        # sleep(1)
        # grado_id = input("> ")

        # print(''' ESCOGER UN SECCIÓN:''')
        # Seccion.all_seccion("xx")
        # sleep(1)
        # seccion_id = input("> ")

        # search = Salon(grado_id, seccion_id, nivel_id)
        # search.all_salon_xx()

    def add_notas(self):
        Alumno.list_all_alumnos("xx")
        print('''ESCOGER ID DE ALUMNOS:''')
        alumno_id = input("> ")

        Periodo.all_periodo("xx")
        print('''ESCOGER ID DE PERIODO:''')
        periodo_id = input("> ")

        Cursos.all_cursos("xx")
        print('''ESCOGER ID DE CURSO:''')
        curso_id = input("> ")

        while True:
            try:
                nota = float(
                    input(f'Ingresa nota: >'))
                if (not nota or nota < 0 or nota > 20):
                    raise Exception
                break
            except:
                print("Ingrese una nota de 0 - 20")        
            
        insert = Notas(periodo_id, alumno_id, nota, curso_id)
        insert.insert_notas()

    def salir(self):
        print(''' \\\ CERRADO ///''')
        exit()


Reformatorio()