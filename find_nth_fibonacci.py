

def fibo(n):
    memo = {}
    if n in memo:
        print("already:", memo[n])
        return memo[n]
    if n <=2:
        res = 1
    else:
        res = fibo(n-1) +fibo(n-2)
        memo[n] = res
        print("=> memo[n] ", memo[n] )
    return res




result = fibo(10)
print("finAL ->",result)