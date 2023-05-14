import networkx as nx
import matplotlib.pyplot as plt

no_nodes = 0
no_edges = 0


# Parse data from the input file
with open('input.txt') as f:
    lines = f.readlines()
no_nodes, no_edges = lines[0].split(',')


# Initializing original network topology
G = nx.Graph()
for line in lines[1:]:
    src, dst, w = line.split(',')
    G.add_edge(src,dst,weight=int(w))

# Compute the forwarding table

print("Destination        Link")
for node in G.nodes:
    l = []
    if node != 'u':
        l = nx.dijkstra_path(G,'u',node,weight='weight')
        print("  " + node + "                "+ "(u, " + str(l[1]) + ")")


# visualize the Newtork topology
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show()