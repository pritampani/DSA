def max_subset_value(N, A):
    def count_distinct_elements(x1, y1, size):
        elements = set()
        for i in range(x1, x1 + size):
            for j in range(y1, y1 + size):
                elements.add(A[i][j])
        return len(elements)
    
    # Initialize dp array where dp[i] is the maximum value considering first i rows
    dp = [0] * (N + 1)
    
    # Iterate through each row as the starting row
    for i in range(N):
        # Update dp[i+1] to be at least dp[i] (no new sub-grid)
        dp[i + 1] = max(dp[i + 1], dp[i])
        # Iterate through each possible square size
        for size in range(1, N - i + 1):
            for j in range(N - size + 1):
                distinct_count = count_distinct_elements(i, j, size)
                # Calculate the ending row index
                end_row = i + size
                if end_row <= N:
                    dp[end_row] = max(dp[end_row], dp[i] + distinct_count)
    
    return dp[N]

# Example usage:
N = 3
A = [
    [1, 2, 1],
    [2, 3, 1],
    [1, 1, 1]
]
print(max_subset_value(N, A))  # Expected Output: 4