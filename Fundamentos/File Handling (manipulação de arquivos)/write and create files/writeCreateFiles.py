y = open("C:\\Users\\tiobe\\Documents\\GitHub\\My-Python-Progress\\Fundamentos\\File Handling\\demofile.txt", "a")
y.write("\nBy: Gustavo Martins")
y.close()

y = open("C:\\Users\\tiobe\\Documents\\GitHub\\My-Python-Progress\\Fundamentos\\File Handling\\demofile.txt", "r")
print(y.read())
