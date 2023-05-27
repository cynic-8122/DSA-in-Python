'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
'''
24
78506 
17111 
12994 
64729 
28272 
84248 
43911 
61883 
40257 
86835 
47827 
8676 
86583 
90580 
56384 
89261 
83176 
25005 
40376 
36473 
68037 
22027 
88546 
75271

19626
8555
3248
32364
883
5265
21955
30941
20128
43417
23913
1084
43291
11322
440
44630
5198
12502
2523
18236
34018
11013
22136
37635

'''
T = int(input())

for i in range(T):
    F = int(input())
    if F&1 :
        print(F>>1)

    else :
        a = bin(F)
        a = str(a)
        x = a[2:]
        print("x", x)
        l = len(x)
        count = 0
        check = True
        i = -1
        while i > -l + 1 :
            print("loop")

            if x[i] == "1" and check:
                check = False

            if not check:
                count  += 1

            i -= 1

        count -= 1
        print("count", count)
        if x[1] == "1":
            ans = (1<<(count + 2)) - 1

        else :
            ans = (1<<(count + 2)) - (1<<count)

        print(ans)
         

            

            