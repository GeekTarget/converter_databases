from load_output_database import Database
from load_input_database import connect_to_db

table_info = connect_to_db(r"""C:\Users\dj_ma\Downloads\Аэрографическая мастерская.mdb""")
db = Database(DB_USER="postgres",
              DB_PASSWORD="RM4haz7",
              DB_NAME="airbrush_workshop",
              DB_HOST="localhost")


def convert_database(table_data, database, all_pk=False, have_one_col_data=False):
    for key, data in table_data.items():
        table_name = key
        row_name = data[0]
        row_data = data[1]

        for item in row_data:
            col_data = tuple(item)[1:]
            database.insert_into_table(table_name, row_name[1:], col_data, all_pk, have_one_col_data)


convert_database(table_info, db, all_pk=True, have_one_col_data=True)
