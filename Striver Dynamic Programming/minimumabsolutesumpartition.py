
def Helper(arr, n, totalsum, dp, sumsofar):
    if n < 1:
        return abs((totalsum - 2*sumsofar))
    
    p = int(sumsofar) + int(arr[n-1])
    if dp[n-1][p] != -1:
        t = dp[n-1][p]
    
    else:
        t = Helper(arr, n-1, totalsum, sumsofar+arr[n-1])
        dp[n-1][p] = t
    
    if dp[n-1][sumsofar] != -1:
        nt = dp[n-1][sumsofar]
                   
    else:
        nt = Helper(arr, n-1, totalsum, sumsofar) 
    
    return min(t, nt)