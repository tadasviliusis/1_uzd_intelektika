import matplotlib
import networkx as nx
import time
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


maze1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'E': ['F'],
    'C': ['F'],
    'D': [],
    'F': []
}

maze2 = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'G'],
    'F': ['D'],
    'G': ['E']
}

maze3 = {
    '1': ['2', '4'],
    '2': ['1', '3', '5'],
    '3': ['2', '6'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'],
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['5', '7', '9'],
    '9': ['6', '8']
}

def generate_graph_from_maze(maze):
    G = nx.Graph()
    for node, neighbors in maze.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G

def draw_graph_with_path(ax, G, path, pos, title="Graph"):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', edge_color='k', ax=ax)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='lightgreen', ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=2, ax=ax)
    ax.set_title(title)
    plt.pause(0.5)

def update_graph_with_path(G, visited, pos, title="Graph"):

    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='lightgreen')
    nx.draw_networkx_labels(G, pos)
    plt.title(title)
    plt.draw()
    plt.pause(0.5)


def bfs_path(graph, start, ax, G, pos):
    visited = [start]
    queue = [start]
    draw_graph_with_path(ax, G, visited, pos, f"BFS Visiting: {start}")

    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                draw_graph_with_path(ax, G, visited, pos, f"BFS Visiting: {neighbour}")


def dfs_path(graph, start, ax, G, pos, visited=None):
    if visited is None:
        visited = [start]
    else:
        visited.append(start)

    draw_graph_with_path(ax, G, visited, pos, f"DFS Visiting: {start}")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs_path(graph, neighbour, ax, G, pos, visited)



for i, (maze_name, maze) in enumerate([('maze1', maze1), ('maze2', maze2), ('maze3', maze3)], start=1):
    print(f"Performance for {maze_name}:")
    G = generate_graph_from_maze(maze)
    pos = nx.spring_layout(G)

    # Create a new figure for each maze
    fig, ax = plt.subplots(figsize=(8, 8))

    start_counter = time.perf_counter()
    bfs_path(maze, next(iter(maze)), ax, G, pos)
    bfs_duration = time.perf_counter() - start_counter
    print(f"BFS took {bfs_duration:.5f} seconds.")

    start_counter = time.perf_counter()
    dfs_path(maze, next(iter(maze)), ax, G, pos)
    dfs_duration = time.perf_counter() - start_counter
    print(f"DFS took {dfs_duration:.5f} seconds.")

    plt.close(fig)


plt.show()
