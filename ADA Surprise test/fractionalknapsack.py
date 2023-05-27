class Entry:
	def __init__(self, value, weight, ratio):
		self.value = value
		self.weight = weight
		ratio = value/weight
		self.ratio = ratio

valuearr = [int(x) for x in input().split()]
weightarr = [int(x) for x in input().split()]
knapsackweight = int(input())
temparr = []

for i in range(len(valuearr)):
	weight = weightarr[i]
	value = valuearr[i]
	ratio = value/weight 
	t = Entry(value, weight, ratio)

	temparr.append(t)

temparr = sorted(temparr, key = lambda Entry:Entry.ratio, reverse = True)

# for x in temparr:
# 	print(x.value, x.weight, x.ratio)

currentweight = 0
i = 0
valuesofar = 0
while i < len(weightarr):
	if knapsackweight - currentweight >= temparr[i].weight :
		currentweight += temparr[i].weight
		valuesofar += temparr[i].value 
		i += 1

	else :
		requiredweight = knapsackweight - currentweight
		gainedvalue = requiredweight*(temparr[i].ratio)
		valuesofar += int(gainedvalue)
		break


print(valuesofar)








