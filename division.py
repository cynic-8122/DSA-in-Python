T = int(input())

for i in range(T) :
	K = int(input())
	A, B = [int(x) for x in input().split()]
    
	if B == 0 :
		i += 1
		continue
	div = str((A/B) - (A//B))
	ans = 0
	for j in range(2, K + 2) :
		ans += int(div[j])
            
	print(ans)