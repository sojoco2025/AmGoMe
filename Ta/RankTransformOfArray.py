
# Given an array arr containing integers, replace each element with its rank in the array.

# The rank is determined based on the size of the element compared to others in the array.
#     Smaller numbers get a lower rank, and equal numbers share the same rank.
#     The ranking starts from 1.

#  Example 1:

#      Input: [10, 20, 20, 30]
#      Expected Output: [1, 2, 2, 3]
#      Justification: 10 is the smallest, so its rank is 1. 20, occurring twice, shares the rank 2. 30, being the largest, gets the rank 3.


#  Example 2:

#      Input: [100, 2, 70, 2]
#      Expected Output: [3, 1, 2, 1]
#      Justification: 2, being the smallest, is ranked 1. 70 is next, so it's ranked 2. 100, the largest, is ranked 3.

#  Example 3:

#      Input: [5, 5, 5, 5]
#      Expected Output: [1, 1, 1, 1]
#      Justification: All elements are the same, so they all share the same rank, 1.






class RankTransformOfArray:
    # Function to transform the array into its rank form
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(set(arr)) # Sorting the unique elements of the array
        rank_dict = {v: i + 1 for i, v in enumerate(sorted_arr)} # Assigning ranks
        return [rank_dict[x] for x in arr] # Replacing elements with ranks

    # Main method for testing examples
    def main(self):
        examples = [
            [10, 20, 20, 30],
            [100, 2, 70, 2],
            [5, 5, 5, 5]
        ]
        for example in examples:
            print("Input:", example)
            print("Output:", self.arrayRankTransform(example))
            print("")

solution = RankTransformOfArray()
solution.main()  # Testing the Python solution with the example inputs




