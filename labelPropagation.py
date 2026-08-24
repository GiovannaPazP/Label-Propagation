import networkx as nx

G = nx.read_edgelist("rede1_duas_comunidades.csv", delimiter=',')

print(G.nodes())
print(G)