import pymysql
import config
from db.connection import get_connection
from db import queries ,load_csv




def user_menu():
    conn = get_connection(pymysql, config)
    user_wants = True
    while user_wants:
        user_selection = input("""
                1. Load CSV into DB
                2. Search records by book name
                3. Search records by author
                4. Find most/least frequent author
                5. Find highest/lowest rated books
                6. Free SQL query
                0. Exit
                """)
        try:
            user_selection = int(user_selection)
        except ValueError:
            print("________only numbers________")
            continue

        if user_selection < 0 or user_selection> 6 :
            print("________only 0-6__________")
            continue

        if user_selection == 0:
            user_wants = False

        if user_selection == 6:
            result = queries.free_query(conn,input("תכניס שאילתה"))

        if user_selection == 1:
            load_csv.load_from_csv(conn)

        if user_selection == 2:
            result = queries.search_by_book_name(conn,input("תכניס את שם הספר"))
            print(result)





user_menu()



