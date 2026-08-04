try:
    number1 = int(input("enter a number: "))
    number2 = int(input("enter a number: "))
    result = number1 / number2
    print(result)
except (ValueError,ZeroDivisionError):
    print("ENETE RVALID numbrr")