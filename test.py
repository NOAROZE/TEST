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
num = num // result
num %= 10
print(f"The digit is: {num}")
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

# 9
num: int = int(input("Enter a number:"))
print("even" if num% 2 == 0 else "odd")
#

# 10
tax = 0
while True:
    salary: int = int(input("Enter your salary:"))
    match salary:
        case salary if salary < 6000:
            tax = salary
            break
        case salary if 6000 <= salary < 12000:
            tax = int(salary + (salary - 6000) / 100 * 10)
            break
        case salary if 12000 <= salary < 18000:
            tax = int(salary + (salary - 6000) / 10 + (salary - 12000) / 100 * 20)
            break
        case salary if 18000 <= salary < 25000:
            tax = int(salary + (salary - 6000) / 10 + (salary - 12000) / 100 * 20 + (salary - 18000) / 100 * 30)
            break
        case salary if 25000 <= salary < 35000:
            tax = int(salary + (salary - 6000) / 10 + (salary - 12000) / 100 * 20 + (salary - 18000) / 100 * 30 + (salary - 25000) / 100 * 40)
            break
        case salary if 35000 <= salary < 50000:
            tax = int(salary + (salary - 6000) / 10 + (salary - 12000) / 100 * 20 + (salary - 18000) / 100 * 30 + (
                        salary - 25000) / 100 * 40 + (salary - 35000) / 100 * 45)
            break
        case salary if 50000 <= salary:
            tax = int(salary + (salary - 6000) / 10 + (salary - 12000) / 100 * 20 + (salary - 18000) / 100 * 30 + (
                    salary - 25000) / 100 * 40 + (salary - 35000) / 100 * 45 + (salary - 50000) / 100 * 51)
            break
print(tax)
#

# 11
age: int = int(input("Enter your age:"))
height: int = int(input("Enter your height in centimeters:"))
print("Person is allowed to climb the facility"if (8 <= age <= 18 and height >= 115) or (age > 18 and height > 100) else"Person is not allowed to climb the facility")
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
    for i in range(num2, num1 + 1):
        print(i)
else:
    for i in range(num1, num2 + 1):
        print(i)
#

# 3
num: int = int(input("Enter a natural number:"))
for i in range(0, num + 1, 2):
    print(i)
#

# 4
maximum: int = int(input("Enter a natural number:"))
den: int =int(input("Enter a natural number:"))
for i in range(0,maximum + 1):
    if i % den == 0:
        print(f"The number: {i} dividing in {den}")
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

# 4
num1: int = int(input("Enter a number:"))
num2: int = int(input("Enter a number:"))
multiplier: int = num1
counter: int = num2
while counter > 1:
    multiplier += num1
    counter -= 1
print(f"The multiplier is: {multiplier}")
#

# 5
num1: int = int(input("Enter a number:"))
num2: int = int(input("Enter a number:"))
power: int = num1
counter: int = num2
while counter > 1:
    power *= num1
    counter -= 1
print(f"The power is: {power}")
#

# 6
num: int = int(input("Enter a number:"))
digit: int = int(input("Enter a number:"))
bool1: list[bool] = []
counter: int = 0
number: int = num
while number > 0:
    number //= 10
    counter += 1
for i in range(counter):
    bool1.append(True if digit == num % 10 else False)
    num //= 10
print(True if any(bool1) else False)
#

# 7
num1: int = int(input("Enter a number:"))
num2: int = int(input("Enter a number:"))
if num1 > num2:
    for i in range(num2, 0, -1):
        if int(num1 % i == 0 and num2 % i == 0):
            print(f"The highest divider is: {i}")
            break
else:
    for i in range(num1, 0, -1):
        if int(num2 % i == 0 and num1 % i == 0):
            print(f"The highest divider is: {i}")
            break
#

# 8
num: int = int(input("Enter a number:"))
bool1: bool = True
if num < 2:
    bool1 = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            bool1 = False
print(f"The number {num} is prime"if bool1 else f"The number {num} is no prime")
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
    print(f"The average of temperature is: {average}")
    print(f"The highest temperature is: {max(temperatures)}")
    print(f"The lowest temperature is: {min(temperatures)}")
#

# 2
counter: int = 44
prefer: int = 1
against: int = 2
impossible: int = 3
veto: int = 4
country_point: int = 1
all_points: list[int] = []
location: int = 0
while counter > 0:
    try:
        point: int = int(input("Enter your voting topic from 1 to 4:"))
        if prefer <= point <= veto:
            if point == prefer:
                all_points.append(prefer)
            elif point == against:
                all_points.append(against)
            elif point == impossible:
                all_points.append(impossible)
            else:
                print(f"The number of country that voted veto is: {country_point}")
                break
        else:
            continue
        counter -= 1
        country_point += 1
    except ValueError:
        print("wrong input")
else:
    print(f"The number of prefer: {all_points.count(prefer)}")
    print(f"The number of against: {all_points.count(against)}")
    print(f"The number of impossible: {all_points.count(impossible)}")
    for point in range(44):
        if all_points[location] == 1:
            print(f"The serial number of the country that voted prefer is: {location + 1}")
            break
        location += 1
    for point in range(44):
        if all_points[location] == 2:
            print(f"The serial number of the country that voted against is: {location + 1}")
            break
        location += 1
#
#
