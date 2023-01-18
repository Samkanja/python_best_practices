import sqlite3
from typing import Dict,Any

class DatabaseManager:
    def __init__(self,database_filename) -> None:
        self.connection = sqlite3.connect(database_filename)

    def __del__(self) -> None:
        self.connection.close()

    def _execute(self,statement,value=None) -> None:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, value or [])
            return cursor


    def create_table(self, table_name,columns: Dict[Any, Any]) -> None:
        columns_with_types = [
            f'{column_name} {data_type}' for column_name
            , data_type in columns.items()
        ]
        self._execute(f'''
          CREATE TABLE IF NOT EXITS {table_name}
        ({', '.join(columns_with_types)});
        '''
      )

    def add(self, table_name, data: Dict[Any, Any]) -> None:
        placeholders = ',  '.join('?' * len(data))
        column_names = ', '.join(data.keys())
        column_values = tuple(data.values())

        self._execute(
            f'''
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            ''',column_values
        )
    
    def delete(self, table_name , criteria : Dict[Any, Any]) -> None:
        placeholders = [f'{column} = ?' for column in criteria.keys()]
        delete_creteria = ' AND '.join(placeholders)
        self._execute(
            f'''
            DELETE FROM {table_name}
            WHERE {delete_creteria};
            ''',
            tuple(criteria.values())
        )
    
    def select(self, table_name:str,criteria:Dict[Any,Any]=None,order_by:str = None):
        query = f'SELECT * FROM {table_name}'

        if criteria:
            placeholders = [f'{column} = ?' for column in criteria.keys()]
            select_criteria = ' AND '.join(placeholders)
            query += f'         WHERE {select_criteria}'

        if order_by:
            query += f' ORDER BY {order_by}'

        return self._execute(
            query,
            tuple(criteria.values())
        )
