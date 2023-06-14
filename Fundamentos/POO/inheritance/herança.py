class person:  #father class
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
    
    def printName (self):
        print(self.firstName, self.lastName)

x = person("Gustavo", "Martins")

x.printName()

#abaixo o filho herda tudo do pai

class stundent (person): #son class
    pass

y = stundent("Stella", "Martins")
y.printName()

#abaixo o filho tem sua __init__ própria

class student2 (person):
    def __init__(self, fName, mName, lName):
        self.firstName = fName
        self.midName = mName
        self.lastName = lName

a = student2("Gustavo", "Henrique", "Martins")
a.printName() #perceba que ele herdou o metodo do pai

#abaixo o filho mantém o __init__ + metodo do pai

class student3 (person):
    def __init__(self, fName, lName):
        person.__init__(self, fName, lName)

a = student3("Theo", "Martins")
a.printName()

#abaixo o filho adiciona mais um metodo
print("-"*10)
class student4 (person):
    def __init__(self, fName, mName, lName):
        super().__init__(fName, lName)
        self.midName = mName
    
    def printNameSon (self):
        print(self.firstName, self.midName, self.lastName)

a = student4("Gustavo", "Ferreira", "Martins")
a.printName()
a.printNameSon()