
weight = (input("Enter your weight in kg: "))
height = (input("Enter your height in meters: "))

bmi = weight / (height * height)

print("Your BMI is:", bmi)

if bmi < 18:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Extremely Obese")
