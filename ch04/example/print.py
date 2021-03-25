#print

#큰따옴표(")로 둘러싸인 문자열은 +연산과 동일하다.
print("큰따옴표(\")로 둘러싸인 문자열은 +연산과 동일하다.")
print("Life""is""too short")
print("Life"+"is"+"too short\n")

#문자열 띄어쓰기는 콤마로 한다.
print("문자열 띄어쓰기는 콤마로 한다.")
print("Life","is","too short\n")

#한 줄에 결괏값을 출력할 땐 매개변수 end를 사용한다.
print("한 줄에 결괏값을 출력할 땐 매개변수 end를 사용한다.")
for i in range(10):
    print(i, end='')
