n = int(input("Nhap n: "))
sum = 0
while n > 0:
	reminder = (int)(n % 10)
	n /= 10
	sum += reminder
	print(sum)
print("Sum: ", sum)

print(23 % 10)