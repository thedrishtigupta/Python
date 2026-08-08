

def dfs(matrix, start_node):
    stack = [start_node]
    visited = set()
    result = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        result.append(current)

        for neighbor in range(len(matrix[current])):
            if matrix[current][neighbor] == 1 and neighbor not in visited:
                stack.append(neighbor)

    return result