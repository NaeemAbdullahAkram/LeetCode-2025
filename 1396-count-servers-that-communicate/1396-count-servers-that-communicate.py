class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [sum(row) for row in grid]
        col_count = [sum(col) for col in zip(*grid)]
        
        return sum(1 for i in range(m) for j in range(n) if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1))