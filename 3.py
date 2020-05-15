a = int(input('Enter a number: '))
n=1000000
ar = []
for i in range(n):
    if i%2 != 0:
        ar.append(i)
if a%2 == 0:
    a -= 1
    print('Output: {}'.format(ar[:a]))
else:
    print('Output: {}'.format(ar[:a]))