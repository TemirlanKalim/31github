class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.acuSum = [[0]*(n + 1) for _ in range(m + 1)]
        
        for r in range(m):
            prefix = 0
            for c in range(n):
                prefix += matrix[r][c]
                above = self.acuSum[r][c + 1]
                self.acuSum[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.acuSum[row2][col2]
        above = self.acuSum[row1 - 1][col2]
        left = self.acuSum[row2][col1 - 1]
        topLeft = self.acuSum[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
