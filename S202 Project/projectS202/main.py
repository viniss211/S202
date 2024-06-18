from database import Database
from match_database import DB_Runner
import time

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("neo4j+s://f01561b6.databases.neo4j.io", "neo4j", "qcRqrUBn8aD-ygJ84rAtJqdAJMXO6mE0mddYPBMtVEA")
db_runner = DB_Runner(db)

print("Library management system")

while True:
    print("--------------------")
    print("Insert book (1)")
    print("Insert author (2)")
    print("Link book/author (3)")
    print("Update book (4)")
    print("Delete book (5)")
    print("Print book (6)")
    print("Exit (0)")
    print("--------------------")
    control = input("Choose an option: ")

    if control == '1':
        book_title = input("Book title: ")
        rl_year = input("Release year: ")
        literature_type = input("Literature type: ")
        db_runner.insert_book(book_title, rl_year, literature_type)
        print(f"Book '{book_title}' inserted successfully.")
    elif control == '2':
        author_name = input("Name: ")
        genre = input("Genre: ")
        db_runner.insert_author(author_name, genre)
        print(f"Author '{author_name}' inserted successfully.")
    elif control == '3':
        book_title = input("Book title: ")
        author_name = input("Author's name: ")
        db_runner.link_book_author(book_title, author_name)
        print(f"Linked book '{book_title}' with author '{author_name}'.")
    elif control == '4':
        old_name = input("Old book name: ")
        new_name = input("New book name: ")
        db_runner.update_book(old_name, new_name)
        print(f"Book title updated from '{old_name}' to '{new_name}'.")
    elif control == '5':
        book_to_delete = input("Book to delete: ")
        db_runner.delete_book(book_to_delete)
        print(f"Book '{book_to_delete}' deleted successfully.")
    elif control == '6':
        book_title = input("Book title to print: ")
        book = db_runner.get_book(book_title)
        if book:
            print(f"Title: {book['title']}, Release Year: {book['release_year']}, Literature Type: {book['literature_type']}")
        else:
            print(f"Book '{book_title}' not found.")
    elif control == '0':
        print("Exiting...")
        time.sleep(1)
        break
    else:
        print("Invalid option. Please choose again.")

# Fechar a conexão com o banco de dados
db.close()