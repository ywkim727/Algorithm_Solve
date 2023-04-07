a = int(input())
b = int(input())

c = int(b/100)
d = int((b-(c*100))/10)
e = int(b-(c*100 + d*10))

print(a*e)
print(a*d)
print(a*c)
print(a*b)