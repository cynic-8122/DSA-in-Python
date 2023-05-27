import sys
 
def start(m):
    print('1 ' + str(m))
    sys.stdout.flush()
    r = int(input())
    if r == 0:
        return False
    elif r == 1:
        return True
    exit()
 
def memorylimit():
    l = 1
    r = 1000000000-1
    while l < r-1:
        mid = (l+r)//2
        if start(mid):
            
            low = mid
        else:
            high = mid



    if start(high):
        return high
    else:
        return low


def main():
    global cnt
    cnt = 0
    global L
    for L in reversed(range(1, 1000000000)):
        calcL = memorylimit()
        if L == calcL and cnt<=31:
            print("For L:", L,"\n***** Success *****")
        else:
            print("Unsuccessfull at", L)
            print("Given L:", L, "\t\tCalculated L", calcL, "\t\tTries", cnt)
            break
        cnt = 0
        l  = mid
        else:
            r = mid
    if start(r):
        return r
    else:
        return l
 
print("2 " + str(memorylimit()))
>>>>>>> 76559b57d8482c966d6b36dddcfb7cb2eb53f629
