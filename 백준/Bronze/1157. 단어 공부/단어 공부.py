word = input()
word = list(word.upper())
set_word = list(set(word))

count = []

for i in range(len(set_word)) :
    count.append(word.count(set_word[i])) 

max_count = max(count)

if count.count(max_count) != 1 :
    print("?")
else :
    print(set_word[count.index(max_count)])