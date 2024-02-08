"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# v = 'Valor' if condicao else 'Outro Valor'
# print(v)

# digito = 8
# # novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

print('Valor' if True else 'Outro Valor' if True else 'Fim')
