import psycopg2
from conf import host, user, password, db_name

try:

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True
    # info server
    '''
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")
    '''
    # create new table
    '''
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE data_password(
                id serial PRIMARY KEY,
                site VARCHAR(50) NOT NULL,
                login VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL);"""
        )
        print(f'New table created')
'''
    '''site, login, password = "vk", "pavel", "hjkKJHKJHakljsdflkh"
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO data_password (site, login, password) VALUES
            ('{site}', '{login}', '{password}');"""
        )
        print(f"Data was succefully insertted")
'''
    # Выполнение SQL-запроса для удаления таблицы
    with connection.cursor() as cursor:
        delete_query = """Delete from data_password where id = 2"""
        cursor.execute(delete_query)
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно удалена")
    # Получить результат
        cursor.execute("SELECT * from data_password")
        print("Результат", cursor.fetchall())

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
