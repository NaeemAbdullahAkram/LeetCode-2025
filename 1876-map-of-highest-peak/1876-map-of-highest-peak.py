class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        que = deque()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    isWater[i][j] = -1
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < len(isWater) and 0 <= y < len(isWater[0]) and isWater[x][y] == 0:
                            que.append((x, y))

        height = 1
        while que:
            for _ in range(len(que)):
                x, y = que.popleft()
                if isWater[x][y] == 0:
                    isWater[x][y] = height
                    for dx, dy in directions:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < len(isWater) and 0 <= new_y < len(isWater[0]) and isWater[new_x][new_y] == 0:
                            que.append((new_x, new_y))
            height += 1

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == -1:
                    isWater[i][j] = 0

        return isWater