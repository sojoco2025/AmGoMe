
# Given a string s, return true if any permutation of the given 
# string s can form a palindromic string. Otherwise, return false.

# A palindrome is a word, phrase, number, or other sequences of characters 
# that reads the same forward and backward (ignoring spaces, punctuation, 
# and capitalization).


# Example 1:
#         Input: "tactcoa"
#         Expected Output: true
#         Justification: The string can be rearranged to form "tacocat", which is a palindrome.


#     Example 2:
#         Input: "abcde"
#         Expected Output: false
#         Justification: There is no possible rearrangement of these characters that would result in a palindrome.

#     Example 3:
#         Input: "aabbccdd"
#         Expected Output: true
#         Justification: The string can be rearranged as "abcddcba", which is palindromes.



class PalindromePermutation:
    def canPermutePalindrome(self, s):
        # Dictionary to count occurrences of each character
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        # Count characters with odd occurrences
        odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)

        # Check if the odd count is not more than 1
        return odd_count <= 1

    # Main method for testing
    def main(self):
        print(self.canPermutePalindrome("tactcoa"))  # true
        print(self.canPermutePalindrome("abcde"))    # false
        print(self.canPermutePalindrome("aabbccdd")) # true

# Creating an instance of the Solution class and calling the main method
PalindromePermutation().main()




