N = int(input())
arr = [int(x) for x in input().split()]
a = sum(arr)
Q = int(input())
Q_arr = [int(x) for x in input().split()]

i = 1
while i <= Q :
	ans = a<<(i)
	print(ans)
	i += 1

    