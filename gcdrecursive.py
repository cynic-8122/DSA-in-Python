
def HCF(a, b):
	if b == 0:
		return a 

	return HCF(b, a%b)

print(HCF(1904, 9997))