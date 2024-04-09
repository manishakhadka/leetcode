# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.





class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s=str(s)
        max_length = 0   
        seen = set()     
        left = 0         
        for right in range(len(s)):  # Iterate through each character of the string.
            while s[right] in seen:   
                seen.remove(s[left])  
                left += 1             # Move the left pointer to the right by 1.

            seen.add(s[right])        # Add the current character to the 'seen' set.
            max_length = max(max_length, right - left + 1) 

        return max_length  # Return the maximum length of the substring found.

s1= Solution() 

print(s1.lengthOfLongestSubstring('abcabcbb'))