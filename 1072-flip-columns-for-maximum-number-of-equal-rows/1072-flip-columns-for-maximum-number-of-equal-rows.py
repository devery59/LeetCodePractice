class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        answer = 0

        for current_row in matrix:
            flipped_row = [1-x for x in current_row]
            identical_row_count = 0
            for compare_row in matrix:
                if compare_row == current_row or compare_row == flipped_row:
                    identical_row_count +=1
            answer = max(answer, identical_row_count)

        return answer
