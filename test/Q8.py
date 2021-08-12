#Q8 파일 내용 역순으로 저장하기

f = open("abc.txt", 'r')
lines = f.readlines()
f.close()

lines.reverse()
newLines = ''
for i in lines:
    newLines += i

f = open("abc.txt", 'w')
f.write(newLines)
f.close()

