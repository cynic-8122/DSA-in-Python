# cook your dish here
T = int(input())

for i in range(T) :
    N, X = [int(x) for x in input().split()]
    arr = [0] + [1]*N 
    barr = [0]*(N + 1)
    freq_map = {1:[]}
    for j in range(N - 1) :
        
        u, v = [int(x) for x in input().split()]
        
        if u in freq_map.keys() :
            freq_map[u].append(v) 
        else :
            freq_map[u] = [] 
        if v in freq_map.keys() :
            freq_map[v].append(u) 
        else :
            freq_map[v] = []
        
    for i in reversed(range(1, N + 1)) :
        if freq_map[i] == [] :
            barr[i] = 0
            
        else :
            for j in range(len(freq_map[i])) :
                barr[i] += barr[int(freq_map[i][j])]
            barr[i] += len(freq_map[i])
    
    
    count = 0
    i = 1
    ans = 1
    
    while count <= (N - 1) and i <= N:
        temp_hash = {}
        sarr = []
        for j in range(len(freq_map[i])) :
            if barr[freq_map[i][j]] in temp_hash.keys():
                temp_hash[barr[freq_map[i][j]]].append(freq_map[i][j])
            else :
                temp_hash[barr[freq_map[i][j]]] = [freq_map[i][j]]
                
            sarr.append(barr[freq_map[i][j]])
        
        print("arr[i]", arr[i])  
        sarr.sort()
        print("sarr", sarr)
        #print(sarr)
        print(barr)
        print(freq_map)
        print(temp_hash)
        #______________________________________________________________________________________________
        #print("temp_hash", temp_hash)
        #for j in range(0, len(sarr)) :
            ##print("j = ", j)
            #print("temp_hash", temp_hash[barr[freq_map[i][j]]])
            #for k in range(0, len(temp_hash[sarr[j]]) - j):
                #a = temp_hash[sarr[j]][k]
                #print(f"a = {a}")
                #print('arr', arr)
                #print(f"arr[a] before any change, {arr[a]}")
                #print('j + k', j + k)
                #arr[a] = arr[a]*(len(sarr) - (itr))
                #print(f"arr[a] after updating, {arr[a]}")
                #ans += arr[a]
        #itr += 1    
        count += len(freq_map[i])
        i += 1 
    #print(arr)
    #print(X*(sum(arr)))
   
    
    
        
        
    
        
        
        
        
        
