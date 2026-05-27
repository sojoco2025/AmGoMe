
# You are given an array heights of size n, representing the heights of n buildings.

# The ocean is to the right of these buildings. A building has an ocean view 
# if there are no taller buildings to its right.

# The task is to find the indices(0-based) of all such buildings with an ocean view.


# Example 1:

#    Input: [4, 3, 2, 1]
#    Expected Output: [0, 1, 2, 3]
#    Justification: Each building is shorter than the one to its left, hence all have an ocean view.

# Example 2:

#    Input: [2, 3, 1, 4]
#    Expected Output: [3]
#    Justification: Building at index 3 is the only one without taller buildings to their right.

# Example 3:

#    Input: [7, 4, 3, 2, 1, 4, 6, 3]
#    Expected Output: [0, 6, 7]
#    Justification: Buildings at indices 0, 6, and 7 are the only ones without taller buildings to their right.




class BuildingsWithAnOceanView:
    def findBuildings(self, heights):
        result = []  # List to store indices of buildings with ocean views
        maxHeight = 0  # Maximum height seen so far

        # Iterate from right to left
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxHeight:
                result.append(i)  # Append index if building has ocean view
                maxHeight = heights[i]  # Update the maximum height

        return result[::-1]  # Reverse to maintain original order

if __name__ == "__main__":
    solution = BuildingsWithAnOceanView()

    # Test cases
    heights1 = [4, 3, 2, 1]
    print("Example 1:", solution.findBuildings(heights1))

    heights2 = [2, 3, 1, 4]
    print("Example 2:", solution.findBuildings(heights2))

    heights3 = [7, 4, 3, 2, 1, 4, 6, 3]
    print("Example 3:", solution.findBuildings(heights3))
















