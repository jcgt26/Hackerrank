


if __name__ == '__main__':
    m = int(input())
    mset = set(list(map(int, input().split())))
    n = int(input())
    nset = set(list(map(int, input().split())))
    diff_m = mset.difference(nset)
    diff_n = nset.difference(mset)
    ans = {*diff_m, *diff_n}
    [print(item) for item in sorted(ans)]