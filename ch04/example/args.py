#여러 개의 입력값 받기
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result_add = add_mul('add', 1,2,3,4,5)
result_mul = add_mul('mul', 1,2,3,4,5)

print(result_add)
print(result_mul)
