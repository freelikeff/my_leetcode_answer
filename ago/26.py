class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        j = 1
        maxn = nums[0]
        for i in range(0, len(nums)):
            if nums[i] != maxn:
                maxn = nums[i]

                nums[j] = maxn
                j += 1
        return j
