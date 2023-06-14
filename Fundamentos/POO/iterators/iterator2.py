myStr = "banana"
myStrIter = iter(myStr)
print(next(myStrIter)) #b
print(next(myStrIter)) #a
print(next(myStrIter)) #n
print(next(myStrIter)) #a
print(next(myStrIter)) #n
print(next(myStrIter)) #a

myTuple = ("apple", "banana", "cherry")

for x in myTuple: #iterator in for loop
    print(x)

for x in myStr:
    print(x)

