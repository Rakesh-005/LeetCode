class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        i=0
        r=[]
        while i<len(folder):
            j=i+1
            r.append(folder[i])
            while j<len(folder) and folder[j].startswith(r[-1]+'/'):
                j+=1
            i=j
        return r