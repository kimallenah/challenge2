from datetime import datetime

currentYear = datetime.now().year

while True:
    x = str(int(input("Enter your year of birth: ")))
    if len(x) < 4 or len(x) > 4:
        print("Invalid year. Please enter a correct year.")

    elif x > str(currentYear):
        print("Invalid year. Please enter a correct year.")


    else:
        age = currentYear - int(x)

        if age < 18:
            print("Hello, you are a minor.")
            break
        elif age >= 18 and age <= 36:
            print("Hello, you are a youth.")
            break
        else:
            print("Hello, you are an elder.")
            break
