#file_readline

f = open("새파일.txt", 'r')
line = f.readline()
print(line)

"""
모든 줄을 읽고 싶은 경우
while True:
    line = f.readline()
    if not line: break
    print(line)
"""
    
f.close()
