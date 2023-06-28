import datetime

print("-"*30)
print("-"*30)
x = datetime.datetime.now()
print(x)
print(x.day)
print(x.month)
print(x.year)
print("-"*30)

print("-"*30)
y = datetime.datetime(2018, 6, 1)
print(y)
print(y.strftime("%A"))
print(y.strftime("%B"))
print(y.strftime("%C"))
print(y.strftime("%D"))
print("-"*30)


