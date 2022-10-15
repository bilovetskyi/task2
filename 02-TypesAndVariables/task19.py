height = input("Enter your haight in cm: ")
weight = input("Enter your weight in kg: ")
height = float(height)
weight = float(weight)
height_in_m = height/100

bmi_index = weight/height_in_m**2

print(f"Your BMI index is {bmi_index}") 

