from AlgoritmoGenetico import AlgoritmoGenetico

tamanho_populacao = 20
max_geracoes = 20
taxa_mutacao = 0.1
torneio_size = 3

melhor_valor_geral = 0
melhor_cromossomo_geral = []

for i in range(tamanho_populacao, 200, 10):
    for j in range(max_geracoes, 200, 10):
        algoritmo_genetico = AlgoritmoGenetico(tamanho_populacao=i, max_geracoes=j, taxa_mutacao=taxa_mutacao, torneio_size=torneio_size)
        melhor_solucao, melhor_valor = algoritmo_genetico.process()
        if (melhor_valor >= melhor_valor_geral) and (algoritmo_genetico.calcular_fitness(individuo=melhor_solucao) == melhor_valor):
            melhor_valor_geral = melhor_valor
            melhor_cromossomo_geral = melhor_solucao
            print("--------------------------------------------\n")
            print(f"\nMelhor solução encontrada: {melhor_solucao.cromossomo}")
            print(f"Valor da melhor solução: R${melhor_valor}")
            print(f"tamanho_populacao: {i}")
            print(f"max_geracoes: {j}")
            print(f"taxa_mutacao: {taxa_mutacao}")
            print(f"torneio_size: {torneio_size}")
            print("--------------------------------------------\n")