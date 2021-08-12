#Q16 모스 부호 해독

morseCode = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}
list_val = list(morseCode.values())
list_key = list(morseCode.keys())

def MorseCode(x):
    list_x = x.split(' ')
    for i in range(0, len(list_x)):
        for j in range(0, len(list_val)):
            if list_x[i] == list_val[j]:
                list_x[i] = list_key[j]
        if list_x[i] == '':
            list_x[i] = ' '
    return ''.join(list_x)

x = input('모스부호를 입력하세요: ')
result = MorseCode(x)
print(result)
