#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.connection import Connection
from time import sleep
from prettytable import PrettyTable

class Alumno:
    def __init__(self, id="", nombres="", codigo_alumno="", edad="", correo="", celular="", dni="", salon_id=""):
        self.id = id
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
            p = PrettyTable()
            print("-- LISTA DE ALUMNOS --".center(80))
            p.field_names = ["ID", "Nombres", "Código", "Edad", "Correo", "Celular", "Dni", "Salon_id"]

            for record in records:
                p.add_row([record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]])
            print(p)
        except Exception as e:
            print(e)
    
    def list_all_alumnos(self):
        try:
            conn = Connection('alumnos')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE ALUMNOS --".center(80))
            p.field_names = ["ID", "Nombres"]

            for record in records:
                p.add_row([record[0], record[1]])
            print(p)

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

    def update_alumnos(self):
        try:
            conn = Connection('alumnos')
            conn.update({
                'id': self.id
            }, {
                'nombres': self.nombres,
                'codigo_alumno': self.codigo_alumno,
                'edad': self.edad,
                'correo': self.correo,
                'celular': self.celular,
                'dni': self.dni,
                'salon_id': self.salon_id
            })
            print(f'Se modifico el usuario: {self.nombres} con DNI: {self.dni}')
        except Exception as e:
            print(e)
    
    def delete_alumnos(self):
        try:
            conn = Connection('alumnos')
            conn.delete({
                'id': self.id
            })
            print(f'Se elimino el usuario.')
        except Exception as e:
            print(e)

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
            print(''' !!! BIENVENIDO A TU REFORMATORIO FAVORITO !!! 
            ¿Que deseas realizar?
                1) Ver Alumnos
                2) Ver Docentes
                3) Administrar Cursos
                4) Agregar Notas
                5) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.view_alumno()
            if opcion == "2":
                pass
                self.view_profesor()
            if opcion == "3":
                self.view_cursos()
            if opcion == "4":
                self.add_notas()
            else:
                self.salir()

    def view_alumno(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo Alumno
                2) Lista de Alumnos por Salón
                3) Modificar Alumno
                4) Eliminar Alumno
                5) Regresar
                6) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.data_insert_alumno()
            elif opcion == "2":
                # self.datos_salon()
                Alumno.all_alumnos("xx")
                sleep(1)
            elif opcion == "3":
                self.data_update_alumno()
            elif opcion == "4":
                self.data_delete_alumnos()
            elif opcion == "5":
                self.view_principal()
            else:
                self.salir()

    def data_insert_alumno(self):
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

        insert = Alumno('', nombres, codigo_alumno, edad, correo, celular, dni, salon_id)
        insert.insert_alumnos()
    
    def choose_alumno(self):
        Alumno.list_all_alumnos("xx")
        print('''ESCOGER ID DE ALUMNOS:''')

    def data_update_alumno(self):
        self.choose_alumno()
        id = input("> ")

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

        update = Alumno(id, nombres, codigo_alumno, edad, correo, celular, dni, salon_id)
        update.update_profesor()

    def data_delete_alumnos(self):
        self.choose_alumno()
        id = input("> ")
        
        delete = Alumno(id)
        delete.delete_alumnos()

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

    def view_profesor(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo Profesor
                2) Lista de Profesores
                3) Profesores por curso
                4) Modificar Profesor
                5) Eliminar Profesor
                6) Regresar
                7) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.data_insert_profesor()
            elif opcion == "2":
                # self.datos_salon()
                Profesor.all_profesores("xx")
                #sleep(1)
                pass
            elif opcion == "3":
                Profesor.list_prof_x_curso("xx")
            elif opcion == "4":
                self.data_update_profesor()
            elif opcion == "5":
                self.data_delete_profesor()
            elif opcion == "6":
                self.view_principal()
            else:
                self.salir()

    def data_insert_profesor(self):
        print(''' INGRESAR DATOS DEL PROFESOR:''')
        print(''' NOMBRES: ''')
        nombre = input("> ")
        print(''' DNI: ''')
        dni = input("> ")
        print(''' EDAD: ''')
        edad = input("> ")
        print(''' CORREO: ''')
        correo = input("> ")
        
        insert = Profesor('', nombre, dni, edad, correo)
        insert.insert_profesores()
    
    def choose_profesor(self):
        Profesor.list_all_profesores("xx")
        print('''ESCOGER ID DEL PROFESOR:''')

    def data_update_profesor(self):
        self.choose_profesor()
        id = input("> ")

        print(''' INGRESAR DATOS DEL PROPFESOR:''')
        print(''' NOMBRES: ''')
        nombre = input("> ")
        print(''' DNI: ''')
        dni = input("> ")       
        print(''' EDAD: ''')
        edad = input("> ")
        print(''' CORREO: ''')
        correo = input("> ")
        print(''' DNI: ''')
        dni = input("> ")

        update = Profesor(id, nombre, dni, edad, correo)
        update.update_profesor()

    def data_delete_profesor(self):
        self.choose_profesor()
        id = input("> ")
        
        delete = Profesor(id)
        delete.delete_profesores()

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
                    input(f'Ingresa nota: > '))
                if (not nota or nota < 0 or nota > 20):
                    raise Exception
                break
            except:
                print("Ingrese una nota de 0 - 20")        
            
        insert = Notas(periodo_id, alumno_id, nota, curso_id)
        insert.insert_notas()

    def view_cursos(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo
                2) Agregar Profesores por curso
                3) Modificar Curso
                4) Eliminar Curso
                5) Regresar
                6) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.add_cursos()
            elif opcion == "2":
                self.data_cursos_profesor()
            elif opcion == "3":
                self.data_update_cursos()
            elif opcion == "4":
                self.data_delete_cursos()
            elif opcion == "5":
                self.view_principal()
            else:
                self.salir()

    def choose_cursos(self):
        Cursos.all_cursos("xx")
        print('''ESCOGER ID DEL CURSO:''')
    
    def choose_salon(self):
        Salon.all_salon("xx")
        print('''ESCOGER ID DEL SALON:''')

    def add_cursos(self):
        print(''' INGRESAR NUEVO CURSO:''')
        nombre = input("> ")
        
        insert = Cursos(nombre)
        insert.insert_cursos()    

    def data_cursos_profesor(self):
        self.choose_profesor()
        profesor_id = input("> ")
        self.choose_salon()
        salon_id = input("> ")
        self.choose_cursos()
        curso_id = input("> ")

        insert = Salon(profesor_id, salon_id, curso_id)
        insert.insert_salon()

    def data_update_cursos(self):
        self.choose_cursos()
        id = input("> ")

        print(''' INGRESAR EL NUEVO NOMBRE DEL CURSO:''')
        nombre = input("> ")

        update = Cursos(id, nombre)
        update.update_cursos()

    def data_delete_cursos(self):
        self.choose_cursos()
        id = input("> ")
        
        delete = Cursos(id, '')
        delete.delete_cursos()

    def salir(self):
        print(''' \\\ CERRADO ///''')
        exit()


Reformatorio()