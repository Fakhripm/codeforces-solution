# author : Fakhripm
# problem : Football
inp = input()
count = 1
found = False
for i in range(len(inp) - 1):
    if inp[i] == inp[i + 1]:
        count += 1
        if count >= 7 :
            print("YES")
            found = True
            break
    else :
        count = 1
if not found:
    print("NO")

'''
s = input()
print("YES" if "0000000" in s or "1111111" in s else "NO")
'''
