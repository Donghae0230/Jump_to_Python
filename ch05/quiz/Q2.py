#Q2.py
#객체변수 value의 값을 100으로 제한

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        result = self.value
        
        if result > 100:
            self.value = 100
        
cal = MaxLimitCalculator()
cal.add(50)
cal.add(70)

print(cal.value)
