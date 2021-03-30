#Q9 텍스트 파일의 숫자 총합과 평균값 구하기

f = open("sample.txt", 'r')
lines = f.readlines()
f.close()

sum = 0
for i in lines:
    i.replace('\n','')
    sum += int(i)

avg = sum / len(lines)

f = open("sample.txt", 'a')
f.write("sum: %d\n" %sum)
f.write("avg: %d\n" %avg)
f.close()


