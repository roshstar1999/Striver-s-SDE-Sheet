class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        i=0
        m=len(a)
        n=len(a[0])
        while i<m :
            if target>=a[i][0] and target<=a[i][n-1]:
                for j in range(n):
                    if a[i][j]== target:
                        return True
                return False
            i+=1
        return False
