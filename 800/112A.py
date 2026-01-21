# author : Fakhripm
# problem : PetyaAndString
inp1 = input()
inp2 = input()
found = False
for i in range(len(inp1)):
    if inp1[i].lower() == inp2[i].lower():
        continue
    elif inp1[i].lower() < inp2[i].lower():
        print("-1")
        found = True
        break
    else:
        print("1")
        found = True
        break

if not found:
    print("0")
