#for loop: marks3.py

marks = [90, 25, 67, 45, 80]
number = 0
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))
    
