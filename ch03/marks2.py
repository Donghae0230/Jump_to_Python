#for loop: marks2.py

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60: continue #불합격인 경우
    print("%d번 학생 축하합니다. 합격입니다." %number)
    
