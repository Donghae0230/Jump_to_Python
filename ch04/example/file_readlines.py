#file_readlines

f = open("새파일.txt", 'r')
lines = f.readlines()
print(lines)

for line in lines:
    print(line)
    
f.close()
