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

📘 My First Python Programs

This repository contains my basic Python learning programs.


---

1️⃣ My First Program

This program takes user input and prints a short introduction.

🖥 Code:

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
hobby = input("Enter your hobby: ")

print(f"Hello! My name is {name}. I am {age} years old, I live in {city}, and I love {hobby}.")

✅ Example Output:

Enter your name: Noor Fatima
Enter your age: 19
Enter your city: Lahore
Enter your hobby: Coding

Hello! My name is Noor Fatima. I am 19 years old, I live in Lahore, and I love Coding.


---

2️⃣ Age Calculator

This program calculates the age of a person based on the current year and their birth year.

🖥 Code:

current_year = int(input("Enter current year: "))
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year
print("Your age is:", age)

✅ Example Output:

Enter current year: 2025
Enter your birth year: 2005
Your age is: 20


---

3️⃣ Voting Eligibility

This program checks if a person is eligible to vote based on their age.

🖥 Code:

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

✅ Example Output:

Enter your age: 20
Eligible to vote

Enter your age: 15
Not eligible to vote


---

4️⃣ Favorite Movies List

This program stores the user's favorite movies in a list and displays them.

🖥 Code:

movies = []

movie1 = input("Enter your first favorite movie: ")
movie2 = input("Enter your second favorite movie: ")
movie3 = input("Enter your third favorite movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print("Your favorite movies are:", movies)

✅ Example Output:

Enter your first favorite movie: Inception
Enter your second favorite movie: Titanic
Enter your third favorite movie: Avatar

Your favorite movies are: ['Inception', 'Titanic', 'Avatar']


---

✨ These are my first Python programs created as part of my learning journey.

5️⃣ Simple Calculator


This program is a **menu-driven calculator** that performs different arithmetic operations.

🖥 Code:
```python
print("------ Simple Calculator ------")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exponent (**)")
print("6. Modulus (%)")

# Taking user input
choice = int(input("\nEnter your choice (1-6): "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Performing operations
if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result =", a / b)
elif choice == 5:
    print("Result =", a ** b)
elif choice == 6:
    print("Result =", a % b)
else:
    print("Invalid choice!")

✅ Example Output:

------ Simple Calculator ------
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exponent (**)
6. Modulus (%)

Enter your choice (1-6): 1
Enter first number: 10
Enter second number: 5
Result = 15

✨ This project helps beginners practice using:

Input and Output in Python

If-Else conditions

Arithmetic operators

6️⃣ Data Types Example

This program demonstrates Python's basic data types and prints their types using the `type()` function.

🖥 Code:
```python
x = 10
y = 2.53
name = "noor"
coine = True

print(type(x), type(y), type(name), type(coine))

✅ Example Output:

<class 'int'> <class 'float'> <class 'str'> <class 'bool'>

📖 Explanation:

int → Integer numbers (e.g., 10)

float → Decimal numbers (e.g., 2.53)

str → Text (e.g., "noor")

bool → Boolean values (True / False)
7️⃣ Reverse Words in a String

This program takes a sentence as input and reverses the order of its words.

🖥 Code:

sentence = input("Enter your sentence: ")
words = sentence.split()
words.reverse()
result = ' '.join(words)
print(result)

✅ Example Output:

Enter your sentence: I love Python
Python love I


---

8️⃣ Second Largest Number

This program finds the second largest number from a list entered by the user.

🖥 Code:

numbers = []
for i in range(5):
    numbers.append(int(input("Enter your number: ")))
numbers.sort()
print("Second largest number:", numbers[-2])

✅ Example Output:

Enter your number: 10
Enter your number: 20
Enter your number: 4
Enter your number: 45
Enter your number: 99
Second largest number: 45


---

9️⃣ Palindrome Check

This program checks whether a given word is a palindrome (same forward and backward).

🖥 Code:

word = input("Enter your word: ")
reverse = word[::-1]
if word == reverse:
    print("Palindrome")
else:
    print("Not palindrome")

✅ Example Output:

Enter your word: madam
Palindrome

Enter your word: hello
Not palindrome


---

🔟 Count Vowels and Consonants

This program counts the number of vowels and consonants in a sentence.

🖥 Code:

sentence = input("Enter your sentence: ")
vowels = 0
consonants = 0

for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)

✅ Example Output:

Enter your sentence: I love Python
Vowels = 4
Consonants = 7

My Python Practice Questions

Q1: Sum, Difference, Multiplication, Division

🖥 Code:

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print("Sum =", a+b)
print("Difference =", a-b)
print("Multiplication =", a*b)
print("Division =", a/b)

✅ Example Output:

Enter your first number: 10  
Enter your second number: 5  
Sum = 15  
Difference = 5  
Multiplication = 50  
Division = 2.0


---

Q2: String vowel se start hoti hai ya nahi

🖥 Code:

str1 = input("Enter your string: ")
if str1[0].lower() in "aeiou":
    print("The string starts with a vowel")
else:
    print("Not start vowel")

✅ Example Output:

Enter your string: apple  
The string starts with a vowel


---

Q3: Average of 10 numbers

🖥 Code:

numbers = []
for i in range(10):
    numbers.append(int(input("Enter your number: ")))
aver = sum(numbers) / len(numbers)
print("Average =", aver)

✅ Example Output:

Enter your number: 10  
Enter your number: 20  
...  
Average = 15.0


---

Q4: Tuple second last element

🖥 Code:

tup = (1, 2, 3, 4, 5)
print("Second last element =", tup[-2])

✅ Example Output:

Second last element = 4


---

Q5: Dictionary students marks

🖥 Code:

student = {"ali": 25, "noor": 29}
name = input("Enter your name: ")
if name in student:
    print("Marks =", student[name])
else:
    print("Not found")

✅ Example Output:

Enter your name: noor  
Marks = 29





