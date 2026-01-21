# author : Fakhripm
# problem : HQ9+
str = input()
printed = False
for char in str :
    if char == 'Q' or char == 'H' or char == '9' :
        print("YES")
        printed = True
        break
if not printed :
    print("NO")
