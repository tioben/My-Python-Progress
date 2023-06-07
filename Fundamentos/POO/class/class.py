class controleRemoto:
    def __init__(self, cor, alturaCM, comprimentoCM, profundidadeCM):
        self.color = cor
        self.height = alturaCM
        self.width = comprimentoCM
        self.depth = profundidadeCM
        
    def volumeControl(self, botao):
        if botao == "+":
            print("aumentar volume")
        elif botao == "-":
            print("diminuir volume")

controleRemoto1 = controleRemoto("preto", 12,10,14)
print(controleRemoto1.color)

controleRemoto2 = controleRemoto("branco", 20,13,5)
print(controleRemoto2.color)

controleRemoto1.volumeControl("+")
controleRemoto2.volumeControl("-")

