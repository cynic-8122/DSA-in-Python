I = int(input())

X, A, B, C, D = [int(x) for x in input().split()]
P, Q, R, S, T, M = [int(x) for x in input().split()]

balance = X
cost1 = A 
cost2 = C
ans = 0
while balance > 0:
	if cost1 <= cost2 :
		balance -= cost1 
		cost1 += B
		
	else:
		balance -= cost2 
		cost2 += D

	if balance >= 0:
		ans += 1 

print(ans)

for i in range(I - 1):
	A = (A + (ans*T))%(M) + P
	B = (B + (ans*T))%(M) + Q
	C = (C + (ans*T))%(M) + R
	D = (D + (ans*T))%(M) + S
	#print(f"A = {A}, B = {B}, C = {C}, D = {D}")
	ans = 0
	balance = X
	cost1 = A 
	cost2 = C
	ans = 0
	while balance > 0:
		if cost1 <= cost2 :
			balance -= cost1
			cost1 += B 
		else:
			balance -= cost2
			cost2 += D

		if balance >= 0 :
			ans += 1 

	print(ans)