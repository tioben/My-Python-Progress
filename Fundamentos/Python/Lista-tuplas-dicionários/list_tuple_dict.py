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
print(listEmpty)




