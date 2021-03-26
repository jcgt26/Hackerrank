def average(array):
    new_array = set(array)
    ans = sum(new_array)/ len(new_array)
    return ans


if __name__=='__main__':
    #print(set("Hallo Welt")) #Basically, sets are used for membership testing and eliminating duplicate entries.
    #print(set([0,4,8,1,8])) #Eliminates duplicate
    n = int(input())
    arr = list(map(int, input().split()))

    if(n == len(arr)):
        ans = average(arr)
        print(ans)
    else:2
        pass

