# Given the root of the binary tree, return the 2D list containing the vertical order 
# traversal of the binary tree.

#A vertical order traversal of the tree is defined as a top to bottom, column by column traversal.

# Note: If two nodes are in the same row and column, keep its order from left to right.

# Example 1:

#    Input: A binary tree: [1,2,3,4,5,6,7]
#    Expected Output: [[4], [2], [1,5,6], [3], [7]]
#    Justification: Nodes 4, 2, 1 with 5 and 6, 3, and 7 are in separate vertical lines. 
#    The nodes in each vertical line are listed in the order they appear from top to bottom.

# Example 2:

#    Input: A binary tree: [3,9,8,4,0,1,7]
#    Expected Output: [[4], [9], [3,0,1], [8], [7]]
#    Justification: Nodes are grouped based on their vertical positions. 
#    Lower nodes in the same vertical line follow the higher ones.

# Example 3:

#    Input: A binary tree: [3,null,20,15,7]
#    Expected Output: [[3, 15], [20], [7]]
#    Justification: The tree is skewed to the right. 
#     The output reflects the vertical traversal from left to right.


from collections import deque, defaultdict

# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right


class BinaryTreeVerticalOrder:
    def verticalOrder(self, root):
        if not root:
            return []

        columns = defaultdict(list) # HashMap to hold column index and list of nodes
        nodesQueue = deque([(root, 0)])  # Queue for BFS, storing node and its column index
        leftMost = rightMost = 0

        while nodesQueue:
            currNode, colIndex = nodesQueue.popleft()

            if currNode:
                columns[colIndex].append(currNode.val) # Append node value to its column list
                leftMost = min(leftMost, colIndex)  # Update minimum column index
                rightMost = max(rightMost, colIndex) # Update maximum column index

                # Enqueue child nodes with updated column index
                nodesQueue.append((currNode.left, colIndex - 1))
                nodesQueue.append((currNode.right, colIndex + 1))

        # Compile the result from the columnTable
        return [columns[pos] for pos in range(leftMost, rightMost + 1)]


# Test cases
solution = BinaryTreeVerticalOrder()

# Test cases
solution = BinaryTreeVerticalOrder()

# Example 1
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(solution.verticalOrder(root1))

# Example 2
root2 = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
print(solution.verticalOrder(root2))

# Example 3
root3 = TreeNode(3, None, TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.verticalOrder(root3))







