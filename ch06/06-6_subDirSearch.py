#subDirSearch.py
#특정 디렉터리에서 부터 그 하위 모든 파일 중 파이썬 파일(*.py)만 출력하기

import os

def search(dirname):
    filenames = os.listdir(dirname) #os.listdir()로 해당 디렉터리의 파일을 리스트로 만듬
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) #디렉터리를 포함한 전체 경로
        ext = os.path.splitext(full_filename)[-1] #os.path.splitext()는 파일 이름을 확장자 기준으로 나눔
        if ext == '.py':
            print(full_filename)
            
search('C:/Users/이동해/python-git/ch06/')
