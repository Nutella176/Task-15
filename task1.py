#Ask user to input a number
#Use the for loop to multiply the number by 1 up to 12 and print the times table 

number = int(input("Please enter a number: "))
i = 1

print(f"The {number} times table is: ")

for i in range(1,13):
    print(f"{number} x {i} = {number * i}")
    i += 1
    