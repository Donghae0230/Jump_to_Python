#Q13 DashInsert 함수 만들기

def DashInsert(x):
    result = []
    for i in range(0,len(x)-1):
        result.append(x[i])

        if int(x[i])%2 == 0 and int(x[i+1])%2 == 0: #짝수가 연속되면 두 수 사이 * 추가
            result.append('*')
        
        elif int(x[i])%2 == 1 and int(x[i+1])%2 == 1: #홀수가 연속되면 두 수 사이 - 추가
            result.append('-')

        elif x[i+1] == False:
            pass
    result.append(x[-1])
    return ''.join(result)
            
x = input('숫자를 입력하세요: ')
result = DashInsert(x)
print(result)
