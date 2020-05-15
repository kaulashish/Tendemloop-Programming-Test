def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a = float(input('Enter first number : '))
b = float(input('Enter second number: '))
op = str(input('Enter type of operation : (add, sub, mul, div)'))
if op == 'add' or op =='sub' or op == 'mul' or op =='div':
    if op =='add':
        print('{} + {} = {}'.format(a,b,add(a,b)))
    elif op =='sub':
        print('{} - {} = {}'.format(a,b,sub(a,b)))
    elif op =='mul':
        print('{} * {} = {}'.format(a,b,mul(a,b)))
    elif op =='div':
        print('{} / {} = {}'.format(a,b,div(a,b)))
else:
    print('Invalid operator.')


