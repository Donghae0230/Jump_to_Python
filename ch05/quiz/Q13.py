#Q13
#random 모듈로 숫자 생성하기

import random

x = 0
num = []
while x < 6:
    y = random.randint(1,45)
    if y not in num:
        num.append(y)
    x += 1

        
print(num)
