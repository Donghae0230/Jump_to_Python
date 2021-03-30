#Q14 문자열 압축하기

def StrCompress(s):
    s = list(s)
    num = 1
    result = []
    x = list(range(0,len(s)))
    
    for i,c in enumerate(x): #for문에서 변수 2개를 사용하기 위해 enumerate 사용
        result.append(s[i])        
        if c < len(s)-1:
            if s[c] == s[c+1]:
                num += 1
            elif s[c] != s[c+1]:
                result.append(str(num)) #리스트에 문자열이 아닌 자료형이 있으면 에러 발생
                num = 1
    result.append(str(num))
    return ''.join(result)

s = input('문자를 입력하세요: ')
result = StrCompress(s)
print(result)
