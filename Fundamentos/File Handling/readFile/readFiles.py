y = open("C:\\Users\\tiobe\\Documents\\GitHub\\My-Python-Progress\\Fundamentos\\File Handling\\demofile.txt", "r")
print(y.read())

print("-"*8)

y = open("C:\\Users\\tiobe\\Documents\\GitHub\\My-Python-Progress\\Fundamentos\\File Handling\\demofile.txt", "r")
print(y.read(5))

print("-"*8)

y = open("C:\\Users\\tiobe\\Documents\\GitHub\\My-Python-Progress\\Fundamentos\\File Handling\\demofile.txt", "r")
print(y.readline())
print(y.readline(10))
print(y.readline())
print(y.readline())
print(y.readline())
print(y.readline())
print(y.readline())
print(y.readline())
print(y.readline())

print("-"*8)

y = open("C:\\Users\\tiobe\\Documents\\GitHub\\My-Python-Progress\\Fundamentos\\File Handling\\demofile.txt", "r")
for x in y:
    print(x)

