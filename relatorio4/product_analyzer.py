from database import Database
from helper.write_a_json import write_a_json


class ProductAnalyzer:
    def __init__(self, database: Database):
        self._database = database

    def VendasPorDia(self):
        resultado = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {
                "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": None, "total": {"$sum": "$total"}}}
        ])

        write_a_json(resultado, "total_vendas_por_dia")

    def ProdutoMaisVendido(self):
        resultado = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao",
                        "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])

        write_a_json(resultado, "produto_mais_vendido")

    def ClienteMaiorCrompa(self):
        resultado = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {
                "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])

        write_a_json(resultado, "cliente_maior_compra")

    def vendidosMaisDe1(self):
        resultado = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match":{"produtos.quantidade":{"$gt": 1}}},
            {"$group": {"_id": "$produtos.descricao", "totalVendido": {
                "$sum": "$produtos.quantidade"}}},
            {"$sort": {"totalVendido": -1}},
            {"$project": {"_id":1, "totalVendido": 1}},
        ])
        
        write_a_json(resultado, "produtos_vendidos_mais_que_1")
