def count_length_of_cycle(arr, start_index):
    def dfs(curr, count, visited):
        if curr in visited:
            return count - visited[curr]
        visited[curr] = count
        return dfs(arr[curr], count + 1, visited)

    visited = {}
    result = dfs(start_index, 0, visited)
    return result if result > 0 else -1

# Example test cases
print(count_length_of_cycle([1, 0], 0))   # Output should be 2
print(count_length_of_cycle([1, 2, 0], 2))   # Out

# https://chatgpt.com/c/ed453ffb-b858-4b98-a14f-e739fdf5ad44