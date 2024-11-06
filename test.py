# conditions
# 1
num1: float = float(input("Enter a number:"))
num2: float = float(input("Enter a number:"))
print(num1 if num1 < num2 else num2)
print(num1 if num1 < num2 else num2)
print(num1 if num1 < num2 else num2)
#

# 2
num1: int = int(input("Enter a number:"))
num2: int = int(input("Enter a number:"))
print(f"The average is: {(num1 + num2) // 2}")
#

# 3
num1: int = int(input("Enter a number:"))
num2: int = int(input("Enter a number:"))
num3: int = int(input("Enter a number:"))
if num1 > num2 and num1 > num3:
    print(f"{num1} is the biggest")
elif num2 > num3:
    print(f"{num2} is the biggest")
else:
    print(f"{num3} is the biggest")
#

# 4
len_of_movie: int = int(input("Enter the length of the movie in minutes:"))
hours: int = len_of_movie // 60
minutes: int = len_of_movie % 60
print(f"The length of the movie is: {hours} hours and: {minutes} minutes ")
#

# 5
num: int = int(input("Enter a number of 4 digits:"))
result: int = 1000
for i in range(3):
    num = num % result
    result /= 10
print(f"The rightmost digit is: {num}")
#
# 6
num: int = int(input("Enter a number of 4 digits:"))
result: int = 10
for i in range(2):
    num = num // result
num %= 10
print(f"The rightmost digit is: {num}")
#

# 7
num: int = int(input("Enter a number of 2 digits:"))
sum_up: int =  num // 10 + num % 10
print(f"The sum is: {sum_up}")
#

# 8
num: int = int(input("Enter a number of 2 digits:"))
digit1: int = num // 10
digit2: int = num % 10
print(digit2 * 10 + digit1)
#
#

# loops
# 1
num: int = int(input("Enter a natural number:"))
for i in range(1, num + 1):
    print(i)
#

# 2
num1: int = int(input("Enter a natural number:"))
num2: int = int(input("Enter a natural number:"))
if num1 > num2:
    for i in range(num2, num1):
        print(i)
else:
    for i in range(num1, num2):
        print(i)
#
#

# data processing
# 1
SENTINEL: int = -99
sum_up: int = 0
counter: int = 1
while True:
    num: int = int(input("Enter a number:"))
    if counter == 1:
        if num == SENTINEL:
            print(None)
    if num == SENTINEL:
        break
    sum_up += num
    counter += 1
print(f"The sum is: {sum_up}")
#

# 2 עשיתי חלק את הקטן ביותר עם רשימה כי ראיתי שהתחלתי להסתבך ...
SENTINEL: int = -99
counter: int = 1
biggest: int = 0
smallest: int = 0
numbers: list[int] = []
while True:
    num: int = int(input("Enter a number:"))
    if counter == 1:
        if num == SENTINEL:
            print(None)
    counter += 1
    if num <= 0:
        break
    numbers.append(num)
    if num > biggest:
        biggest = num
    smallest = min(numbers)
print(f"The number with the highest value is: {biggest}")
print(f"The number with the highest value is: {smallest}")
#

# 3
counter: int = 0
biggest: int = 0
for i in range(5):
    num: int = int(input("Enter a number:"))
    if num > biggest:
        biggest = num
        counter = i
print(counter + 1)
#

#

# complex loops
# 1

average: int = 0
sum_temper: int = 0
temperatures: list[int] = []
counter: int = 12
while counter > 0:
    try:
        temperature: int = int(input("Enter the temperature:"))
        if -5 <= temperature <= 40:
            print("correct data")
            if temperature == 0 and len(temperatures) > 0 and temperatures[-1] == 0:
                continue
            sum_temper += temperature
            temperatures.append(temperature)
            counter -= 1
        else:
            print("wrong data")
    except:
        print(f"The input is not a number")
        # temperature: int = int(input("Enter the temperature:"))
else:
    average = sum_temper // 12
    print(average)
#
#