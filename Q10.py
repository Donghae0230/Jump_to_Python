#Q10 클래스로 계산기 만들기
#조건: 리스트를 받아서 합계와 평균을 계산할 수 있어야 함

class Calculator:
    def setdata(self, data):
        self.data = data
        print(self.data)

    def sum(self):
        sum = 0
        for i in self.data:
            sum += i
        return sum

    def avg(self):
        sum = 0
        for i in self.data:
            sum += i
        avg = sum / len(self.data)
        return avg
    
cal1 = Calculator()
cal1.setdata([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator()
cal2.setdata([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())
