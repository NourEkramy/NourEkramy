if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
arr.sort()

if (arr.count(arr[-1]))>1:
    x=arr.count(arr[-1])
    while x>1:
        del arr[-1]
        x-=1

print(arr[-2])
