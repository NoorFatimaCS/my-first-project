
# menu_calculator.py

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


