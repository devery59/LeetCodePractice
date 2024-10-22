class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        interval = len(p)
        counter_p = Counter(p)
        counter_s = Counter(s[: interval - 1])

        for i in range(interval - 1, len(s)):
            counter_s[s[i]] += 1

            if counter_s == counter_p:
                answer.append(i - interval + 1)

            counter_s[s[i - interval + 1]] -= 1

            if counter_s[s[i - interval + 1]] == 0:
                del counter_s[s[i - interval + 1]]

        return answer
