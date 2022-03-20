class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0;
        # Copy character by character into array
        for i in range(len(s)) :
            for j in range(i,len(s)):
                if s[j] in s[i:j]: 
                    break
                else:
                    maxLen = max(maxLen, j-i+1)
        return maxLen
    