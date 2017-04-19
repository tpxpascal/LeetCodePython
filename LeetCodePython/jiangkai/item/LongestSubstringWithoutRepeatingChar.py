# coding=utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        charList = list(s)
        longest = 0
        count = 0
        current = []
        for char in charList:
            if not char in current:
                current.append(char)
                count = count + 1
            else:
                if count > longest:
                    longest = count
                reindex = current.index(char)
                current = current[reindex + 1:]
                current.append(char)
                count = count - reindex
        if count > longest:
            longest = count
        return longest

if __name__ == '__main__':
    print "Module Test start."
    item = Solution()
    print item.lengthOfLongestSubstring("ababcaa")
    print item.lengthOfLongestSubstring("aabbccc")
    print item.lengthOfLongestSubstring("aaaaaabcd")
