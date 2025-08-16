My First Python Program

This is my very first Python project, created to practice the basics of Python programming such as:

Taking user input

Printing output

Using f-strings for formatting


Program Code

name = input("enter your name:")
age = input("enter your age:")
city = input("enter your city:")
hobby = input("enter your hobby:")
print(f"Hello! My name is {name}. I am {age} years old, I live in {city}, and I love {hobby}.")

Program Output

enter your name: Noor Fatima 
enter your age: 19 
enter your city: Lahore  
enter your hobby: Coding 
Hello! My name is Noor Fatima. I am 19 years old, I live in Lahore, and I love Coding.



How to Run

1. Install Python (version 3.x).


2. Save the program as myfirstprogram.py.


3. Run in terminal or command prompt:
python myfirstprogram.py



   About This Project

This repository is part of my Python learning journey.
It is meant for beginners who are learning:

How to take input in Python

How to format strings

How to run basic scripts

 Keywords (for Google Search)

Python beginner project, first Python program, Python input output example, Python f-string example, how to take input in Python, Python basics for beginners, learn Python step by step, Python simple projects, coding for beginners, Python tutorial example code, start programming with Python, beginner-friendly Python project, my first Python code, how to run Python program, Python practice code.
My First Python Programs

This repository contains my basic Python learning programs.


---

1. Age Calculator

This program calculates the age of a person based on the current year and their birth year.

Code:

current_year = int(input("Enter current year: "))
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year
print("Your age is:", age)

Output Example:

Enter current year: 2025  
Enter your birth year: 2005  
Your age is: 20


---

2. Voting Eligibility

This program checks if a person is eligible to vote based on their age.

Code:

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

Output Example:

Enter your age: 20  
Eligible to vote  

Enter your age: 15  
Not eligible to vote


---

3. Favorite Movies List

This program stores the user's favorite movies in a list and displays them.

Code:

movies = []

movie1 = input("Enter your first favorite movie: ")
movie2 = input("Enter your second favorite movie: ")
movie3 = input("Enter your third favorite movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print("Your favorite movies are:", movies)

Output Example:

Enter your first favorite movie: Inception  
Enter your second favorite movie: Titanic  
Enter your third favorite movie: Avatar  
Your favorite movies are: ['Inception', 'Titanic', 'Avatar']

