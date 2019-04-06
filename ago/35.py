class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j=0,len(nums)-1
        while i<=j:

            now=(i+j)//2
            if target==nums[now]:
                return now
            elif target>nums[now]:
                i=now+1

            else:
                j=now-1
        if i:
            return j+1
        else:
            return i