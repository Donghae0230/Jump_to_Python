def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return print(result/len(args))

avg_numbers(1,2,3)
