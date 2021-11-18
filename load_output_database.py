import psycopg2


class Database:

    def __init__(self, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST):
        self.con = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        self.sql = self.con.cursor()

    def insert_into_table(self, table_name: str, rows_name: list, row_data: tuple, all_pk=False, have_one_col_data=False):
        with self.con:
            rows_name = ",".join(rows_name)
            if all_pk and have_one_col_data:
                if len(row_data) == 1:
                    self.sql.execute(f"INSERT INTO {table_name}({rows_name}) VALUES('{row_data[0]}')")
                else:
                    self.sql.execute(f"INSERT INTO {table_name}({rows_name}) VALUES{row_data}")


