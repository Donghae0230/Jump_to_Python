#multTable.py

"""
구구단 프로그램 만들기
함수 이름짓기: GuGu
입력값 정하기: 2
출력값 정하기: 2단(2, 4, 6,···,18)
결과 저장할 변수 자료형 정하기: 리스트
"""

def GuGu(n):
    result = []

    i = 1
    while(i<10):
        result.append(n*i)
        i += 1
        
    return str(result)

i = 1
while (i<10):
    print("%d단 :%s" %(i, GuGu(i)))
    i += 1
