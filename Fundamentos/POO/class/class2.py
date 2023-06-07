class cliente:
    def __init__(self, nickname, email, plan):
        self.nome = nickname
        self.email = email
        self.plano = plan

    def addClientToDatabase(self):
        pass
        
client1 = cliente("otavio", "otavio@hotmail.com.br", plan="Premium")
client1.addClientToDatabase

print(client1.nome)