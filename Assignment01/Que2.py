num1 = int(input("Enter num1: "))
temp = num1
i = 1
rev = 0
while i <= 4:
    rem  = int(num1%10)
    num1 = num1/10
    i = i + 1
    rev = rev * 10 + rem
print(f"{int(rev)}")

num1 = temp

d = num1%10
num1 = int(num1/10)
temp1 = num1
		
c = num1%10
num1 = int(num1/10)

b = num1%10
num1 = int(num1/10)

a = num1

print(f"{int(a)} {int(b)} {int(c)} {int(d)}")

print(f"{int(a*1000)} {int(b*100)} {int(c*10)} {int(d)}")


