class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums.pop(0)
        maxTotal = total
        for num in nums:
            if total < 0:
                total = 0
            total += num
            maxTotal = max(maxTotal, total)
        return maxTotal
            