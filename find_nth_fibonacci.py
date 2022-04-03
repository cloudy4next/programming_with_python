

# def fibo(n):
#     memo = {}
#     if n in memo:
#         print("already:", memo[n])
#         return memo[n]
#     if n <=2:
#         res = 1
#     else:
#         res = fibo(n-1) +fibo(n-2)
#         memo[n] = res
#         print("=> memo[n] ", memo[n] )
#     return res




# result = fibo(10)
# print("finAL ->",result)

def getNthFib(n):
    if n<= 0:
        print("Incorrect input")
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)

print(getNthFib(10))

 
# def getNthFib(n):
#     if n<= 0:
#         print("Incorrect input")
#     # First Fibonacci number is 0
#     elif n == 1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 2:
#         return 1
#     else:
#         return getNthFib(n-1)+getNthFib(n-2)
 
# # Driver Program
 
# print(getNthFib(10))