class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s, pair, score):
            stack = []
            sc = 0
            for char in s:
                if stack and stack[-1] + char == pair:
                    stack.pop()
                    sc += score
                else:
                    stack.append(char)
            return ''.join(stack), sc

        sc = 0
        if x >= y:
            s, score = remove_pairs(s, 'ab', x)
            sc += score
            s, score = remove_pairs(s, 'ba', y)
            sc += score
        else:
            s, score = remove_pairs(s, 'ba', y)
            sc += score
            s, score = remove_pairs(s, 'ab', x)
            sc += score

        return sc