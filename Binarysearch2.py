
import sys
 
def findpos(x):
    print('1 ' + str(x))
    sys.stdout.flush()
    t = int(input())
    return t

def upperbound(low, high, x2):
    
    while low < high - 1:
        middle = (low+high)//2
        if findpos(middle) == x2:
            low = middle
        else:
            high = middle
    if findpos(high) == x2:
        return high
    else:
        return low

def lowerbound(low, high, x2):
    while low < high - 1:
        middle = (low+high)//2
        if findpos(middle) == x2:
            high = middle
        else:
            low = middle
    if findpos(low) == x2:
        return low
    else:
        return high
def count(n, x2):
    global cnt
    low = 0
    high = n-1
    
    middle = (low+high)//2
    val = findpos(middle)
    while low <= high:
        if val == x2:
            break
        elif val > x2:
            high = middle-1
        else:
            low = middle+1
        middle = (low+high)//2
        val = findpos(middle)
    
    if val != x2:
        print("value not found")
        return 0
    
    lower_Limit = lowerbound(low, middle, x2)
    

    upper_Limit = upperbound(middle, high, x2)
    
    return upper_Limit - lower_Limit + 1

 
n = int(input())
x = int(input())
 
print('2 ' + str(count(n, x)))

