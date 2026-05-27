class toeplitz:
    def isToeplitzMatrix(self, matrix):
        if matrix is None or len(matrix) == 0:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False

        return True
    
    def main():
        s = Solution()

    matrix1 = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]

    matrix2 = [
        [1, 2],
        [2, 2]
    ]

    print("Matrix 1:")
    print(s.isToeplitzMatrix(matrix1))   # True

    print("Matrix 2:")
    print(s.isToeplitzMatrix(matrix2))   # False
    
        
