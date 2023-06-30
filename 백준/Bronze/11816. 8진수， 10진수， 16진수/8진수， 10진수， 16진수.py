X = input()
X_list = list(X)

if X_list[0] == '0' :
    if X_list[0] == '0' and X_list[1] == 'x' :
        print(int(X, 16))
    else :
        print(int(X, 8))
else :
    print(int(X))