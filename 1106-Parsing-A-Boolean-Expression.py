class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st=deque()
        for i in expression:
            if i==',' or i=='(':
                continue
            if i in ['t','f','!','&','|']:
                st.append(i)
            elif i==')':
                ht=False
                hf=False
                while st[-1] not in ['!','&','|']:
                    a=st.pop()
                    if a=='t':
                        ht=True
                    elif a=='f':
                        hf=True
                op=st.pop()
                if op=='!':
                    st.append('t' if not ht else 'f')
                elif op=='&':
                    st.append('f' if hf else 't')
                else:
                    st.append('t' if ht else 'f')
        return st[-1]=='t'