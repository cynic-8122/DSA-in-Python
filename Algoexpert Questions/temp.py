from typing import *



def minimizeIt(A: List[int], K: int) ->int:
    minval = float('inf')
    maxval = -float('inf')
    for i in range(len(A)):
        minval = min(minval, A[i])
        maxval = max(maxval, A[i])
    
    if maxval >= K :
    	amax = max(maxval - K, minval + K)
    	amin = min(minval + K, maxval - K)
    	for i in range(len(A)):
            t = A[i]
            if t > K and t - K >= amin :
                continue
                
            elif t + K <= amax :
                continue
                
            elif (t + K - amax) <= (amin - t + K):
                amax = t + K
                
            else :
                amin = t - K
                            
        
    else :
        ans = maxval - minval
        return ans
        

    ans = amax - amin
    return ans

A = [int(x) for x in input().split()]
K = int(input())

print(minimizeIt(A, K))
    
    
    
        
           
                
            
            
    

            
        
            
        
            


