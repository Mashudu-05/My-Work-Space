"""
Ask the user to enter the weight in Kg and height in m

BMI = (weight in kg) / ((height in m)*(height in m))

 If the user’s BMI is 30 or greater, the user is obese
 If the user’s BMI is 25 or greater, the user is overweight
 If the user’s BMI is 18.5 or greater, the user is normal
 If the user’s BMI is less than 18.5, the user is underweight
 Display the user’s BMI and whether they are obese, overweight, normal or
underweight.

"""

weight_in_kg = float(input("Enter your weight in kg: "))
height_in_m = float(input("Enter your height in meters: "))

# Calculate BMI
BMI = weight_in_kg / (height_in_m ** 2)

print(f"Your BMI is: {BMI:.2f}")

if BMI >= 30:
    print("You are obese.")
elif BMI >= 25:
    print("You are overweight.")
elif BMI >= 18.5:
    print("You are normal weight.")
else:  
    print("You are underweight.")


