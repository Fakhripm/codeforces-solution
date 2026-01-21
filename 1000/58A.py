# author : Fakhripm
# problem : ChatRoom
word = input()
h_exist = False
e_exist = False
l_exist = 0
o_exist = False
for i in range(len(word)) :
    if word[i] == 'h' :
        h_exist = True
    if word[i] == 'e' and h_exist :
        e_exist = True
    if word[i] == 'l' and e_exist:
        l_exist+= 1
    if word[i] == 'o' and l_exist >= 2:
        o_exist = True

if (o_exist) :
    print("YES")
else :
    print("NO")
