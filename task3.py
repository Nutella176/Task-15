#1 Using while loop count down from 20 to 0 

number = 20 

while True:
    print(number)
    number -= 1 
    if number == -1:
        break

#2 Create any type of loop to print all even numbers between 1 and 20 

number = 20

for i in range(1,number + 1):
    if i % 2 == 0:
        print(i)

#3 Create a loop that will produce one to five "*"

symbol = "*"

while True:
    print(symbol)
    symbol += "*"
    if symbol == "******":
        break 

#4 Calculate the greatest common divisor between two positive numbers

num1 = 9
num2 = 27

if num1 > num2:
    smaller = num2
else:
    smaller = num1

while smaller > 0:
    if num1 % smaller == 0 and num2 % smaller == 0:
        print("The GCD is", smaller)
        break 
    smaller -= 1 

