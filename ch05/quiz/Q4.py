#Q4.py
#filter와 lambda로 리스트 음수 제거

l = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x: x>=0, l)))
