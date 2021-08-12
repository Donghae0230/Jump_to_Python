#Q5 피보나치 함수 만들기
#피보나치 수열: 첫 번째 항이 0, 두 번째 항이 1일 때 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))
