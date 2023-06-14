def calculate_age():
    name = input("Enter your name: ")
    birth_year = int(input("Enter your birth year: "))
    current_year = 2023  # Replace with the current year
    age = current_year - birth_year
    print(f"{name}, you are {age} years old.")

calculate_age()
