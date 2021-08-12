#Q4 리스트 총합 구하기

A = [20,55,67,82,45,33,90,87,100,25]

result = 0
for i in A:
    if i >= 50:
        result += i
        
print(result)
