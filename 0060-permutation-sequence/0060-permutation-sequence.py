import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s=set()
        for i in range(1,n+1):
            s.add(str(i))
        glob=set()
        L=[]
        def recur(n,k):
            nonlocal L
            x=s-glob
            if k<=1:
                L.extend(list(sorted(x)))
                return
            if n==1:
                L.append(list(x)[0])
                return
            c=k//(math.factorial(n-1))
            if k%math.factorial(n-1)==0:
                c-=1
            print(sorted(list(x)))
            print(k)
            L.append(sorted(list(x))[c])
            glob.add(sorted(list(x))[c])
            recur(n-1,k-c*math.factorial(n-1))
            return 
        recur(n,k)
        return ''.join(L)
            

            