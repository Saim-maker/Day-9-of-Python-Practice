principle = 0
interest = 0
time = 0

while principle <= 0:
    principle = int(input("Enter the Principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than or equal to 0")

while interest <= 0:
    interest = int(input("Enter the Interest amount: "))
    if interest <= 0:
        print("Interest amount must be greater than or equal to 0")




while time <= 0:
    time = int(input("Enter the Time amount: "))
    if time <= 0:
        print("Time amount must be greater than or equal to 0")

print(principle)
print(interest)
print(time)

total = principle * pow((1 + interest/100),time)
print(f"Total after {time} years : ${total}")

lenght = 0
width = 0

while lenght <= 0:
    lenght = int(input("Enter lenght: "))
    if lenght <= 0:
        print("Please enter the valid input")

while width <= 0:
    width = int(input("Enter width: "))
    if width <= 0:
        print("Please enter the valid input")

area = lenght * width
print(f"With {lenght} lenght and {width} width is area is : {area}")

weight = 0
height = 0

while weight <= 0:
    weight = int(input("Enter weight: "))
    if weight <= 0:
        print("Please enter a positive integer!")
while height <= 0:
    height = int(input("Enter height: "))
    if height <= 0:
        print("Please enter a positive integer!")

bmi = weight/pow(height,2)
print(f"Your BMI is: {bmi}")