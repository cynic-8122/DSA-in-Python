N, H, x = input().split()

N = int(N)
H = int(H)
x = int(x)

arr = list(map(int, input().split()))

check = True
for i in range(len(arr)) :
	if arr[i] >= (H - x) :
		print("YES")
		check = False
		break

if check :
	print("NO")







