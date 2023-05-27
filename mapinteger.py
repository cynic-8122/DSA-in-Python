n = int(input())

intersections = {}
vertical = set()
horizontal = set()
for i in range(n):
    start, end, name, direction = input().split()
    if start in intersections:
        intersections[start][0].add(name)
        intersections[start][1] +=1
        if direction == 'E' or direction == 'W':
            intersections[start][2][1] = True
        else:
            intersections[start][2][0] = True
    else:
        intersections[start] = [{name}, 1, [False, False]]
        if direction == 'E' or direction == 'W':
            intersections[start][2][1] = True
        else:
            intersections[start][2][0] = True
    if end in intersections:
        intersections[end][0].add(name)
        intersections[end][1] += 1
        if direction == 'E' or direction == 'W':
            intersections[end][2][1] = True
        else:
            intersections[end][2][0] = True
    else:
        intersections[end] = [{name}, 1, [False, False]]
        if direction == 'E' or direction == 'W':
            intersections[end][2][1] = True
        else:
            intersections[end][2][0] = True
    
count = 0
for intersection in intersections:
    if len(intersections[intersection][0]) == 2 and intersections[intersection][1] == 4 and intersections[intersection][2][0] and intersections[intersection][2][1]:
        count+=1
print(count)
