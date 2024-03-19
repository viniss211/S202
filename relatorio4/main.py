from database import Database
from helper.write_a_json import write_a_json
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
pa = ProductAnalyzer(db)

# Chamada das funções para pegar cada tipo de dado

pa.VendasPorDia()
pa.ProdutoMaisVendido()
pa.ClienteMaiorCrompa()
pa.vendidosMaisDe1()
