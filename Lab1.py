def calculate_age():
    try:
        name = input("Enter your name: ")
        birth_year = int(input("Enter your birth year: "))
        current_year = 2023  # Replace with the current year
        age = current_year - birth_year
        print(f"{name}, you are {age} years old.")
    except ValueError:
        print("Please enter an integer for the birth year.")

calculate_age()
