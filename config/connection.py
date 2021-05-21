from psycopg2 import connect

class Connection:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db = connect(host='localhost', user='postgres', password='987521',
                        database='Reto6', port=5432)
        self.cursor = self.db.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.commit()

    def select(self, data=[]): # lista
        fields = ", ".join(data)
        if not len(data): # False
            fields = '*'

        query = f'''
            SELECT {fields} FROM {self.table_name} ORDER BY id
        '''
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def select_inner(self):
        query = f'''
            SELECT p.dni, p.nombre as pnombre, c.nombre as cnombre FROM curso_docente cd 
            INNER JOIN profesor p ON p.id = cd.profesor_id
            INNER JOIN cursos c ON c.id = cd.curso_id
        '''
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def count_total(self):
        query = f'''
            SELECT count(*) FROM {self.table_name}
        '''
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

    def insert(self, data):
        list_values = ""
        for value in data.values():
            if isinstance(value, str):
                value = f"'{value}'"
            list_values += f'{value},'
        print(list_values)
        query = f'''
            INSERT INTO {self.table_name} ({", ".join(data.keys())}) VALUES ({list_values[:-1]})
        '''
        self.execute_query(query)
        return True

    def update(self, id_object, data):
        list_where = []
        for field_name, field_value in id_object.items():
            if isinstance(field_value, str):
                field_value = f"'{field_value}'"
            list_where.append(f"{field_name}={field_value}")
        
        list_update = []
        for field_name, field_value in data.items():
            if isinstance(field_value, str):
                field_value = f"'{field_value}'"
            list_update.append(f"{field_name}={field_value}")
            
        query = f'''
            UPDATE {self.table_name} SET {', '.join(list_update)}
            WHERE {' AND '.join(list_where)}
        '''
        self.execute_query(query)
        return True
    
    def delete(self, id_object):
        list_where = []
        for field_name, field_value in id_object.items():
            if isinstance(field_value, str):
                field_value = f"'{field_value}'"
            list_where.append(f"{field_name}={field_value}")

        query = f'''
            DELETE FROM {self.table_name} WHERE {' AND '.join(list_where)}
        '''
        query_refresh = f'''
            ALTER TABLE {self.table_name} ALTER COLUMN id SET DEFAULT {(self.count_total()) + 1}
        '''
        
        self.execute_query(query)
        self.execute_query(query_refresh)
        return True

    def commit(self):
        self.db.commit()
        return True

    def rollback(self):
        self.db.rollback()
        return True
