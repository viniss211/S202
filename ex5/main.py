from database import Database
from bookModel import BookModel

db = Database(database="relatorio", collection="books")
bookModel = BookModel(database=db)

def criar():
    titulo = input("Entre com o titulo: ")
    autor = input("Entre com o nome do autor ")
    ano = int(input("Ano de pub: "))
    preco = float(input("preco: "))
    bookModel.criar(titulo, autor, ano, preco)
    print("Livro criado!")

def pesquisar():
    book_id = input("Entre com o ID: ")
    book = bookModel.pesquisar(book_id)
    if book:
        print(book)
    else:
        print("Livro nao encontrado")

def atualiza():
    book_id = input("Entre com o ID a ser atualizado: ")
    titulo = input("titulo: ")
    autor = input("autor: ")
    ano = input("novo ano: ")
    preco = input("preco: ")

    updated_data = {}
    updated_data["titulo"] = titulo
    updated_data["autor"] = autor
    updated_data["ano"] = int(ano)
    updated_data["preco"] = float(preco)

    bookModel.atualiza(book_id, **updated_data)
    print("Book updated successfully!")

def deletar():
    book_id = input("Enter book ID to delete: ")        
    bookModel.deletar(book_id)

def main_menu():
    while True:
        print("\nMenu de livro")
        print("1. Criar")
        print("2. Pesquisa por id")
        print("3. Atualizar")
        print("4. deletar")
        print("5. Exit")

        opcao = input()

        if opcao == '1':
            criar()
        elif opcao == '2':
            pesquisar()
        elif opcao == '3':
            atualiza()
        elif opcao == '4':
            deletar()
        elif opcao == '5':
            print("saindo...")
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main_menu()