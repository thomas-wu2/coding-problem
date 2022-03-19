class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {}
        sb = ""
        maxLen = 0;
        
        # Copy character by character into array
        for i in range(len(s)) :
            
            c = s[i]
            if (c in charMap) :
                
                if (len(sb) > maxLen):
                    maxLen = len(sb)
                index = sb.find(c)
                sb = sb[index+1:]
                sb+=c
            else :
                sb+=c
                charMap[c]=1

                if (len(sb) > maxLen):
                    maxLen = len(sb)
        return maxLen
