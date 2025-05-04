# Ask user to enter their age

age = int(input("Enter your age: "))

# Check the age and print required messages

if age >= 18:
    print("You are old enough.")
elif age >= 16:  
    print("Almost there.")
else:  
    print("You're just too young.")
