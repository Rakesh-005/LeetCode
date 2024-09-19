class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res=[]
        for i in range(len(expression)):
            op=expression[i]
            if op in '+-*':
                s1=self.diffWaysToCompute(expression[:i])
                s2=self.diffWaysToCompute(expression[i+1:])
                for i in s1:
                    for j in s2:
                        if op=='+':
                            res.append(int(i)+int(j))
                        elif op=='-':
                            res.append(int(i)-int(j))
                        elif op=='*':
                            res.append(int(i)*int(j))
        if len(res)==0:
            res.append(int(expression))
        return res