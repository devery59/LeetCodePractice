class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = current = 0
        p2 = len(nums) - 1

        while current <= p2:
            if nums[current] == 0:
                nums[p1], nums[current] = nums[current], nums[p1]
                p1 += 1
                current += 1

            elif nums[current] == 2:
                nums[current], nums[p2] = nums[p2], nums[current]
                p2 -= 1

            else:
                current += 1
