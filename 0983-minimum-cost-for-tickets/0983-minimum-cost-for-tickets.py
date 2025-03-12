class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        index = 0

        for day in range(1, last_day + 1):
            if index >= len(days) or day < days[index]:
                dp[day] = dp[day - 1]
            else:
                index += 1

                one_day = dp[day - 1] + costs[0]
                seven_day = dp[max(0, day - 7)] + costs[1]
                thirty_day = dp[max(0, day - 30)] + costs[2]

                dp[day] = min(one_day, seven_day, thirty_day)
        return dp[last_day]
