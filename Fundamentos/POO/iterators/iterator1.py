myTuple = ("apple", "banana", "cherry")
myTupleIter = iter(myTuple)
print(next(myTupleIter)) #apple
print(next(myTupleIter)) #banana
print(next(myTupleIter)) #cherry
print(next(myTupleIter)) #error