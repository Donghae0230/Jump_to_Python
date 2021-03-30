#Q11 모듈 사용 방법
#C:\Users\이동해\python-git\test 디렉터리에 mymod.py 모듈이 있을 때 cmd에서 모듈 사용하는 방법 모두 기술하기

'''
1) 모듈이 있는 test 디렉터리로 이동해서 사용하기
    1. #C:\Users\이동해\python-git\test 디렉터리로 이동
    2. python 명령어로 파이썬 셸 실행
    3. import mymod 명령어로 모듈 사용

2) sys.path.append(모듈 저장 경로) 사용하기
    1. 파이썬 셸 실행
    2. import sys 명령어로 sys 모듈 사용
    3. sys.path.append() 명령어로 모듈 디렉터리 경로 추가
    4. import mymod 명령어로 모듈 사용


3) PATHONPATH 환경 변수 사용하기
    1. set PYTHONPATH 명령어로 모듈 디렉터리 경로 입력
    2. 파이썬 셸 실행
    3. import mymod 명령어로 모듈 사용

    
