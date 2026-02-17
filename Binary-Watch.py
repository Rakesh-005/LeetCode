1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        output = []
4        # Loop through all possible combinations of hours and minutes and count the number of set bits
5        for h in range(12):
6            for m in range(60):
7                if bin(h).count('1') + bin(m).count('1') == turnedOn:  # Check if the number of set bits in hours and minutes equals the target number
8                    output.append(f"{h}:{m:02d}")  # Add the valid combination of hours and minutes to the output list
9        return output