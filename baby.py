from datetime import date

"""

Ask the user to enter the year they were born
Calculate the age based on the year they were born
if they are 18 or older display message that says "congrats you are old enough"

"""


born_year = int(input("Enter the year you were Born:"))

#Getting the current year

current_date = date.today()

current_year = current_date.year

age = current_year - born_year

if age >= 18 :
    print("Congrats you are old enough")
