#getTotalPage.py

"""
게시판 페이징하기
함수명: getTotalPage
입력값: 게시물 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
출력값: 총 페이지 수
계산: 총 페이지 수 = m /n + 1
"""

def getTotalPage(m, n):
    if m % n == 0:    #'%'는 나머지 연산자
        result = m / n
    else:
        result = m / n + 1
    return int(result)  #소수점 아래를 버릴 때 //연산자도 사용 가능

print(getTotalPage(5, 10))
print(getTotalPage(30, 10))

