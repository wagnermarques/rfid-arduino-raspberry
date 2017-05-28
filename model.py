class Pessoa:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.id_card = None


class Registro:
    def __init__(self, momento, id_card, autorizado):
        self.momento = momento
        self.id_card = id_card
        self.autorizado = autorizado

        
