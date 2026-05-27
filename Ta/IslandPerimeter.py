
# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). 
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# There are no lakes on the island, so the water inside the island is not connected to 
# the water around it. A cell is a square with a side length of 1.

# The given matrix has only one island, write a function to find the perimeter of that island.



class IslandPerimeter:
    def findIslandPerimeter(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # only if the cell is a land and not visited
                if (matrix[i][j] == 1 and not visited[i][j]):
                    return self.is_land_perimeter_DFS(matrix, visited, i, j)

        return 0


    def is_land_perimeter_DFS(self, matrix,  visited, x,  y):
        if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
            return 1  # returning 1, since this a boundary cell initiated this DFS call

        if (matrix[x][y] == 0):
            return 1  # returning 1, because of the shared side b/w a water and a land cell

        if (visited[x][y]):
            return 0  # we have already taken care of this cell

        visited[x][y] = True  # mark the cell visited

        edgeCount = 0
        # recursively visit all neighboring cells (horizontally & vertically)
        edgeCount += self.is_land_perimeter_DFS(matrix, visited, x + 1, y)  # lower cell
        edgeCount += self.is_land_perimeter_DFS(matrix, visited, x - 1, y)  # upper cell
        edgeCount += self.is_land_perimeter_DFS(matrix, visited, x, y + 1)  # right cell
        edgeCount += self.is_land_perimeter_DFS(matrix, visited, x, y - 1)  # left cell

        return edgeCount


def main():
    sol = Solution()
    print(sol.findIslandPerimeter([[1, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0]]))

    print(sol.findIslandPerimeter([[0, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 1, 0, 0],
                            [0, 1, 1, 0],
                            [0, 1, 0, 0]]))


main()





