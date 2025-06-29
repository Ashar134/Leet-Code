class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_red = 0
        count_white = 0
        count_blue = 0
        length = len(nums)


        for i in range(length):

            if nums[i] == 0:
                count_red += 1

            elif nums[i] == 1:
                count_white += 1
                
            else:
                count_blue += 1
        
        for i in range(count_red):
            nums[i] = 0

        for i in range(count_red, count_red + count_white):
            nums[i] = 1

        for i in range(count_red + count_white, length):
            nums[i] = 2
