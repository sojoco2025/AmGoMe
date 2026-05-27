
# You are given two integers, lower and upper, specifying the inclusive range, 
# and the sorted array of unique integers nums, where each element is in between [lower, upper].

# We can say the number n is missing if n is not in the nums and falls in the range [lower, upper].

# Return the shortest sorted list of ranges that covers all missing numbers. 
# These ranges should fall within the inclusive bounds specified by the lower 
# and upper limit integers.

# Example 1:

# Input: nums = [3, 5, 10, 20], lower = 1, upper = 22
#   Expected Output: [[1, 2], [4, 4], [6, 9], [11, 19], [21, 22]]
#   Justification: The missing ranges are 1-2, 4, 6-9, 11-19, and 21-22. Each missing range is represented as a pair in the list, where both numbers are the same for a single missing number.


# Example 2:

#   Input: nums = [10, 20, 30, 40, 50], lower = 5, upper = 55
#   Expected Output: [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]
#   Justification: The missing ranges are 5-9, 11-19, 21-29, 31-39, 41-49, and 51-55. Each interval is represented as a pair of start and end values.


# Example 3:

#    Input: nums = [1, 3, 6, 10], lower = 0, upper = 12
#   Expected Output: [[0, 0], [2, 2], [4, 5], [7, 9], [11, 12]]
#   Justification: The missing ranges are 0, 2, 4-5, 7-9, and 11-12. Each range is represented as a start and end pair.



class MissingRanges:
    def findMissingRanges(self, nums, lower, upper):
        result = []
        prev = lower - 1  # Initialize previous element as lower-1

        # Iterate through the array and beyond to include upper bound
        for i in range(len(nums) + 1):
            # Handle last element case by setting it to upper+1
            curr = nums[i] if i < len(nums) else upper + 1

            # Check if there is a gap between prev and curr
            if prev + 1 <= curr - 1:
                result.append([prev + 1, curr - 1])  # Add the missing range to the result

            prev = curr  # Update prev for the next iteration

        return result

# Testing the solution with example cases
if __name__ == "__main__":
    solution = MissingRanges()
    examples_nums = [[3, 5, 10, 20], [10, 20, 30, 40, 50], [1, 3, 6, 10]]
    examples_lower = [1, 5, 0]
    examples_upper = [22, 55, 12]

    for nums, lower, upper in zip(examples_nums, examples_lower, examples_upper):
        print(f"Example: {solution.findMissingRanges(nums, lower, upper)}")



