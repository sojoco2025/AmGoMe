#Given a non-negative integer num, return the maximum number, 
# which you can create by swapping any two digits of 
# the number only once. If no swaps can improve the number, return the original number.

# Examples

#    Example 1:
 #       Input: 2736
#        Expected Output: 7236
#        Justification: Swapping the first and second digits (2 and 7) results in the largest possible number.

#    Example 2:
#        Input: 9965
#        Expected Output: 9965
#        Justification: The number is already in its maximum form, so no swap is needed.

#    Example 3:
#        Input: 7281912
#        Expected Output: 9281712
#        Justification: Swapping the first digit (7) with the first 9 found from the left results in the maximum number.



class MaximumSwap:
    def maximumSwap(self, number):
        nums = list(str(number))
        bestPos = [0] * len(nums)
        largestPos = len(nums) - 1

        # Finding index of maximum digit after each digit
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] > nums[largestPos]:
                largestPos = idx
            bestPos[idx] = largestPos

        # Swapping first non-maximum digit
        for idx in range(len(nums)):
            if nums[idx] != nums[bestPos[idx]]:
                nums[idx], nums[bestPos[idx]] = nums[bestPos[idx]], nums[idx]
                break

        return int(''.join(nums))


# Testing the Solution with examples
solution = MaximumSwap()
print(solution.maximumSwap(2736))     # Output: 7236
print(solution.maximumSwap(9965))     # Output: 9965
print(solution.maximumSwap(7281912))  # Output: 9281712