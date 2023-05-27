def longestPalinSubstring(string):
    ans = 0
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i] == string[j]:
            count = 2
            if i == j:
                count -= 1
                
            t1 = i+1
            t2 = j-1
            check = True
            while t1 <= t2:
                if t1 == t2:
                    count += 1
                    break
                    
                elif string[t1] == string[t2]:
                    count += 2
                    t1 += 1
                    t2 -= 1
                    
                else:
                    check = False
                    break
                    
            if check:
                ans = max(ans, count)
                break
                
            else:
                ans = max(ans, 1)

            i = t1
            j = t2
                
        elif i + 1 <= j and string[i + 1] == string[j]:
            i += 1
            
        elif j-1 >= i and string[i] == string[j-1]:
            j -= 1
            
        else:
            i += 1
            j -= 1
            
    return ans
            
                    
                    
string = str(input())
print(longestPalinSubstring(string))