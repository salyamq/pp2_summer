import csv
from connect import get_connection
import config
from loguru import logger

@logger.catch
def create_table():
    sql = """create table if not exists phonebook(
    id serial primary key,
    name varchar(100) not null unique,
    phone varchar(20) not null unique);
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()


@logger.catch
def show_all():
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = "select * from phonebook"
            cur.execute(sql)
            results = cur.fetchall()

            for row in results:
                print(row)


@logger.catch
def insert_from_console():
    name = input("first name: ").strip()
    phone = input("phone: ").strip()

    sql = """
    insert into phonebook (name, phone) values (%s, %s)
    on conflict (phone) do nothing;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (name, phone))

            if cur.rowcount > 0:
                logger.success(f"{name, phone} added in table")
            else:
                logger.warning(f"{phone} already exists, skipping")
        conn.commit()

@logger.catch
def insert_from_csv():
    file_path = input("the path: ").strip()
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)

        sql = "insert into phonebook (name, phone) values (%s, %s) on conflict (phone) do nothing"
        with get_connection() as conn:
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute(sql, (row[0], row[1]))
            conn.commit()
    logger.success("import from csv finished")


@logger.catch
def update_name_or_number():
    choice = input("name: 1, number: 2 -> ").strip()

    if choice == '1':
        old_val, new_val = input("current name: ").strip(), input("new name: ").strip()
        sql = "UPDATE phonebook SET name = %s WHERE name = %s"
    elif choice == '2':
        old_val, new_val = input("current number: ").strip(), input("new number: ").strip()
        sql = "UPDATE phonebook SET phone = %s WHERE phone = %s"
    else:
        print("invalid choice")
        return

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (new_val, old_val))
        if cur.rowcount > 0:
            conn.commit()
            print("update successful")
        else:
            print("contact not found")


@logger.catch
def search_name():
    choice = input("search by: 1 - name, 2 - prefix of number -> ").strip()

    if choice == '1':
        name = input("your name: ").strip()
        sql = "select * from phonebook where name = %s"
        params = (name,)
    elif choice == '2':
        num_prefix = input("your number prefix: ").strip()
        sql = "select * from phonebook where phone like %s"
        params = (f"{num_prefix}%",)
    else:
        print("invalid choice")
        return

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            results = cur.fetchall()

            for row in results:
                print(row)


@logger.catch
def delete_contact():
    choice = input("search by: 1 - name, 2 - prefix of number -> ").strip()

    if choice == '1':
        name = input("your name: ").strip()
        sql = "delete from phonebook where name = %s"
        params = (name,)
    elif choice == '2':
        num_prefix = input("your number prefix: ").strip()
        sql = "delete from phonebook where phone like %s"
        params = (f"{num_prefix}%",)
    else:
        print("invalid choice")
        return

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
        conn.commit()


# ----------- menu

menu = config.MENU

def main():
    create_table()

    while True:
        print(menu)
        choice = input("choose the option: ").strip()

        if choice == '0':
            show_all()
        elif choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv()
        elif choice == '3':
            update_name_or_number()
        elif choice == '4':
            search_name()
        elif choice == '5':
            delete_contact()
        else:
            print("try again")



if __name__ == "__main__":
    main()




