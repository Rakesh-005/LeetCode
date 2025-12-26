1class Solution:
2    def bestClosingTime(self, customers: str) -> int:
3        # Start with closing at hour 0 and assume the current penalty is 0.
4        minPenalty = 0
5        curPenalty = 0
6        earliestHour = 0
7
8        for i in range(len(customers)):
9            ch = customers[i]
10
11            # If status in hour i is 'Y', moving it to open hours decrement
12            # penalty by 1. Otherwise, moving 'N' to open hours increment
13            # penatly by 1.
14            if ch == "Y":
15                curPenalty -= 1
16            else:
17                curPenalty += 1
18
19            # Update earliestHour if a smaller penatly is encountered.
20            if curPenalty < minPenalty:
21                earliestHour = i + 1
22                minPenalty = curPenalty
23
24        return earliestHour