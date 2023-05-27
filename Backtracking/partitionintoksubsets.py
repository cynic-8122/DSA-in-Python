#User function Template for python3
import sys
sys.setrecursionlimit(10000000)
class Solution:
    def isKPartitionPossible(self, a, k):
        Hashmap = {}
        for x in a:
            Hashmap[x] = Hashmap.get(x, 0) + 1
            

        s = sum(a)
        if s%k:
            return False
        
        if k == 1 or len(a) == 1:
            return True
            
        target = s//k
        temparr = [0 for i in range(k)]
        n = len(a)
        return self.Helper(a, k, n, temparr, target, 0, k, 0)
        
    def Helper(self, a, k, n, temparr, target, i, zerocount, tcount):
        if i >= n:
            if zerocount == 0 and tcount == k:
                return True
            

            return False
            
        check = True
        for t in range(k):
            if temparr[t]:
                temparr[t] += a[i]
                if temparr[t] == target:
                    tcount += 1
                ans = self.Helper(a, k, n, temparr, target, i+1, zerocount, tount)
                if ans == True:
                    return True
                    
                else:
                    if temparr[t] == target:
                        tcount -= 1
                    temparr[t] -= a[i]
                    
            elif check:
                zerocount -= 1
                check = True
                temparr[t] += a[i]
                if temparr[t] == target:
                    tcount += 1
                ans = self.Helper(a, k, n, temparr, target, i+1, zerocount, tcount)
                if ans == True:
                    return True
                    
                else:
                    if temparr[t] == target:
                        tcount -= 1
                    temparr[t] -= a[i]
                    zerocount += 1
                    
            
        return False
        
        
            
            
            
        
        

#{ 
#  Driver Code Starts


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())
        if Solution().isKPartitionPossible(arr, k):
            print(1)
        else:
            print(0)
# } Driver Code Ends