

def search_by_book_name(conn,keyword):
    cursor = conn.cursor()
    query= """SELECT book_id ,title, authors ,average_rating  
                    FROM books  
                    WHERE title LIKE CONCAT('%%',%s,'%%')"""
    cursor.execute(query,keyword)

    return cursor.fetchall()



def search_by_authors(conn,author_name):
    cursor = conn.cursor()
    query = """
    SELECT book_id ,title ,authors ,average_rating
    FROM books
    WHERE authors LIKE CONCAT('%%',%s,'%%')
    """
    cursor.execute(query,author_name)

    return cursor.fetchall()



def most_or_least_appearing_author(conn,user_input):
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
    return cursor.fetchone()



def highest_lowest_rating(conn,user_input):
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
    return cursor.fetchall()



def free_query(conn,query):
    if query[0:6] == "SELECT":
        if "UPDATE" not in query and "DELETE" not in query:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        else:
            return "only print"

    else:
        return "no select"




