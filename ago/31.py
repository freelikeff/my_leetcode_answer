class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            pass
        elif nums[-2] < nums[-1]:
            nums[-2], nums[-1] = nums[-1], nums[-2]

        else:
            for i in range(len(nums) - 2, 0, -1):

                if nums[i] > nums[i - 1]:
                    for j in range(len(nums) - 1, i - 1, -1):
                        if nums[j] > nums[i - 1]:
                            nums[i - 1], nums[j] = nums[j], nums[i - 1]
                            for k in range(i, (i + len(nums)) // 2):
                                nums[k], nums[len(nums) - 1 - k + i] = nums[len(nums) - 1 - k + i], nums[k]
                            break
                    break



            else:
                for i in range(0, len(nums) // 2):
                    nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]