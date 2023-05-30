a = 3
b = 4

if a > b: #condicao em varias linhas
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} and {b} are equal")
else:
    print(f"{b} is greater than {a}")

if a < b: print(f"{a} is less than {b}") #condicao em uma linha so opcao1

a=1
b=200
print(a) if a>b else print(b) #condicao em uma linha so opcao2

a = 330
b = 330
print(a) if a>b else print("=") if a==b else print(b) #mais de um if na mesma linha

if a>b or a==b: #or condition
    print("ök")

if a>b and a==b: #and condition
    print("ok")
else: 
    print('nok')

if not a>b and a==b: #not + and condition
    print("ok")
else: 
    print('nok')

if type(a) == "str":
    print('ok')

if a==b:
    pass


