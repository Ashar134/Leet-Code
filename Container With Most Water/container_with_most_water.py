class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:

            mass = min(height[left], height[right]) * (right - left)
            result = max(result, mass)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
