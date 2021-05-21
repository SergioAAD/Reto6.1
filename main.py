#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.connection import Connection
from time import sleep
from prettytable import PrettyTable
from models.alumnos import Alumno
from models.profesor import Profesor
from models.salon import Salon
from models.grado import Grado
from models.nivel import Nivel
from models.seccion import Seccion
from models.cursos import Cursos
from models.periodo import Periodo
from models.notas import Notas

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