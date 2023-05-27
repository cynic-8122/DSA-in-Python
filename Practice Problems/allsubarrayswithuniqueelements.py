def sumoflength(arr,n):
        checkarr = [None]*n
        Hashmap = {}
        for i in range(n) :
            t = arr[i]
            if t in Hashmap.keys() :
                checkarr[i] = False
                
            else :
                checkarr[i] = True
                Hashmap[t] = 1
        
        ans  = 0
        count = 0
        i = 0
        while i < n:
            check = True
            t = checkarr[i]
            if t :
                count += 1
                
            else :
                check = False
                ans += (((count)*(count + 1)*(2*count + 1)//6) + (count)*(count + 1)//2)//2
                count = 1

            i += 1
        #print('count', count)
        if check :
            ans += (((count)*(count + 1)*(2*count + 1)//6) + (count)*(count + 1)//2)//2
            #print("ans", ans)
        return ans

arr = [int(x) for x in input().split()]
print(sumoflength(arr, len(arr)))