import random
from Config import ITENS


class Individuo:
    '''Classe que responsável por operações de indivíduo'''

    def __init__(self):
        self.cromossomo = self.criar_individuo()

    def criar_individuo(self):
        """Cria um indivíduo (cromossomo) aleatório."""
        return [random.randint(0, 1) for _ in range(len(ITENS))]
