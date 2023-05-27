def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    Hashmap = {}
    for x in arr :
        Hashmap[x] = Hashmap.get(x, 0) + 1
    
    maxlen = 0
    for x in Hashmap.keys() :
        templen = 0
        t = x - 1
        while (t) in Hashmap.keys() and Hashmap[t]:
            
            templen += 1
            Hashmap[t] = 0
            t -= 1
        t = x + 1    
        while (t) in Hashmap.keys() and Hashmap[t]:
            Hashmap[t] = 0
            templen += 1
            t += 1
            
        templen += 1
        Hashmap[x] = 0
        maxlen = max(maxlen, templen)
        
    return maxlen
            
