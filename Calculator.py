def calculator():
    print(" Simple Calculator")
    print("Operations: +  -  *  /")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print(" Cannot divide by zero.")
                return
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print(" Please enter valid numbers.")

calculator()