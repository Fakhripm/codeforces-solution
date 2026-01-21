# Problem : Chewbaсca and final

n = list(input())
final = 0
for i in range(len(n)) :
    number = int(n[i])
    if (number > 4 and i != 0) or (4 < number < 9):
        final = final * 10 + (9 - number)
    else :
        final = final * 10 + number
    
print(final)