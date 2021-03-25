#except_IndexError.py
def test(a):
    try:
        print(a[3])    
    except IndexError as e:
        print(e)
