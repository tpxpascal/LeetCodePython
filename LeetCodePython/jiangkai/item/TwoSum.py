# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numList = range(len(nums))
        for i in numList:
            for j in numList[i + 1:]:
                if (nums[i] + nums[j] == target):
                    return [i, j]

if __name__ == '__main__':
    print "Module Test start."
    item = Solution();
    print item.twoSum([1, 2, 3], 4)
    print item.twoSum([1, 2, 3], 3)
    print item.twoSum([1, 2, 3], 5)
