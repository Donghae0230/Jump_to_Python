#except_ExceptionClass.py

class MyError(Exception):
    pass

#별명을 출력하는 함수 작성
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
