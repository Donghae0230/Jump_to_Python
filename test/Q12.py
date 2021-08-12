#Q12 오류와 예외처리
#코드의 실행 결과를 예측하기

result = 0

try:
    [1, 2, 3][3]    #IndexError 에러 발생
    'a' + 1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:  # result는 3 -> finally로 이동
    result += 3
finally:            # result는 7
    result += 4

print(result)
