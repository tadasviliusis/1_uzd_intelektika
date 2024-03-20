import networkx as nx
import matplotlib.pyplot as plt
import time


import matplotlib

matplotlib.use('TkAgg')

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'E': ['F'],
    'C': ['F'],
    'D': [],
    'F': []
}

G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G)  # Node positions for all nodes


def draw_graph(highlight_nodes=[], highlight_color='lightblue'):
    """
    Graph drawing
    """
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='k', node_size=700, font_size=20,
            font_weight='bold')
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color=highlight_color)
    plt.show(block=False)
    plt.pause(1)


def bfs_visual(graph, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        draw_graph(highlight_nodes=visited + [m], highlight_color='lightgreen')
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        time.sleep(1)  # Sleep to slow down the visualization for observation


def dfs_visual(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        draw_graph(highlight_nodes=visited, highlight_color='red')
        for neighbour in graph[node]:
            dfs_visual(graph, neighbour, visited)
        time.sleep(1)  # Sleep to slow down the visualization for observation



start_time = time.time()
print("Breadth-First Search Visualization:")
bfs_visual(graph, 'A')
bfs_execution_time = time.time() - start_time
print("\nBFS Execution Time with Visualization:", bfs_execution_time, "seconds")

plt.clf()


start_time = time.time()
print("\nDepth-First Search Visualization:")
dfs_visual(graph, 'A')
dfs_execution_time = time.time() - start_time
print("\nDFS Execution Time with Visualization:", dfs_execution_time, "seconds")
