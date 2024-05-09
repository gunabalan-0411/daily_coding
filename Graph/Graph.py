from collections import defaultdict

def flatten_lists(nested_list):
    flattened_list = [item for sublist in nested_list for item in sublist]
    return flattened_list
# Unweighted and un directed graphs
def graph_linked_list(connections):
    graph = defaultdict(list)
    
    con_list = [con for con in connections.split('\n') if con != '']
    
    v, e = len(set(flatten_lists([con.split() for con in con_list]))), len(con_list)
    for i in range(e):
        u, v = map(str, con_list[i].split())
        graph[u].append(v)
        graph[v].append(u)

    for v in graph:
        print(v, graph[v])

def graph_adjacency_matrix(connections):
    con_list = [con for con in connections.split('\n') if con != '']
    v, e = len(set(flatten_lists([con.split() for con in con_list]))), len(con_list)
    print(v, e)
    matrix = [[0]* v for _ in range(v)]
    for i in range(e):
        u, v = map(str, con_list[i].split())
        u = ord(u) - ord('A')
        v = ord(v) - ord('A')
        matrix[u][v] = 1 # Undirected graphs
        matrix[v][u] = 1
    print(matrix)

# - graph_adjaceny_matrx_directed_weight
def graph_adjacency_matrix_weighted(weighted_connections):
    con_list = [con for con in weighted_connections.split('\n') if con != '']
    v, e = len(set(flatten_lists([con.split()[:-1] for con in con_list]))), len(con_list)
    adj_matrix = [[0]*v for _ in range(v)]

    for i in range(e):
        items = con_list[i].split()
        u = ord(items[0]) - ord('A')
        v = ord(items[1]) - ord('A')
        w = int(items[2])
        adj_matrix[u][v] = w
    
    for row in adj_matrix:
        print(row)

        

# ----------------------------- Testing
connections = '''
A B
A C
A F
C E
C F
C D
D E
D G
G F
'''
weighted_connections = '''
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
'''
# graph_linked_list(connections)
# graph_adjacency_matrix(connections)
graph_adjacency_matrix_weighted(weighted_connections)