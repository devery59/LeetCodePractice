class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {0: 0, 1: 0, 2: 0}
        for i in nums:
            counter[i] += 1
        idx = 0
        for key in [0, 1, 2]:
            for _ in range(counter[key]):
                nums[idx] = key
                idx += 1
