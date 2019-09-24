a = int(input())
c = input()
b = int(input())
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print (a*b)
elif c == '/':
    if b == 0:
        print('Деление на 0 невозможно!')
    else:
        print(a//b)
