n = int(input())

decimals = {}
index = {}
arr = list(map(int, input().split()))
for i in range(n):
    a = arr[2*i]
    b = arr[2*i + 1]
    if b == 0:
        if a > 0:
            if 10000000000 in decimals:
                if decimals[10000000000][0] > a:
                    decimals[10000000000] = (a, 0)
            else:
                decimals[10000000000] = (a, 0)
        else:
            if -10000000000 in decimals:
                if decimals[-10000000000][0] < a:
                    decimals[-10000000000] = (a, 0)
            else:
                decimals[-10000000000] = (a, 0)

        continue
    decimal = a/b
    if decimal in decimals:
        x = decimals[decimal][0]
        y = decimals[decimal][1]
        if b*y < 0:
            if b > 0:
                A = a
                B = b
            else:
                A = x
                B = y
        else:
            if b < 0 and a < 0:

                if a > x:
                    A = a
                    B = b
                else:
                    A = a
                    B = b
            else:
                if a > 0:
                    if a < x:
                        A = a
                        B = b
                    else:
                        A = x
                        B = y
                else:

                    if a > x:
                        A = a
                        B = b
                    else:
                        A = x
                        B = y
    else:
        A = a
        B = b

    decimals[decimal] = (A, B)

decimalKeys = sorted(decimals)
print(len(decimalKeys))
for key in decimalKeys:
    print(*decimals[key], end=" ")
