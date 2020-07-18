def solve(tu,eden):
    tu=list(tu)
    op=0
    for l in eden:
        c=0
        for j in tu:
            if j in l:
                break
            else:
                c=c+1
        if c==len(tu):
            op=op+1
    return op

n,k=map(int,input().split())
eden=[]
for i in range(n-1):
    eden.append(map(int,input().split()))
tu=map(int,input().split())
y=solve(tu,eden)
print(y)
