# author : fakhripm
# problem : 41A - Translation

word1 = input()
word2 = input()

if len(word1) != len(word2):
    print("NO")
    exit()

for i in range(len(word1)):
    if word1[len(word1)-1-i] != word2[i]:
        print("NO")
        break
else:
    print("YES")

# string slicing
'''
if word1[::-1] == word2:
    print("YES")
else:
    print("NO")
'''