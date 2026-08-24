import networkx as nx
import numpy as np

# ================ CONSTANTES ================
MAXITE = 10
# ================ ---------- ================

G = nx.read_edgelist("rede1_duas_comunidades.csv", delimiter=',', nodetype=int)

#print(G.nodes())
#print(G)

def labelPropagation(G, MAXITE):
    n = G.number_of_nodes()
    rotulos = np.arange(n)

    iteracao = 0
    MUDOU = True

    for iteracao in range(MAXITE):
        if not MUDOU:
            break ## ou seja, não mudou
        MUDOU = False
        ordem_vertices = np.random.permutation(rotulos)
        print(ordem_vertices)
        for i in ordem_vertices:
            vizinhos = list(G.neighbors(i))

            if vizinhos is not None:
                print(vizinhos)

    print(n)
    print(rotulos)


def main():
    labelPropagation(G, MAXITE)

main()