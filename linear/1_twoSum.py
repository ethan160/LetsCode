class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ''' range only include start point, not the end point'''
        for i in range (0, len(nums)):
            for j in range (i + 1, len(nums)) :
                if nums[j] == target - nums[i]:
                    return [i, j]

''' Time complexity: O(n^2) ; Space complexity: O(1) '''
