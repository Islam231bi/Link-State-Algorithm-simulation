import networkx as nx
import matplotlib.pyplot as plt

no_nodes = 0
no_edges = 0

least_cost_paths = [[]]


# Dijkstra function
def dijkstra_path(graph, src, dst, weight):
    # Create a dictionary to store the shortest distances
    distances = {node: float('inf') for node in graph.nodes}
    distances[src] = 0

    # Create a dictionary to store the previous node in the shortest path
    previous = {node: None for node in graph.nodes}

    # Create a set to store visited nodes
    visited = set()

    # Dijkstra's algorithm
    while len(visited) < len(graph.nodes):
        # Find the node with the minimum distance
        min_dist_node = None
        for node in graph.nodes:
            if node not in visited and (min_dist_node is None or distances[node] < distances[min_dist_node]):
                min_dist_node = node

        # If the destination node is reached, break the loop
        if min_dist_node == dst:
            break

        # Add the current node to the visited set
        visited.add(min_dist_node)

        # Update the distances and previous nodes of neighboring nodes
        for neighbor in graph.neighbors(min_dist_node):
            if neighbor in visited:
                continue
            new_distance = distances[min_dist_node] + graph.edges[min_dist_node, neighbor][weight]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = min_dist_node

    # Construct the shortest path from source to destination
    path = []
    current_node = dst
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous[current_node]

    return path


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
            l = dijkstra_path(G,n,node,weight='weight')
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