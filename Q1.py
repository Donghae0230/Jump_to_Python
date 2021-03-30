#Q1 a:b:c:d를 a#b#c#d로 바꾸기

x = 'a:b:c:d'

result = '#'.join(x.split(':'))
print(result)

