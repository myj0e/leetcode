#使用划窗方法解决
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tab={}
        Max=0
        index=0
        sub=""
        for i in s:
            if not i in sub:
                sub=sub+i
            else:
                Max=max(Max,len(sub))
                index=sub.find(i)
                sub=sub[index+1::]+i
        Max=max(Max,len(sub))
        return Max