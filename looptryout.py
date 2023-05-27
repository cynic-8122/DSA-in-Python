i = 0
j = 0
k = 0
	
while i < len(ins) and k < len(wlarr) :

	a = wlarr[k]
		
	if ins[i] < (a + j) :
	
		wlarr[k] += 1
		i += 1


	else :
	
		j += a 
		k += 1
		i += 1