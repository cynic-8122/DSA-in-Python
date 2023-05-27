string = str(input())

stack = []
count = 0
flag = True
for i in range(len(string)):
	char = string[i]
	if char == '(':
		count += 1
		stack.append(char)

	if char == ')':
		if len(stack) == 0:
			

		else:
			stack.pop()


if flag:
	if len(stack) == 0:
		print(1)

	else:
		print(0)



