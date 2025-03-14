class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        answer = []
        counter = {}
        for i in range(len(A)):
            count = 0
            counter[A[i]] = counter.get(A[i], 0) + 1
            counter[B[i]] = counter.get(B[i], 0) + 1
            count += sum(1 for value in counter.values() if value == 2)
            answer.append(count)

        return answer
