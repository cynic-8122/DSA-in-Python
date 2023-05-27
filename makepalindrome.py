# cook your dish here
def word_count(S, start, end) :
    output = {}
    for i in range(start, end + 1 ) :
        if S[i] in output :
            output[S[i]] += 1 
        else :
            output[S[i]] = 1 
    
    return output
    
T = int(input())
for i in range(T) :
    cost = 0
    S, P = input().split()
    P = int(P)
    P -= 1 
    a = word_count(S, P + 1, len(S) - 1)
    b = word_count(S, 0, P - 1 )
    for x in a.keys() :
        if x not in b.keys() :
            cost += a[x]
        elif x in b.keys() :
            cost += abs(a[x] - b[x])

    for y in b.keys() :
        if y not in a.keys() :
            cost += b[y]
        
    print(cost)   
    
    