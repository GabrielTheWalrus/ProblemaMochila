from AlgoritmoGenetico import AlgoritmoGenetico
from Individuo import Individuo

def main():
    '''
        Módulo principal
    '''

    algoritmo_genetico = AlgoritmoGenetico()
    melhor_solucao, melhor_valor = algoritmo_genetico.process()

    if algoritmo_genetico.calcular_fitness(individuo=melhor_solucao) == melhor_valor:
        print(f"\nMelhor solução encontrada: {melhor_solucao.cromossomo}")
        print(f"Valor da melhor solução: R${melhor_valor}")

if __name__ == "__main__":
    main()
