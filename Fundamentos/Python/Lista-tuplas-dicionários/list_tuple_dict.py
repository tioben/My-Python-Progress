#list
myStrList = ["apple", "banana", "kiwi"]
print(myStrList)

myBooleanList = [True, False, False]
print(myBooleanList)

myNumberList = [2,3,5]
print(myNumberList)

myRandomList = ["apple", True, 5]
print(myRandomList)

myListList = [["orange", "pineapple", "melon"], [1,2,3], [True,False,False], [1.2, 2.3, 5.6]]
print(myListList)

print(myStrList[0])
print(myStrList[-1])
print(myStrList[0:4])
print(myListList[0])

testList = [1,2,3] #list is a collection which is ordered and changeable. Allows duplicate members.
testList.insert(3,5) #possible
print(testList)

testTuple = (1,2,3)  #tuple is a collection which is ordered and unchangeable.
testList.insert(3,5) #not possible
print(testTuple)

fruits = ["apple", "banana", "cherry"]
more_fruits = ["orange", "mango", "grapes"]
print(fruits)
print(more_fruits)

for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

fruits.pop(2)   #remove index2
print(fruits)

fruits.append("cherry") #add "cherry" to last index
print(fruits)

fruits.remove("cherry") #remove "cherry"
print(fruits)

fruits.insert(1,"cherry")   #insert "cherry" in index 1
print(fruits)

fruits.extend(more_fruits)  #extend list
print(fruits)

i=0
while i < len(fruits):
    print(fruits[i])
    i += 1

[print(x) for x in fruits]

listEmpty = []
for x in fruits:
    if 'e' in x:
        listEmpty.append(x)

print('-')

print(listEmpty)#lista de frutas
listEmpty.sort()#colocando em ordem alfabetica crescente
print(listEmpty)
listEmpty.sort(reverse=True)#colocando em ordem alfabetica decrescente
print(listEmpty)

listEmpty.reverse()
print(listEmpty)

print("***")
listEmptyCopy = listEmpty.copy() #copiando uma lista metodo1
print(listEmptyCopy)

listEmptyCopy2 = list(listEmpty) #copiando uma lista metodo2
print(listEmptyCopy2)

numberList = [1,2,3,4,5]
lettersList = ["a","b","c","d"]

somaList = numberList + lettersList #um metodo para somar listas
print(somaList)

for x in lettersList: #outro metodo para somar listas
    somaList.append(x)
print(somaList)

somaList2 = []
somaList2.extend(numberList) #outro metodo para somar listas
print(somaList2)

print("---tuplas---")
tuple1 = ("apple",) #this is a tuple
tuple2 = ("apple") #this is a str
print(type(tuple1)); print(type(tuple2))

thisTuple = tuple(("apple", "onion")) #create the tuple
print(thisTuple)

fruitsTuple = ('apple', 'banana', 'cherry')#soma the tuple
numberTuple = (1,2,3,4)
somaTuple = fruitsTuple + numberTuple
print(fruitsTuple, " ",numberTuple); print(somaTuple)

(red, yellow, pink) = fruitsTuple #descompactando tupla
print(red); print(yellow); print(pink)

print("---Set---")
thisSet = {1,2,3,2} #não permite valores duplicados
print(thisSet)
print(type(thisSet))

thisSet = {1,2,3,True,4,5} #1 == True
print(thisSet)

print(True in thisSet)

thisSet.add("apple") #adicionando item
print(thisSet)

thisSet2 = {"blue", 12, False, 45.2}

thisSet.update(thisSet2) #somando sets
print(thisSet)

thisSet = {"apple", "banana", "strawberries"} #apenas os que são iguais
thisSet2 = {"apple", "rice", "tomato"}

thisSet.intersection_update(thisSet2) 
print(thisSet)

thisSet = {"apple", "banana", "strawberries"} #tudo exceto o que são iguais
thisSet2 = {"apple", "rice", "tomato"}

thisSet.symmetric_difference_update(thisSet2)
print(thisSet)


