class myNumbers ():
    def __iter__ (self):
        self.a = 1
        return self
    
    def __next__ (self):
        x = self.a
        self.a += 1
        return x

myClass = myNumbers()
myClassIter = iter(myClass)

print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))

class myNumbers ():
    def __iter__ (self):
        self.a = 1
        return self
    
    def __next__ (self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass = myNumbers()
myClassIter = iter(myClass)

print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
