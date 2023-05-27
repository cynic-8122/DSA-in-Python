a = int(input())

b = int(input())

c = a^b
c = bin(c)
c = str(c[2:])
count = 0
for "1" in c :
	count += 1

print(count)
