try:
    print(x) #x is not defined
except:
    print("Error!")


y = 0
try:
    print(y)
except:
    print("Error!")

try:
    print(h)
except NameError: #especificando o erro
    print(f"Variable is not defined!")
else:
    print("Incomum error!")
finally:
    print("The try test finish!")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


