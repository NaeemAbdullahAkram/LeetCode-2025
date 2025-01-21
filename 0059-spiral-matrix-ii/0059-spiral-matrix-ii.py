class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for _ in range(n)] for _ in range(n)]
        top, bottom, left, right = 0, n, 0, n
        gena = (i for i in range(1, n ** 2 + 1))
        while left < right:
            for i in range(left, right):
                matrix[top][i] = next(gena)
                if n % 2 == 1 and bottom - top == 1:
                    break
            for i in range(top + 1, bottom):
                matrix[i][right - 1] = next(gena)
            for i in range(right - 2, left - 1, -1):
                matrix[bottom - 1][i] = next(gena)
                if n % 2 == 0 and bottom - top == 2:
                    break
            for i in range(bottom - 2, top, -1):
                matrix[i][left] = next(gena)
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return matrix