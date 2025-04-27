def divide_by(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide a number by zero.")
    else:
        return result
    finally:
        print("Division complete.")

print(divide_by(10, 5)) # prints 2.0 and "Division complete."
print(divide_by(10, 0)) # prints "Error: Cannot divide a number by zero." and "Division complete."