#User function Template for python3

class Solution:
    def check(self, arr, idx, ans):
        leftans = 0
        rightans = 0
        for i in range(idx, -1, -1):
            leftans += 1/(ans-arr[i])
            
        for i in range(idx+1, len(arr)):
            rightans += 1/(arr[i] - ans)
            
        if leftans == rightans:
            return 0
            
        elif rightans > leftans:
            return -1
            
        
        return 1
            
            
    def Helper(self, arr, idx):
        l = float(arr[idx])
        r = float(arr[idx+1])
        ans = l
        while l < r:
            mid = (l+r)/2
            decide = self.check(arr, idx, mid)
            if decide == 0:
                return mid
                
            if decide > 0:
                ans = mid
                l += 0.001
                
            else:
                ans = mid
                r -= 0.001
                
        return ans
                
            
        
    def nullPoints(self, n, a, getAnswer):
        for i in range(n-1):
            t = self.Helper(a, i)
            getAnswer[i] = t
            
        return getAnswer
            
        # Your code goes here 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        getAnswer = [0]*n
        ob=Solution()
        ob.nullPoints(n, a, getAnswer)
        
        for i in range(0,n-1):
            print("{:.2f}".format(getAnswer[i]), end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends