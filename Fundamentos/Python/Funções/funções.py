print(30*"-")

def myFunction(): #create function
    print("hellow world!")
myFunction() #execute function

print(30*"-")

def printFirstName(firstName): #usando um parametro
    print(f"First name: {firstName}")
printFirstName("Gustavo")

print(30*"-")

def printCompleteName(firstName, lastName): #usando dois parametros
    print(f"First name: {firstName}\nLast name: {lastName}")
printCompleteName("Gustavo", "Martins")

print(30*"-")

def partyPlayers(*nickNamePlayers): #usando diversos parametros utilizando "*" antes da variável, isso cria uma tupla
    for x in nickNamePlayers:
        print(f"Nick name player{nickNamePlayers.index(x)+1}: {x}")
partyPlayers("celaena sardotienn", "wilmarcus silver", "tio ben")

print(30*"-")

def myFunction2(country="Brazil"): #parametro começa com um valor padrao caso nenhum seja atribuido
    print(f"Country: {country}")
myFunction2()
myFunction2("China")

print(30*"-")

def multiplicationFunction(x,y): #return para retornar um valor
    return x*y
print(multiplicationFunction(3,5))

print(12*"-" + "Lambda" + 12*"-")
x = lambda a: a+10 #uma função rapida e simples
print(x(1))

print(30*"-")

x = lambda a,b: a*b
print(x(2,45))

print(30*"-")








