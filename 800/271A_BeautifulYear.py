# author : fakhripm
# problem : 271A - Beautiful Year

year = int(input())

while True:
    year += 1
    str_year = str(year)
    if len(set(str_year)) == 4:
        print(year)
        break