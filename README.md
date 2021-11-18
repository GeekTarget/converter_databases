# converter_databases
Утилита, конвертирующая инфомацию и данные из одной базы данных - в другую.
---------------------------------------------------------------------------
Существуют два главных модуля: load_input_database и load_output_database. Первая служит для подключения базы данных, откуда нужно взять данные, а вторая - 
куда нужно ввести эти данные.
---------------------------------------------------------------------------
В load_input_database имеется одна функция connect_to_db, которая принимает в себя: 
- local_db: Boolean - указывает, локальная ли база данных (по умолч. True)
- db_path - путь к локальной базе данных (по умолч. False)
- DB_NAME - имя базы данных (если у вас нелокальная база данных, по умолч. False) 
- DB_USER - имя пользователя (если у вас нелокальная база данных, по умолч. False)
- DB_PASSWORD - пароль базы данных (если у вас нелокальная база данных, по умолч. False)
- DB_HOST - имя хоста (если у вас нелокальная база данных, по умолч. False)
Эта функция возвращает объект типа dict (словарь), содержащий: имя таблицы (ключ), объект типа tuple (кортеж, значение), содержащий: имя столбцов: list (список), данные столбца: tuple(кортеж)
---------------------------------------------------------------------------
В load_output_database имеется класс Database, для инициализации которой требуются:
- *DB_NAME - имя базы данных 
- *DB_USER - имя пользователя 
- *DB_PASSWORD - пароль базы данных
- *DB_HOST - имя хоста
Класс Database имеет одну функцию insert_into_table, служащая для вставки значений в базу данных и принимающая в себя:
- *table_name: str - имя таблицы
- *rows_name: list - список имен столбцов
- *row_data: tuple - кортеж их значений столбцов
- all_pk: Boolean - указывает, что все таблицы имеют первичный ключ (по умолч. False)
- have_one_col_data: False - указывает, что есть таблицы имеется единственный столбец, кроме первичного ключа (по умолч. False)
---------------------------------------------------------------------------
В файле main показано, как реализуется конвертирование баз данных.

Важное: эта утилита имеет ограниченный функционал, а именно: в load_input_database мы можем пока только подключить локальную базу данных MsAccess, а в load_output_database - только нелокальную
(в main показано на примере базы данных PostgreSQL). Возможно, в дальнейшем она будет обновляться.
