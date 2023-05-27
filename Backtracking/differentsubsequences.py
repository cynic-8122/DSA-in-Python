
def subsequenceCounting(t: str, s: str, lt: int, ls: int) -> int:
    ans = Helper(t, s, 0, 0)
    return ans

def Helper(t, s, i, j):
    print(f"i = {i}, j = {j}")
    if j >= len(s):
        return 1
    
    if i >= len(t):
        return 0
    
    tempans = 0
    while i < len(t):
        if t[i] == s[j]:
            tempans += Helper(t, s, i+1, j+1)

        i += 1
    
    print(f"tempans = {tempans}")    
    return tempans


t = str(input())
s = str(input())

print(subsequenceCounting(t, s, len(t), len(s)))