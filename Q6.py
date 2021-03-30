#Q6 입력받은 숫자의 총합 구하기

import sys

x = sys.argv[1]
x = x.split(',')    #콤마를 기준으로 숫자 구분

result = 0
for i in x:
    result += int(i)
    
print(result)
