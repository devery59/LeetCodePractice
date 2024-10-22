class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = list()
        interval = len(p)
        counter_p = Counter(p)
        counter_s = Counter(s[:interval])
        for i in range(len(s) - interval):
            if counter_s == counter_p:
                answer.append(i)
            counter_s[s[i]] -= 1
            counter_s[s[i + interval]] += 1
        if counter_s == counter_p:
                answer.append(len(s)-interval)
        return answer
