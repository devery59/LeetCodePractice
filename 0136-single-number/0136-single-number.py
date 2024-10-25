class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter_nums = Counter(nums)
        for i in counter_nums:
            if counter_nums[i] == 1:
                return i
