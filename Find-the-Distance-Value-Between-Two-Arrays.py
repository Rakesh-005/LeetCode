class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n,m=len(arr1),len(arr2)
        a=0
        for i in arr1:
            found=False
            for j in arr2:
                dist=abs(i-j)
                if dist<=d:
                    found=True
                    break
            if found==False:
                a+=1
        return a