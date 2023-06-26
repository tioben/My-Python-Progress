#Existe uma função interna para listar todos os nomes de funções (ou nomes de variáveis) em um módulo. A dir()função:

import platform
from myModule import person2

x = dir(platform)
print(x)

y = person2["Name"]
print(y)