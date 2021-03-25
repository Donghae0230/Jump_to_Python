#multAdd.py

"""
3과 5의 배수 합하기
입력값: 1부터 999까지
출력값: 3의 배수와 5의 배수의 합
생각1: 3의 배수와 5의 배수 찾기
생각2: 3과 5의 배수가 중복되지 않도록 제외하기
"""

result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0: #or 연산자로 중복 제거
        result += n
    n += 1

print(result)
