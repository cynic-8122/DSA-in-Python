def sumBase(n, k):
    ans = 0
    while n:
        ans = ans + n % k
        n //= k
    return ans

T = int(input("Number of testcases "))
n = int(input("Enter the number "))
for i in range(T):
    k = int(input("Enter the base "))
    print(sumBase(n, k))
