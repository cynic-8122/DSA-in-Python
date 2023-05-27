
def countnumberofways(n):
	if n == 0 :
		return 1

	if n == 1:
		return 1

	if n == 2 :
		return 2

	return countnumberofways(n-1) + countnumberofways(n-2) + countnumberofways(n-3)

n = int(input())
print(countnumberofways(n))