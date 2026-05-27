
# You are given two strings pattern and text. 
# It is given that all characters of the pattern string are unique.

# Rearrange the characters of the text string based on the characters' 
# order in pattern string. In other words, if a character a occurs before 
# a character b in the pattern string, then a should occur before b in the output string.

# Characters in text that do not appear in pattern should be appended at the 
# end of the rearranged string in their original order.


# Example 1:

#    Input: pattern = "xy", text = "yyzx"
#    Expected Output: "xyyz"
#    Justification: In 'pattern', the order is 'x', 'y'. In the text, 'x' appears once, 
#    'y' twice, and 'z' doesn't appear. So, we put z at the end of the string. Thus, the
#     output string is xzyy.

# Example 2:

#    Input: pattern = "abc", text = "aabbcc"
#    Expected Output: "aabbcc"
#    Justification: Here, the 'text' already follows the order 'a', 'b', 'c' as specified in 'pattern', 
#    so the order remains 'aabbcc'.

#Example 3:

 #   Input: pattern = "mno", text = "onomon"
#    Expected Output: "mnnooo"
#    Justification: According to 'pattern', 'm' comes first, then 'n', then 'o'. 
#    Rearranging 'text' in this order results in 'm' once, 'n' twice, followed by 'o' 
#    thrice, hence 'mnnooo'.



class CustomSortString:
    def customSortString(self, order, value):
        # Counting frequency of each character in 'value'
        charCount = {}
        for letter in value:
            charCount[letter] = charCount.get(letter, 0) + 1

        # Building result string based on 'order'
        output = []
        for letter in order:
            if letter in charCount:
                output.append(letter * charCount.pop(letter))

        # Appending remaining characters in their original order
        for letter in value:
            if letter in charCount:
                output.append(letter)

        return ''.join(output)


if __name__ == "__main__":
    sorter = CustomSortString()

    print(sorter.customSortString("xy", "yyzx"))       # "xyyz"
    print(sorter.customSortString("abc", "aabbcc"))    # "aabbcc"
    print(sorter.customSortString("mno", "onomon"))    # "mnnooo"
