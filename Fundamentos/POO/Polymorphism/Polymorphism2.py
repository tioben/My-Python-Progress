class cat:
    def __init__(self, raça, castrado, sexo):
        self.race = raça
        self.castrated = bool(castrado)
        self.sex = sexo

    def say (self):
        print("Meow!")

class dog:
    def __init__ (self, raça, castrado, sexo):
        self.race = raça
        self.castrated = castrado
        self.sex = sexo
    def say (self):
        print("Woof! Woof!")

gato = cat("Bengal", True, "Male")
cachorro = dog("Pit Bull", False, "Female")

for x in (gato, cachorro):
    x.say()