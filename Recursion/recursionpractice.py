def allpermutationsofstring(string):
	if len(string) == 0 :
		return 

	if len(string) == 1 :
		return string

	char = allpermutationsofstring(string[1:])
	 




