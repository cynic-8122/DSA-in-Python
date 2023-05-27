# cook your dish here
T = int(input())

for i in range(T) :
    N, M = [int(x) for x in input().split()]
    count = 0 
    for j in range(2, N + 1) :
        for i in range(1, j):
            if (M % i) == ((M % j)%i) :
                count += 1
                print(f"({i}, {j})") 
                
    
    print(count)
            