import sys

sys.setrecursionlimit(20)

def fun(i = 0):
	print(i)

	return fun(i+1)

fun()