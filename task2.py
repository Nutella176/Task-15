#Get user to input the first year they wish to check if it's a leap year 
#Ask user to enter the number of years they wish to check for a leap year starting from the first year 
#Using for loop, calculate and display which of those years are leap and which are not 

first_year = int(input("What year do you want to start with? "))
num_of_years = int(input("How many years do you want to check? "))

for year in range(first_year, first_year + num_of_years):
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    year += 1

