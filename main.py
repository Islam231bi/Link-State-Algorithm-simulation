import networkx as nx
import matplotlib.pyplot as plt

no_nodes = 0
no_edges = 0

least_cost_paths = [[]]


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
for n in G.nodes:
    print("Forwarding table for node "+ n)
    print("Destination        Link")
    for node in G.nodes:
        l = []
        if node != n:
            l = nx.dijkstra_path(G,n,node,weight='weight')
            print("  " + node + "                "+ "("+str(n)+", " + str(l[1]) + ")")
            if node == 'u':
                least_cost_paths.append(l)
    print("\n")


# Compute least cost path plot
G2 = nx.Graph()

for l in least_cost_paths:
    for i in range(len(l)-1):
        G2.add_edge(l[i],l[i+1])


# visualize the Newtork topology
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Visualize Least cost path graph
pos = nx.spring_layout(G2)
nx.draw(G2, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
plt.show()