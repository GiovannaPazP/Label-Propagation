import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# ================ CONSTANTES ================
MAXITE = 10
# ================ ---------- ================

'''
rede1_duas_comunidades.csv
rede2.csv
'''
G = nx.read_edgelist("rede1_duas_comunidades.csv", delimiter=',', nodetype=int)

#print(G.nodes())
#print(G)

def calcula_moda(valores):
    numeros, contagem = np.unique(valores, return_counts=True) #retorna valores unicos e quantas vezes aparece
    modas = numeros[contagem == contagem.max()] #filtra os numeros por aqueles com maior repetiçaõ
    moda = np.random.choice(modas)
    #print("moda:", moda, ",", contagem, ",", contagem.max()) #tirar dps
    return moda

def labelPropagation(G, MAXITE):
    n = G.number_of_nodes()
    rotulos = np.arange(n)

    iteracao = 0
    MUDOU = True

    for iteracao in range(MAXITE):
        if not MUDOU:
            print("Finalização por Imutabilidade")
            break ## ou seja, não mudou

        MUDOU = False
        ordem_vertices = np.random.permutation(n)
        #print(ordem_vertices)

        for i in ordem_vertices:
            vizinhos = list(G.neighbors(i)) #nao retorna None, retorna lista []

            if len(vizinhos) > 0:
                #print(vizinhos)
                rotulos_vizinhos = rotulos[vizinhos] #vizinhos é o indice, pega os valores de rotulos correspondente a essa lista de indice -- só numpy
                #print(rotulos_vizinhos)
                #print()
                novo_rotulo = calcula_moda(rotulos_vizinhos)
                if novo_rotulo != rotulos[i]:
                    rotulos[i] = novo_rotulo
                    MUDOU = True
                
    print("rotulos:", rotulos)
    return rotulos

def plot(G, rotulos):
    pos = nx.spring_layout(G, seed=42) #para plotar grafos, fixa a seed para não ficar mudando a posição
    cores = rotulos

    nx.draw(
        G, pos,
        node_color = cores,
        cmap = plt.cm.tab10,
        with_labels = True,
        node_size = 500,
        font_color = "black"
    )

    plt.title("Comunidades Detectadas")
    plt.show()

#para comparação de partições
def normaliza_grupos(rotulos):
    grupos = {}
    for no, rotulo in enumerate(rotulos):
        if rotulo not in grupos:
            grupos[rotulo] = []
        grupos[rotulo].append(no)

    grupos_imutaveis = frozenset(frozenset(g) for g in grupos.values())
    return grupos_imutaveis

def teste(G, MAXITE, n_exec=10):
    contagem = Counter()
    restultados = {}

    for _ in range(n_exec):
        rotulos = labelPropagation(G, MAXITE)
        grupos = normaliza_grupos(rotulos)
        contagem[grupos] += 1
        restultados[grupos] = rotulos 

    return contagem, restultados

def main():
    #np.random.seed(42)
    #print(sorted(G.nodes()))
    #rotulos = labelPropagation(G, MAXITE)
    #print(normaliza_grupos(rotulos))
    #plot(G, rotulos)
    contagem, resultados = teste(G, MAXITE)

    print("Partições encontradas:")
    for particao, frequencia in contagem.most_common():
        print(f"{frequencia}x a partição {particao}")
        plot(G, resultados[particao])

main()

