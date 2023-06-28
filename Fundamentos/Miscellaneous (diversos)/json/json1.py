#JSON é uma sintaxe para armazenar e trocar dados.
#JSON é texto, escrito com notação de objeto JavaScript.

import json

#Se você tiver uma string JSON, poderá analisá-la usando o json.loads()método.
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(type(y), y)

#Se você tiver um objeto Python, poderá convertê-lo em uma string JSON usando o json.dumps()método.
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(type(y), y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

