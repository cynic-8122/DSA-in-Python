# cook your dish here
def HCF(a, b):
    if a == 0 :
        return b
    c = a + b 
    b = min(a, b)
    a = c - b
    return HCF(a%b, b)

T = int(input())

for i in range(T) :
    k = int(input())
    ans = 0
    for j in range(1, 2*(k)+ 1):
        A_i = k + j*j 
        A_j = 2*j + 1 
        ans += HCF(A_i, A_j)
    print(ans)   