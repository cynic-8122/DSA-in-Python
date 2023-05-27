T = int(input())

for j in range(T) :			
	s = str(input())

	max_pal = 0
	pal_so_far = 1

	for i in range(len(s) - 1) :
		pal_so_far = 1
		#print("i", i)
		itr_right = i + 1
		itr_left = i - 1
		ans = pal_so_far
		if s[i] == s[itr_right] :
			itr_right += 1
			pal_so_far += 1
			ans = pal_so_far

		while (itr_right) < len(s) and (itr_left) >= 0 :
			#print(f"right = {s[itr_right]}, left = {s[itr_left]}")
			if s[itr_right] == s[itr_left] :
				pal_so_far += 2
				ans = pal_so_far

			else :
				pal_so_far = 1
				break
			itr_right += 1
			itr_left -= 1
		if ans > max_pal :
			substring = s[(itr_left + 1) : itr_right]
			#print(substring)
		max_pal = max(max_pal, ans)
		#print(max_pal)

	print(substring)
	print(max_pal)











