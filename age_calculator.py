from datetime import date

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = date.today().year
age = current_year - birth_year
print(f"Hello {name}. Your age is {age}.")
