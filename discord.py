t = int(input(""))
for i in range(t):
    s = input(" ")
    x = s.split()
    d = int(x[0])
    c = int(x[1])
    l = int(x[2])
    if 4 * d + 4 * c == l:
        print("yes")
    elif d > c:
        for i in range(c + 1):
            if 4 * d + 4 * (c - i) == l:
                print("yes")
                break
        else:
            print("no")
    elif c > d:
        for i in range(d ):
            if 4 * d + 4 * (c - i) == l:
                print("yes")
                break
        else:
            print("no")
    elif c==d:
        for i in range (c+1):
           if 4 * d + 4 * (c - i) == l:
                print("yes")
                break
        else:
            print("no")
    
