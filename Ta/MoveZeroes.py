

# Given an array of integers nums, move all the 0s present in the array to the end
# while maintaining the relative order of the non-zero elements.

# Note: This rearrangement should be done in-place without using extra space for 
# another array.

# Input: [1, 0, 2, 0, 3, 0, 4]
#  Expected Output: [1, 2, 3, 4, 0, 0, 0]
#  Justification: Here, all non-zero elements (1, 2, 3, 4) retain their order, and all zeros are moved to the end of the array.


class MoveZeroes:
    def moveZeroes(self, nums):
        lastNonZeroIndex = 0  # Tracks the position for the next non-zero element

        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != 0:  # If the current element is non-zero
                # Swap with the element at lastNonZeroIndex
                nums[i], nums[lastNonZeroIndex] = nums[lastNonZeroIndex], nums[i]
                lastNonZeroIndex += 1
        return nums

if __name__ == "__main__":
    solution = MoveZeroes()

    # Test with different examples
    # Example 1
    example1 = [1, 0, 2, 0, 3, 0, 4]
    print(f"Example 1: {solution.moveZeroes(example1)}")

    # Example 2
    example2 = [0, 0, 0, 10, 20]
    print(f"Example 2: {solution.moveZeroes(example2)}")

    # Example 3
    example3 = [5, 1, 0, 2, 0]
    print(f"Example 3: {solution.moveZeroes(example3)}")



