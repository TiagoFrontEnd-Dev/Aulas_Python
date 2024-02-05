"""
Iterável -> ( e um elemento que pode te entregar uma coisa por vez)str, range, etc (___iter___)
Iterador -> ( )quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iteredor
"""

# text = iter('Tiago')  # .__iter__()
# print(next(text))
# print(next(text))
# print(next(text))
# print(next(text))
# print(next(text))
# print(next(text))

text = 'Tiago'
# iterator = iter(text)

# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

for letra in text:
    print(letra)
