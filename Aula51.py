"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Tiago'
# noutra_variavel = nome
# nome = 'Tg'

# print(nome)
# print(noutra_variavel)

lista_a = ['tg', 'victoria']
lista_b = lista_a

lista_a[0] = 'Tiago'
print(lista_b)
