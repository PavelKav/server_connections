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
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")
    '''
    # create new table
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

    site, login, password = "vk", "anassna", "klASdfsjsd123flkh"

    '''
    def add_data_in_db(site, login, password):
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO data_password (site, login, password) VALUES
                ('{site}', '{login}', '{password}');"""
            )
            print(f"Data was successfully inserted")
    '''

    # add_data_in_db(site, login, password)

    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT * FROM data_password
                WHERE site = 'vk';"""
        )
        print(f"Login = {cursor.fetchone()[2]}")
        print(f"Password = {cursor.fetchall()[2][3]}")





    # Выполнение SQL-запроса для удаления таблицы
    with connection.cursor() as cursor:
        delete_query = """Delete from data_password where id = 14"""
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

'''
def main():
    print(""" Что ты хочешь сделать? 
        (1) Создать новое значение в БД
        (выход)
    """)
    done = False

    while not done:
        choice = input('Выберите действие: ')
        if choice == "1":
            site = input('Enter site: ')
            login = input('Enter login: ')
            password = input('Enter password: ')
            add_data_in_db(site, login, password)


if __name__ == "__main__":
    main()
'''
