class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ll = len(nums)
        maxi = 0
        for i in range(ll):
            if i > maxi:
                return False
                break
            else:
                maxi = max(maxi, i + nums[i])
        else:
            return True
s=Solution()
print(s.canJump([2,3,1,1,4]))