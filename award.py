"""
Competion for Swimming, Cycling and Running

The user must enter the minutes for both swimming, cycling and running
Print out the minutes complete
calculate the total minutues for the user
print the total time for triathlon
if the total time is less than 100, print provincial colours
if the total time is less than 100 and less or eqaul to 105, print provincial half colours
if the total time is less than 105 and less or equal to 110, print provincial scroll
if the total time is more than 110 print No award

"""

swimming = int(input("Enter time taken for swimming in minutes : "))

cycling = int(input("Enter time taken for cycling in minutes : "))

running = int(input("Enter time taken for running in minutes : "))

total_time = swimming + cycling + running
print("Total time taken for triathlon: ",total_time)

if (total_time < 100): 
    print("Provincial colours")

elif (total_time > 100 and total_time <=105) :
    print("Provincial half colours")

elif (total_time >105 and total_time <=110):
    print("Provincial scroll")

else:
    print("No Award")
