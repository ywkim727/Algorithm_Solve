string = list(input())

count = 0

for i in string :
    if i == " " :
        count += 1

if string[0] == " " :
    if string[-1] == " ":
        print(count-1)
    else :
        print(count)
else :
    if string[-1] == " " :
        print(count)
    else :
        print(count+1)




