N, R = [int(x)for x in input().split()]

queries = []
for i in range(R):
	arr = [int(x) for x in input().split()]
	queries.append(arr)


def merge(list1, list2) :
    arr = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        a = list1[i][0]
        b = list2[j][0]
        if a <= b :
            arr.append(list1[i])
            i += 1

        else :
            arr.append(list2[j])
            j += 1
    if j >= len(list2) :
        while i < len(list1) :
            arr.append(list1[i])
            i += 1

    else :
        while j < len(list2) :
            arr.append(list2[j])
            j += 1

    return arr 



def sort_function(list1, left, right) :
        
    if left == right :
        return [list1[left]]

    mid = (left + right)//2
    x = sort_function(list1, left, mid)
    y = sort_function(list1, mid+1, right)
    output = merge(x, y)
    return output



def arrayManipulation(n, queries):
    queries = sort_function(queries, 0, len(queries)-1)
    i = 0
    max_value_so_far = queries[0][2]
    ans = max_value_so_far
    while i < len(queries) - 1:
        max_value_update = max(max_value_so_far, queries[i + 1][2])
        j = i
        x = queries[i][1]
        check = False
        temp_ans = 0
        if queries[i][1] >= queries[i + 1][0] :
        	check = True
        	temp_ans = queries[i][2]

        while j < len(queries) - 1:
            if x >= queries[j + 1][0] and check:
                temp_ans += queries[j + 1][2]
                j += 1
            else:
                break

        ans = max(ans, temp_ans, max_value_update)
        i = j + 1

    return ans

print(arrayManipulation(N, queries))

			

