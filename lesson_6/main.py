# import psycopg2
#
#
# def get_db_connection():
#     return psycopg2.connect(dbname="lesson_5",
#                             user="postgres",
#                             password="1",
#                             host="localhost",
#                             port="5432")
#
#
# class Book:
#     def __init__(self, id, title, description, author):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.author = author
#
#     def save(self):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         if self.id:
#             cursor.execute(
#                 "UPDATE books SET title=%s, description=%s, author=%s WHERE id=%s",
#                 (self.title, self.description, self.author, self.id)
#             )
#         else:
#             cursor.execute(
#                 "INSERT INTO books (title, description, author) VALUES (%s, %s, %s) RETURNING id",
#                 (self.title, self.description, self.author)
#             )
#             self.id = cursor.fetchone()[0]
#         conn.commit()
#         cursor.close()
#         conn.close()
#
#     @staticmethod
#     def get_book(id):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT id, title, description, author FROM books WHERE id=%s", (id,))
#         row = cursor.fetchone()
#         cursor.close()
#         conn.close()
#         if row:
#             return Book(row[0], row[1], row[2], row[3])
#         return None
#
#     @staticmethod
#     def get_all_books():
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT id, title, description, author FROM books")
#         rows = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return [Book(row[0], row[1], row[2], row[3]) for row in rows]
