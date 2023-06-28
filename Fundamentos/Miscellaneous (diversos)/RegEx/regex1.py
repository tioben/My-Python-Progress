"""Um RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.

RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado."""

import re

#Pesquise a string para ver se ela começa com "The" e termina com "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Ok!")
else:
    print("Nok!")

#A findall()função retorna uma lista contendo todas as correspondências.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

