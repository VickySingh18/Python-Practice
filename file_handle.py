#Error Handling

try:
    numerator=float(input("Enter the first Numerator "))
    denominator=float(input("Enter the first Denominator "))
    result=numerator/denominator
    print(f"Result:{result}")
except ZeroDivisionError:
    print("Error:you cant divide by zero")
except ValueError:
    print("Error:Please enter valid number only")