while(1) :
    name, age, weight = input().split()
    if name == '#' and int(age) == 0 and int(weight) == 0 :
        break
    if (int(age) > 17 or int(weight) >= 80) :
        print(name, 'Senior')
    else :
        print(name, 'Junior')