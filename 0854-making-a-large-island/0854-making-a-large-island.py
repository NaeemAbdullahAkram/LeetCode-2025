class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def explore_grid(r, c, index):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = index
            return (
                1
                + explore_grid(r - 1, c, index)
                + explore_grid(r, c + 1, index)
                + explore_grid(r + 1, c, index)
                + explore_grid(r, c - 1, index)
            )

        mp = {}
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    mp[index] = explore_grid(i, j, index)
                    index += 1

        if len(mp) == 0:
            return 1
        if len(mp) == 1:
            size = mp[2]
            return size if size == n**2 else size + 1

        mp[0] = 0
        ans = 0
        for i in range(n):
            for j in range(n):
                neighbours = set()
                length = 1
                if grid[i][j] == 0:
                    if i - 1 >= 0:
                        neighbours.add(grid[i - 1][j])
                    if j + 1 < n:
                        neighbours.add(grid[i][j + 1])
                    if i + 1 < n:
                        neighbours.add(grid[i + 1][j])
                    if j - 1 >= 0:
                        neighbours.add(grid[i][j - 1])
                    for nei in neighbours:
                        length += mp[nei]

                ans = max(ans, length)

        return ans