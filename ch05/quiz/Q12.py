#Q12
#time 모듈로 날짜와 시간 출력하기

import time
print(time.strftime('%x' + ' ' + '%X', time.localtime(time.time())))
