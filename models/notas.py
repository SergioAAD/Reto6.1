from helpers import *

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
