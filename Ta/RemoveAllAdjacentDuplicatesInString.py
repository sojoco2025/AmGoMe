
# You are given a string s consisting of lowercase English letters. 
# A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made.



#    Input: s = "abccba"
#    Output: ""
#    Explanation: First, we remove "cc" to get "abba". Then, we remove "bb" to get "aa". Finally, we remove "aa" to get an empty string.

#    Input: s = "foobar"
#    Output: "fbar"
#    Explanation: We remove "oo" to get "fbar".

#    Input: s = "fooobar"
#    Output: "fobar"
#    Explanation: We remove the pair "oo" to get "fobar".

#    Input: s = "abcd"
#    Output: "abcd"
#    Explanation: No adjacent duplicates so no changes.



# Note: String s consists of lowercase English letters.
class RemoveAllAdjacentDuplicatesInString:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else: 
                stack.append(c)
        
        return ''.join(stack)
        


