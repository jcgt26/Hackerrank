import time



def f(y):
    for x in range(y):
        ans = x

    return ans

if __name__=="__main__":
    tic = time.time()
    f(10000000)
    toc = time.time()
    print(toc - tic)
    # 42.0462589263916