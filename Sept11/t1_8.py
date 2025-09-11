myvar = int(input("Enter the number"))

firstDigit = myvar // 100
ost = myvar % 100
secondDigit = ost // 10
thirdDigit = ost % 10
print(firstDigit * secondDigit * thirdDigit)