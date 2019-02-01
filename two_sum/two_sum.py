class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
 
        d={}
        for i in range(0,len(nums)):
            d[target-nums[i]]=i
        for i in range(0,len(nums)):
            if nums[i] in d.keys() and d[nums[i]]!=i:
                return [i,d[nums[i]]]
