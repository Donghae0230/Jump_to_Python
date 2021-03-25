#Q11.py
#확장자가 .py인 파일만 출력하기

import glob
x = input("디렉터리 경로를 입력하세요: ")
print(glob.glob(x + "/" "*.py"))
