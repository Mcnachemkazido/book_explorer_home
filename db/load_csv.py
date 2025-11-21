import csv

def load_from_csv(conn):
    user_input = input("האם ברצונך לנקות את הטבלה לפני הטעינה מחדש yes or no")
    cursor = conn.cursor()

    if user_input == 'yes':
        cursor.execute("DELETE FROM books")


    with open("data/books_100_rows.csv") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute("INSERT INTO books "
                           "(book_id, title, authors, average_rating,isbn"
                           ", isbn13, language_code, num_pages,ratings_count, text_reviews_count,"
                           "publication_date, publisher)"
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",row)
        conn.commit()







