class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        answer = [0 for _ in range(n)]
        frequency = [0 for _ in range(n + 1)]
        count = 0

        for current_index in range(n):
            frequency[A[current_index]] += 1
            if frequency[A[current_index]] == 2:
                count += 1

            frequency[B[current_index]] += 1
            if frequency[B[current_index]] == 2:
                count += 1

            answer[current_index] = count

        return answer
