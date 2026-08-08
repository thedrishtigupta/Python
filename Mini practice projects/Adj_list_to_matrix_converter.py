
def adjacency_list_to_matrix(adj_list):
    nodes = len(adj_list)

    matrix = [[0] * nodes for _ in range(nodes)]

    for node in range(nodes):
        for edge in adj_list[node]:
            matrix[node][edge] = 1

    for row in matrix:
        print(row)

    return matrix