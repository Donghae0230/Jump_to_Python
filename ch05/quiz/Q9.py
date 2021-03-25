#Q9.py
#입력값을 모두 더하는 스크립트

import sys

print(sys.argv)

l = sys.argv[1:]

print(l)

result = 0
for i in l:
    result += int(i)

print(result)
    
