class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lst = []
        if len(matrix) == 1:
            return matrix[0]
        for item in matrix[0]:
            lst.append(item)
        return lst + self.spiralOrder([list(row) for row in zip(*matrix[1:])][::-1])