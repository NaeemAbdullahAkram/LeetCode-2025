class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def traversePond(r, c) -> int:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            
            total = grid[r][c]
            grid[r][c] = 0
            for direction in directions:
                nextR, nextC = direction[0] + r, direction[1] + c
                total += traversePond(nextR, nextC)
            return total
        
        maxPond = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    maxPond = max(maxPond, traversePond(r, c))
        return maxPond