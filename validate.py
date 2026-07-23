def get_age():
    while True:
        try:
            age = int(input("enter the age:"))
            if age >= 1 and age <= 120:
                print (f"your age is {age}")
                break
            else:
                print("must be between 1-120")
        except ValueError:
            print("thats not a real number")ff

get_age()