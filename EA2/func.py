from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def create_and_return_example(tx, nome,idade,sexo,profissao):
        query = """
            CREATE(n:$Pessoa:$profissao{
                nome: $nome,
                idade: $idade,
                sexo: $sexo
            })
        """
        result = tx.run(
            query, 
            nome = nome,
            idade = idade,
            sexo = sexo,
            profissao = profissao
        )

        try:
            return [{"nome": row["n"]["nome"]} for row in result]

        # Capture any errors along with the query and data for traceability

        except ServiceUnavailable as exception:

            print("{query} raised an error: \n {exception}".format(query=query, exception=exception))

            raise

def get_childs(tx,pai):
    query = """
        MATCH ({nome:"$pai"})-[:PAI_DE]->(p) RETURN p.nome As filhos;
            """
    
    try:
        result = tx.run(query.replace("$pai", pai))
        return [row['filhos'] for row in result]

    except ServiceUnavailable as exception:

        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))


def get_nephew(tx,tio):
    query = """
        MATCH ({nome:"$tio"})-[:TIO_DE]->(p) RETURN p.nome As sobrinhos;
            """
    
    try:
        result = tx.run(query.replace("$tio", tio))
        return [row['sobrinhos'] for row in result]

    except ServiceUnavailable as exception:

        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))     
        
def get_brother(tx,irmao):
    query = """
        MATCH ({nome:"$irmao"})-[:IRMAO_DE]->(p) RETURN p.nome As irmao;
            """
    
    try:
        result = tx.run(query.replace("$irmao", irmao))
        return [row['irmao'] for row in result]

    except ServiceUnavailable as exception:

        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))     

uri = "neo4j+s://4c000984.databases.neo4j.io"
user = "neo4j"
password = "XjRwGkm9ajHn4R-ek0qE5h9_KsuCAr6VonHL_iNy3_Y"

driver = GraphDatabase.driver(uri, auth=(user, password))

def main():
    while True:
        # Exibir o prompt para o usuário
        print(f'Bem vindo ao menu de comando')
        print("0 para sair ")
        print("1 para ver os filhos de uma determinada pessoa ")
        print("2 para ver os sobrinhos de uma determinada pessoa ")
        print("3 para ver os irmaos de uma determinada pessoa ")
        
        
        entrada = input("Digite um número: ")

        # Verificar se a entrada é '0' para sair
        if entrada == '0':
            print("Encerrando o programa...")
            break  # Sair do loop while

        # Processar a entrada do usuário
        try:
            numero = int(entrada)
            if numero == 1:
                pai = input("Entre com o nome da mãe/pai para pesquisa: ") 
                with driver.session() as session:
                    result = session.execute_read(get_childs,pai)
                    print(result)
            if numero == 2:
                tio = input("Entre com o nome da tia/tio para pesquisa: ") 
                with driver.session() as session:
                    result = session.execute_read(get_nephew,tio)
                    print(result)
            if numero == 3:
                irmao = input("Entre com o nome para ver os irmãos dessa pessoa: ") 
                with driver.session() as session:
                    result = session.execute_read(get_brother,irmao)
                    print(result)
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()    


driver.close()