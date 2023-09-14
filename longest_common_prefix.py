'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        first_element = strs[0]
        for i in range(len(first_element)):
            for j in range(1,len(strs)):
                if first_element[i] != strs[j][i] or i >= len(strs[j]):
                    return output
            output += first_element[i]
        return output 