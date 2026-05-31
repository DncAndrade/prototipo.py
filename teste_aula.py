vendas = [
    {"pedido": 101, "cliente": "Ana Silva", "valor": 150.00},
    {"pedido": 102, "cliente": "Ana Silva", "valor": 300.00},
    {"pedido": 103, "cliente": "Bruno Costa", "valor": 80.00},
    {"pedido": 104, "cliente": "Carlos Lima", "valor": 450.00}
]

for item in vendas:
    if item["valor"] < 300:
        print()
        print("========================================")
        print()
        print("Menor que 300:", item["cliente"], item["valor"])
        print()
    else:
        print()
        print("Maior ou igual a 300:", item["cliente"],item["valor"])
        print()
