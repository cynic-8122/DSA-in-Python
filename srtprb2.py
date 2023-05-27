def requiredmatches(arr):
    if len(arr) == 2:

        if arr[0] != arr[1]:
            return 1
        else:
            return 0

    half = len(arr)//2

    left_required_matches = requiredmatches(arr[:half])
    right_required_matches = requiredmatches(arr[half:])

    matches1 = set(arr[:half])
    matches2 = set(arr[half:])

    if (matches1 & matches2):
        return left_required_matches+right_required_matches
    else:
        return left_required_matches+right_required_matches + 1


n = int(input())

arr = list(map(int, input().split()))


print(requiredmatches(arr))