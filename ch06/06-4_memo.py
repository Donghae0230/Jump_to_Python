#memo.py

"""
메모를 파일에 저장하고 추가 및 조회하는 기능 만들기
필요한 기능: 메모 추가 및 조회
입력값: 메모 내용, 프로그램 실행 옵션
출력값: memo.txt
"""

import sys

option = sys.argv[1] 

if option == '-a':  #option이 -a일 때 메모추가
    memo = sys.argv[2]
    f = open('memo.txt', 'a') #이전 내용이 지워지지 않도록 a로 작성
    f.write(memo)
    f.write('\n')
    f.close()

elif option == '-v':   #option이 -v일 때 메모출력
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
