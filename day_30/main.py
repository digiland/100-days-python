height = float(input("Enter height: "))
weight = float(input("Enter weight: "))

if height > 3:
    raise ValueError("Height must be less than 3")

bmi = weight / (height * height)
print("BMI: ", bmi)
