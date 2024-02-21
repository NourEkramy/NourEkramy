n=int(input())
sol=0
mx=0
for i in range(n):
    leave,coming = map(int, input().split())
    sol-=leave
    sol+=coming
    if mx<sol:
        mx=sol

print (mx)
