from database import Database
from relatorio8.match_database import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("neo4j+s://4c000984.databases.neo4j.io", "neo4j", "XjRwGkm9ajHn4R-ek0qE5h9_KsuCAr6VonHL_iNy3_Y")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
match_db = MatchDatabase(db)


match_db.create_player("Ribadara",1)

match_db.create_player("Gabigol",2)

match_db.create_player("Yasuo",3)

match_db.create_player("Yugi Muto",4)

match_db.create_player("Josimar",5)

match_db.create_player("All Might",6)

match_db.create_match(1,"4-0")
match_db.create_match(2,"4-3")


match_db.insert_player(1,"Ribadara")
match_db.insert_player(1,"All Might")
match_db.insert_player(1,"Gabigol")
match_db.insert_player(1,"Josimar")

match_db.insert_player(2,"Ribadara")
match_db.insert_player(2,"Josimar")

match_db.update_player("Yasuo","Yone")

match_db.delete_player("Gabigol")

match_db.get_player()

match_db.get_player_history("Ribadara")




# Fechando a conexão com o banco de dados
db.close()