a = int(input())
nhuan = (a%400 == 0) or ((a%4 ==0) and not (a%100 == 0))
print(nhuan)
