# Author: fakhripm
# Problem: 118A - String Task

word = input().lower()
vowels = set('aeiouy')

result = []
for char in word:
    if char not in vowels:
        result.append('.' + char)

print(''.join(result))