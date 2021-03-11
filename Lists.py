#List Comprehension Hacerrank


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    i = [count for count in range(x +1)]
    j = [count for count in range(y +1)]
    k = [count for count in range(z +1)]
    # print(i,j,k)

    
    ans = [[a,b,c] for a in i for b in j for c in k if  a + b + c != n]
    print(ans)

