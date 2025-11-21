from connection import get_connection
import config

def search_by_book_name(keyword):
    conn = get_connection(config.user,config.password,config.host,config.database)
    cursor = conn.cursor()
    query= """SELECT book_id ,title, authors ,average_rating  
                    FROM books  
                    WHERE title LIKE CONCAT('%%',%s,'%%')"""
    cursor.execute(query,keyword)

    rows = cursor.fetchall()
    for r in rows:
        print(r)



def search_by_authors(author_name):
    conn = get_connection(config.user,config.password,config.host,config.database)
    cursor = conn.cursor()
    query = """
    SELECT book_id ,title ,authors ,average_rating
    FROM books
    WHERE authors LIKE CONCAT('%%',%s,'%%')
    """
    cursor.execute(query,author_name)

    rows = cursor.fetchall()
    for r in rows:
        print(r)


def most_or_least_appearing_author(user_input):
    conn = get_connection(config.user,config.password,config.host,config.database)
    cursor = conn.cursor()

    if user_input == 'most':
        kind = "DESC"
    else:
        kind = "ASC"

    query = f"""
    SELECT authors ,COUNT(*) AS num
    FROM books
    GROUP BY authors
    ORDER BY num {kind}
    LIMIT 1
    """
    cursor.execute(query)
    rose = cursor.fetchone()
    print(rose)


def highest_lowest_rating(user_input):
    conn = get_connection(config.user,config.password,config.host,config.database)
    cursor = conn.cursor()

    if user_input == 'high':
        kind = "DESC"
    else:
        kind = "ASC"

    query =  f"""
    SELECT *
    FROM books
    ORDER BY average_rating {kind}
    LIMIT 10
    """
    cursor.execute(query)
    rose = cursor.fetchall()

    for r in rose:
        print(r)


def free_query(query):
    if query[0:6] == "SELECT":
        if "UPDATE" not in query and "DELETE" not in query:
            conn = get_connection(config.user,config.password,config.host,config.database)
            cursor = conn.cursor()
            cursor.execute(query)
            rose = cursor.fetchall()

            for r in rose:
                print(r)
        else:
            print("only print")

    else:
        print("no select")






