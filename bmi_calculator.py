
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)
bmi_rounded = round(bmi,2)

print(bmi_rounded)
# print(f"Your BMI is:, {bmi:.2f} ")

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
