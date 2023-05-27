n=int(input())
entry = {}
exit={}
ans=0
for i in range(0,n):
    x=input()
    if(x=="entry"):
        y=input()
        t = int(input())
        entry[y]=t
    else:
        y=input()
        t =int(input())
        exit[y]=t
for item in entry:
    g = exit[item]-entry[item]
    if(g%60!=0):
        g=(g//60)+1
    else:
        g=g//60
    if g>=1:
        ans+=60+(g-1)*30
print(ans)