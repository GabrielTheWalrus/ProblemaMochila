import random
from typing import List
from Individuo import Individuo
from Config import CAPACIDADE_MOCHILA, ITENS, TORNEIO


class AlgoritmoGenetico:
    '''
        Classe que implementa o algoritmo genético
    '''

    def __init__(
            self, tamanho_populacao : int = 100,
            max_geracoes : int = 100,
            taxa_mutacao : float = 0.1,
            mutacao_flag : bool = True,
            crossover_flag : bool = True,
            tipo_selecao = TORNEIO
        ):
        self.tamanho_populacao = tamanho_populacao
        self.max_geracoes = max_geracoes
        self.taxa_mutacao = taxa_mutacao
        self.mutacao_flag = mutacao_flag
        self.crossover_flag = crossover_flag
        self.populacao = []
        self.tipo_selecao = tipo_selecao

    def criar_populacao(self):
        '''
            Função que cria a população de indivíduos
        '''
        self.populacao = []

        for _ in range(self.tamanho_populacao):
            self.populacao.append(Individuo())

        return self.populacao

    def mutacao(self, individuo: Individuo):
        '''
            Realiza a mutação em um indivíduo trocando aleatoriamente alguns bits.
        '''
        for item in enumerate(individuo.cromossomo):
            if random.random() < self.taxa_mutacao:
                individuo.cromossomo[item[0]] = 1 - individuo.cromossomo[item[0]]

        return individuo

    def crossover_binario(self, pai1: Individuo, pai2: Individuo):
        '''
            Realiza o crossover de ponto único entre dois pais para gerar dois filhos.
        '''
        ponto_corte = random.randint(0, len(pai1.cromossomo) - 1)

        filho1 = Individuo()
        filho2 = Individuo()

        filho1.cromossomo = pai1.cromossomo[:ponto_corte] + pai2.cromossomo[ponto_corte:]
        filho2.cromossomo = pai2.cromossomo[:ponto_corte] + pai1.cromossomo[ponto_corte:]

        return filho1, filho2

    def selecao_torneio(self, populacao: List[Individuo], torneio_size: int = 3) -> list:
        '''
            Seleciona os pais usando o método de torneio.
        '''
        pais = []
        for _ in range(2):  # Dois pais para o crossover
            participantes = random.sample(populacao, torneio_size)
            fitness = [self.calcular_fitness(participante) for participante in participantes]
            index_melhor_participante = fitness.index(max(fitness))
            melhor_participante = participantes[index_melhor_participante]
            pais.append(melhor_participante)

        return pais

    def calcular_fitness(self, individuo: Individuo):
        '''
            Função que calcula fitness de cada indivíduo
        '''

        valor_total = 0
        peso_total = 0

        for item in enumerate(ITENS):
            if individuo.cromossomo[item[0]] == 1:
                valor_total += ITENS[item[0]]["valor"]
                peso_total += ITENS[item[0]]["peso"]

        if peso_total > CAPACIDADE_MOCHILA:
            return 0 # Penaliza soluções que excedem a capacidade

        return valor_total

    def process(self):
        '''
            Função principal de processamento do algoritmo genetico
        '''

        self.criar_populacao()

        for geracao in range(self.max_geracoes):

            if self.tipo_selecao == TORNEIO:
                pais = self.selecao_torneio(self.populacao)
            else:
                raise NotImplementedError

            nova_populacao = []
            for _ in range(self.tamanho_populacao // 2):
                pai1 = pais[0]
                pai2 = pais[1]
                filho1, filho2 = self.crossover_binario(pai1, pai2)
                filho1 = self.mutacao(filho1)
                filho2 = self.mutacao(filho2)
                nova_populacao.extend([filho1, filho2])

            self.populacao = nova_populacao

            aptidoes = [self.calcular_fitness(individuo) for individuo in self.populacao]
            melhor_aptidao = max(aptidoes)
            melhor_individuo = self.populacao[aptidoes.index(melhor_aptidao)]

            # Mostra o progresso a cada 10 gerações
            if geracao % 10 == 0:
                print(f"Geração {geracao}: Melhor valor = R${melhor_aptidao}")

        # Retorna o melhor indivíduo encontrado
        return melhor_individuo, melhor_aptidao
