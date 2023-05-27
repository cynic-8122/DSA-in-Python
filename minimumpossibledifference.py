A = list(map(int, input().split()))

K = int(input())

m = max(A) - min(A)

if m % 2 == 0 and 2*K >= m :
	ans = 0

if m % 2 != 0 and 2*K >= m :
	ans = 1

else :
	ans = m - 2*K

print(ans)



