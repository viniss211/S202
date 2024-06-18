from database import Database

class DB_Runner:
    def __init__(self, database: Database):
        self.db = database

    def insert_book(self, title, release_year, literature_type):
        query = "CREATE (:Book {title: $title, release_year: $release_year, literature_type: $literature_type})"
        parameters = {"title": title, "release_year": release_year, "literature_type": literature_type}
        self.db.execute_query(query, parameters)

    def insert_author(self, name, genre):
        query = "CREATE (:Author {name: $name, genre: $genre})"
        parameters = {"name": name, "genre": genre}
        self.db.execute_query(query, parameters)

    def link_book_author(self, book_title, author_name):
        query = """
        MATCH (b:Book {title: $book_title}), (a:Author {name: $author_name})
        CREATE (b)-[:WRITTEN_BY]->(a)
        """
        parameters = {"book_title": book_title, "author_name": author_name}
        self.db.execute_query(query, parameters)

    def update_book(self, old_title, new_title):
        query = "MATCH (b:Book {title: $old_title}) SET b.title = $new_title"
        parameters = {"old_title": old_title, "new_title": new_title}
        self.db.execute_query(query, parameters)

    def delete_book(self, title):
        query = "MATCH (b:Book {title: $title}) DETACH DELETE b"
        parameters = {"title": title}
        self.db.execute_query(query, parameters)

    def get_book(self, title):
        query = "MATCH (b:Book {title: $title}) RETURN b.title AS title, b.release_year AS release_year, b.literature_type AS literature_type"
        parameters = {"title": title}
        result = self.db.execute_query(query, parameters)
        if result:
            return result[0]  # Return the first match
        else:
            return None
