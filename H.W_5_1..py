while True:
    first_number = float(input("Enter first digit: "))
    operator = input("Enter operator (+, -, *, /,): ")
    second_number = float(input("Enter second digit: "))

    if operator == "-":
        result = first_number - second_number
    elif operator == "+":
        result = first_number + second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            result = None
            print("cannot divide by zero")
        else:
            result = first_number / second_number
    else:
        result = None
        print("no valid data")

    print(result)

    new_condition = input("Do you want to continue?").lower()
    if new_condition == "yes" or new_condition == "y":
        print(" new calculation")
        continue
    else:
        break
print("exit")
