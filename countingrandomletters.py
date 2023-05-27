a = input("Give your input ")

def countrandletters(b) :
	no_of_reps = 0
	for i in range(0, len(a)) :
		if a[i] == b :
			no_of_reps += 1
	return(no_of_reps)

b = input("The alphabet you want you check ")

if b != "" :
	x = countrandletters(b)
	print(a, b, x)

else :
	import string
	import random

	lower_upper_alphabet = string.ascii_letters
	random_letter = random.choice(lower_upper_alphabet)

	x = countrandletters(random_letter)
	print(a, random_letter, x)



