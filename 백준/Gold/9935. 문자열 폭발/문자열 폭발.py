word = input()
bomb = input()

stack = []

for i in word :
    stack.append(i)
    if ''.join(stack[-len(bomb):]) == bomb :
        del stack[-len(bomb):]

res = ''.join(stack)

if len(res) == 0 :
    print('FRULA')
else :
    for i in res :
        print(i, end='')