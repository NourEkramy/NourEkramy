if __name__ == '__main__':
    N = int(input())

sol=[]

for i in range(N):
    com=input().split()
    if com[0]=="insert":
        sol.insert(int(com[1]),int(com[2]))
    elif com[0]=="print":
        print(sol)
    elif com[0]=="remove":
        sol.remove(int(com[1]))
    elif com[0]=="append":
        sol.append(int(com[1]))
    elif com[0]=="pop":
        sol.pop()
    elif com[0]=="sort":
        sol.sort()
    elif com[0]=="reverse":
        sol.reverse()

