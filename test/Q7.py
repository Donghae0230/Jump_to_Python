#Q7 한 줄 구구단 만들기


def multTable(n):
    result = []
    for i in range(1,10):
        result.append(i * n)
    return result
    
n = 2
print('%d 단: ' %n, multTable(n))
