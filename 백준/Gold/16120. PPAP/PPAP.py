import sys
ppap = list(sys.stdin.readline().rstrip())

stack = []

for i in ppap :
    stack.append(i)
    if stack[-4:] == ['P', 'P', 'A', 'P'] :
        stack.pop()
        stack.pop()
        stack.pop()

if stack == ['P'] :
    print("PPAP")
else :
    print("NP")
