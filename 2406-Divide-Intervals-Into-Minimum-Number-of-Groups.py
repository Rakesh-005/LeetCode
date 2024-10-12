class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ':' '}
        j = 0
        s = ''
        l = 'abcdefghijklmnopqrstuvwxyz'
        for i in key:
            if i not in d:
                d[i] = l[j]
                j += 1
        for i in message:
            s += d[i]
        return s