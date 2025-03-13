class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        max_beauty = items[0][1]
        for i in range(len(items)):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty

        return [self.binary_search(items, q) for q in queries]

    def binary_search(self, items, target_price):
        left, right = 0, len(items) - 1
        max_beauty = 0
        while left <= right:
            mid = (left + right) // 2
            if items[mid][0] > target_price:
                right = mid - 1
            else:
                max_beauty = max(max_beauty, items[mid][1])
                left = mid + 1
        return max_beauty
