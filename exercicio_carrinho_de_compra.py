"""
Faça uma list comprehension para somar os valores de um carrinho de compra de um e-commerce
"""
carrinho = []
carrinho.append(('Produto 1',  30))
carrinho.append(('Produto 2',  20))
carrinho.append(('Produto 3',  50))
#
# total = []
# for produto in carrinho:
#     total.append(produto[1])
#
# print(total)
# print(sum(total))

# Forma mais aceita em Python
total = [produto[1] for produto in carrinho]
print(total)
print(sum(total))