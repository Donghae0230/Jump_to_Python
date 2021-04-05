#Q18 문자열 검색
#코드의 결괏값 예측하기

import re
p = re.compile("[a-z]+")    #a부터 z까지 1회 이상 반복
m = p.search("5 python")
print(m.start() + m.end()) #m.start()는 0, m.end()는 7 

