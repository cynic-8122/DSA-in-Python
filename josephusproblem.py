n, k = [int(x) for x in input().split()]

def game_of_death(n, k, t) :
	if n == 0 :
		return t
	if 