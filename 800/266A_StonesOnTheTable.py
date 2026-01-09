# author : fakhripm
# problem : 266A - Stones on the Table

inp = int(input())
word = input()
count = 0
for i in range(inp - 1):
    char = word[i]
    if char == word[i + 1]:
        count += 1
    
print(count)