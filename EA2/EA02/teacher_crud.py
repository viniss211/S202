from EA02.db import Database


class TeacherCRUD:
    def __init__(self, uri, user, password) -> None:
        self._db = Database(uri, user, password)

    def create(self, name, birth_year, cpf):
        # cria um Teacher
        query = "CREATE(:Teacher{name: $name, birth_year: $birth_year, cpf: $cpf});"
        parameters = {
            "name": name,
            "birth_year": birth_year,
            "cpf": cpf
        }

        self._db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t;"
        parameters = {
            "name": name,
        }

        result = self._db.execute_query(query, parameters)

        if result:
            return {
                'name': result[0]['t']['name'],
                'birth_year': result[0]['t']['birth_year'],
                'cpf': result[0]['t']['cpf']
            }
        else:
            return None

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf RETURN t;"
        parameters = {
            "name": name,
            "newCpf": newCpf
        }

        result = self._db.execute_query(query, parameters)

        if result:
            return {
                'name': result[0]['t']['name'],
                'cpf': result[0]['t']['cpf']
            }
        else:
            return None

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t;"
        parameters = {
            "name": name,
        }

        self._db.execute_query(query, parameters)

    def close(self):
        self._db.close()
        print('Conexão Encerrada')


if __name__ == '__main__':
    teacherCRUD = TeacherCRUD(
        'neo4j+s://866c64e8.databases.neo4j.io',
        'neo4j',
        'bFpcJvndreeqWEjuf-SmmqCxDNj9GprFlQNVna7bdxU'
    )

    teacherCRUD.create(
        name='Chris Lima',
        birth_year=1956,
        cpf='189.052.396-66'
    )

    print(teacherCRUD.read('Chris Lima'))

    teacherCRUD.update('Chris Lima', "162.052.777-77")

    print(teacherCRUD.read('Chris Lima'))

    teacherCRUD.close()
