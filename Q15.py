#Q15 Duplicate Numbers
'''
입력값: 0-9까지의 숫자
DupNum(): 입력값이 0-9의 모든 숫자를 각각 한 번씩 사용한 것인지 확인
'''

def DupNum(x):
    x = list(map(int,x))
    x.sort()
    y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if x == y:
        return True
    else:
        return False

x = input('숫자를 입력하세요: ')
result = DupNum(x)
print(result)
