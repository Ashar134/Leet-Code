class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        index_lookup = {} 

        for i in range(len(nums)):

            number = target - nums[i]

            if number in index_lookup:
                return [index_lookup[number], i]
                
            index_lookup[nums[i]] = i

        return []
