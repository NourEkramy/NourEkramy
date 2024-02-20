# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
book={}

for i in range(n):
    x, y = map(str, input().split())
    book[x]=y
    
for i in range(n):
    try:
        w=str(input())
        if w in book:
            print(w+'='+book[w])
        else:
            print("Not found")
    except EOFError:
        break
