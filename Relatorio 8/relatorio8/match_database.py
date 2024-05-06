from database import Database

class MatchDatabase:
    def __init__(self, database: Database):
        self.db = database

    def create_player(self, name,id):
        query = "CREATE (:Player {name: $name, id: $id})"
        parameters = {"name": name , "id":id}
        self.db.execute_query(query, parameters)

    def create_match(self, id,result):
        query = "CREATE (p:Match {id: $id, result: $result})"
        parameters = {"id": id, "result": result}
        self.db.execute_query(query, parameters)

    def insert_player(self,match_id,player_name):
        query = "MATCH (p:Player {name:$name}),(m:Match{id:$id}) CREATE (p)-[:PLAYED_ON]->(m)"
        parameters = {"name":player_name,"id":match_id}
        self.db.execute_query(query,parameters)

    def get_player(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def get_player_history(self,name):
        query = "MATCH (:Player {name: $name})-[:PLAYED_ON]->(m:Match) m.id as id"
        parameters = {"name":name}
        results = self.db.execute_query(query,parameters)
        return [result["id"] for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
