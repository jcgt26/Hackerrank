if __name__=="__main__":
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(list(arr), reverse=True)


if(2 <= n <= 10 ):
    count = 0
    done = False
    temp = arr[0]
    ans = 0
    for x in arr:
        if(x < temp):
            ans = x
            break
    print(ans)
    
