# For the following list of numbers:

from contextlib import nullcontext


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
evenNumbers = []
for number in numbers:
    if number %2 == 0:
        evenNumbers.append(number)
print(evenNumbers)

# 2. Print the difference between the largest and smallest value:
largestnumber = 0
smallestNumber = 99
for number in numbers:
    if number > largestnumber:
        largestnumber = number
for number in numbers:
    if number < smallestNumber:
        smallestNumber = number
print(largestnumber - smallestNumber)


# 3. Print True if the list contains a 2 next to a 2 somewhere.
testNumber = 0
for number in numbers:
    if testNumber == number:
        print("True")
    testNumber = number


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
add = True
for number in numbers:
    if number != 6 and add == True:
        total += number
    elif number == 6:
        add = False
    elif number == 7:
        add = True
print(total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

total = 0
counter = True

for number in numbers:
    if number != 13 and counter == True:
        total += number
    elif number == 13:
        counter = False
    else:
        counter = True

print(total)





