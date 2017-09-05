class Pessoa:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.id_card = None


class Registro:
    def __init__(self, momento, id_card, autorizado=0,id_pessoa=None,transf_em=None):
        self.momento = momento
        self.id_card = id_card
        self.autorizado = autorizado        
        self.id_pessoa_identificada = id_pessoa
        self.transf_em = transf_em

    def __str__(self):
        return str(self.momento)+";"+str(self.id_card)+";"+str(self.autorizado)+str(self.transf_em)
          

    def __repr__(self):
        return self.__str__()

        
