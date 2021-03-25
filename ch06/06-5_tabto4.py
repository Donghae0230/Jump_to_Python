#tabto4.py

'''
문서 파일 안에 있는 탭(tab)을 공백(space) 4개로 바꾸기
필요한 기능: 파일 읽기, 문자열 변경하기
입력값: 탭을 포함하는 문서(src)
출력값: 탭이 공백으로 수정된 문서(dst)
'''

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read() #읽은 내용을 변수 tab_content에 저장
f.close()

space_content  = tab_content.replace("\t", " "*4)

f = open(dst, 'w')  #b.txt 생성
f.write(space_content)
f.close()

