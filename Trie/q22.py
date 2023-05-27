from queue import Queue

def regenerate(S):
    s2 = 'cokubes'
    return minSwapsToMakeEqual(S, s2, len(S))

def minSwapsToMakeEqual(s1,  s2,  n):    
    if (s1 == s2):
        return 0    
    done = set()                  
    bfsQ = Queue(maxsize=10**5)   
    bfsQ.put([s1, 0, 0])
    done.add(s1)

    while (not bfsQ.empty()):
        node = bfsQ.get()
        cur = node[0]   
        i = node[1]   
        lvl = node[2] 
        for i in range(i, n):
            if(cur[i] != s2[i]):
                break
        

        optimal = False
        for j in range(i+1, n):

            if (cur[j] != s2[j] and cur[j] == s2[i] and cur[i] == s2[j]):
                cur = list(cur)
                cur[i], cur[j] = cur[j], cur[i]
                cur = ''.join(cur)
                if (cur == s2):
                    return lvl + 1

                if (cur not in done):
                    bfsQ.put([cur, i + 1, lvl + 1])
                    done.add(cur)

                optimal = True
                break

        if (optimal):
            continue
            
        for j in range(i+1, n):
            if (cur[j] != s2[j] and cur[j] == s2[i]):

                cur = list(cur)
                cur[i], cur[j] = cur[j], cur[i]
                cur = ''.join(cur)
                
                if (cur == s2):
                    return lvl + 1

                if (cur not in done):
                    bfsQ.put([cur, i + 1, lvl + 1])
                    done.add(cur)

                cur = list(cur)
                cur[i], cur[j] = cur[j], cur[i]
                cur = ''.join(cur)
        
    return n - 1