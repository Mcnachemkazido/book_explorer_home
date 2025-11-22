

def search_by_book_name(conn,keyword):
    cursor = conn.cursor()
    query= """SELECT book_id ,title, authors ,average_rating  
                    FROM books  
                    WHERE title LIKE CONCAT('%%',%s,'%%')"""
    cursor.execute(query,keyword)
    result = cursor.fetchall()
    cursor.close()
    return result



def search_by_authors(conn,author_name):
    cursor = conn.cursor()
    query = """
    SELECT book_id ,title ,authors ,average_rating
    FROM books
    WHERE authors LIKE CONCAT('%%',%s,'%%')
    """
    cursor.execute(query,author_name)
    result = cursor.fetchall()
    cursor.close()

    return result



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
    result = cursor.fetchone()
    cursor.close()
    return result



def highest_lowest_rating(conn,user_input):
    cursor = conn.cursor()

    if user_input == 'high':
        kind = "DESC"
    else:
        kind = "ASC"

    query =  f"""
    SELECT book_id ,title ,authors ,average_rating
    FROM books
    ORDER BY average_rating {kind}
    LIMIT 5
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result



def free_query(conn,query):
    if query[0:6] == "SELECT":
        if "UPDATE" not in query and "DELETE" not in query:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        else:
            return "only print"

    else:
        return "no select"




