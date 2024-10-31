#for Summation code her
EnteredNumber = int(input("Enter a number: "))
CountingNumber = 1
Sum = 0

for i in range(EnteredNumber):
    Sum = CountingNumber + Sum
    CountingNumber = CountingNumber + 1

print (str(Sum))