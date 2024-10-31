#while summation code following directions from Readme
EnteredNumber = int (input ("Enter a number: "))
CountingNumber = 1
Sum = 0

while CountingNumber <= EnteredNumber:
    Sum = CountingNumber + Sum
    CountingNumber = CountingNumber + 1
print (str(Sum))