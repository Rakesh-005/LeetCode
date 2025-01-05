class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_effect = [0] * (n + 1)  # Extra space to handle range shifts

        # Apply the shifts to the shift_effect array
        for a, b, c in shifts:
            if c == 1:  # Right shift
                shift_effect[a] += 1
                shift_effect[b + 1] -= 1
            else:  # Left shift
                shift_effect[a] -= 1
                shift_effect[b + 1] += 1

        # Compute the cumulative shifts
        for i in range(1, n):
            shift_effect[i] += shift_effect[i - 1]

        # Apply the shifts to the string
        result = []
        for i in range(n):
            net_shift = shift_effect[i] % 26  # Ensure the shift is within bounds
            new_char = chr((ord(s[i]) - ord('a') + net_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)
