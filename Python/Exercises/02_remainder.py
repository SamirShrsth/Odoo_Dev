num = 238
sum = 0
for i in range(len(str(num))):
    sum += num % 10
    num = num // 10
print(sum)
    
    