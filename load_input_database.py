import datetime

import pypyodbc


def connect_to_db(local_db=True, db_path=False, DB_NAME=False, DB_USER=False, DB_PASSWORD=False, DB_HOST=False):
    conn = pypyodbc.win_connect_mdb(db_path)
    cursor = conn.cursor()

    cursor.tables()
    tables = cursor.fetchall()[10:]
    table_names = [table_name[2] for table_name in tables]

    table_data = {}
    for table_name in table_names:
        col_data = list()

        cursor.execute(f"SELECT * FROM {table_name}")
        col_names = [desc[0] for desc in cursor.description]
        for i in cursor.fetchall():
            data = list()
            for j in i:
                a = j
                if type(j) == datetime.datetime:
                    a = str(j)
                data.append(a)
            col_data.append(data)
        table_data[table_name] = col_names, col_data
    cursor.close()
    return table_data


