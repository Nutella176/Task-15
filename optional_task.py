#Ask user to input a number
#Use a for loop - if umber is > 10, print the number as many times as its value
#If number is <= 10, break loop and print error message 

num = int(input("Please enter a number: "))

for i in range(num):
    if num <= 10:
        print("Sorry, too small")
        break
    else:
        print(num)
        