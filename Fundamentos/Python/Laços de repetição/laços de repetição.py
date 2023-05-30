a = 0

while a < 5:
    print(f"ok {a}")
    a += 1

b = 0
while b < 6:
    b += 1
    if b==3:
        continue #reseta o loop
    print(b)

print('-----')

b = 0
while b < 6:
    b += 1
    if b ==3:
        break #cancela o loop
    print(b)

print('-----')

c = 0
while c < 6:
    print(c)
    c += 1
else:
    print(f'{c} is no longer less than 6')

print('-----')

listNumber = [11,21,31,41,51]

for x in listNumber:
    print(x)

print("")

for x in 'banana':
    print(x)

print("")

for x in range(10):
    print(x)

print("")

for x in range(10,19): #range 10 for 18
    print(x)

print("")

