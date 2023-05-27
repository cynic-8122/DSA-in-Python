#User function Template for python3
import bisect
def kthSmallest(mat, n, k):
    l = mat[0][0]
    r = mat[n-1][n-1]
    
    while l <= r:
        mid = (l+r)//2
        ans = checkcount(mat, n, k, mid)
        p = ispresent(mat, n, mid)
        print(mid, ans, p)
        if ans == 1 and p:
            return mid
            
        if ans == 0:
            r = mid-1
            
        else:
            l = mid+1
            
def checkcount(mat, n, k, val):
    i = 0
    j = n-1
    count1 = 0
    count2 = 0
    for x in range(n):
        ans1 = bisect.bisect_left(mat[x], val)
        t = bisect.bisect_right(mat[x], val)-1 
        count1 += ans1
        count2 += t
                
    if count1 <= k-1 and count2 > k-1:
        return 1

    if count1 > k-1:
        return 0
    
def ispresent(mat, n, val):
    i = 0
    j = n-1
    while i < n and j >= 0:
        if mat[i][j] == val:
            return True
            
        if mat[i][j] < val:
            i += 1
            
        else:
            j -= 1
            
    return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()




# } Driver Code Ends