class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 1

        while fast < len(nums):
            if fast == slow or nums[fast] == 0:
                fast += 1
            elif nums[slow] == 0:
                nums[slow] = nums[fast]
                nums[fast] = 0
                slow += 1
            else:
                slow += 1