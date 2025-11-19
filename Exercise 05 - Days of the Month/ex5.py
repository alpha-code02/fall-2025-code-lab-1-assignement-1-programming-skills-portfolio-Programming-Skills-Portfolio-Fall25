def exercise_5():
    days_in_month = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }
    month = input("Enter the name of a month: ").strip()
    days = days_in_month.get(month)
    if days:
        print(f"{month} has {days} days.")
        if month == "February":
            leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
            if leap_year == "yes":
                print("February has 29 days in a leap year.")
    else:
        print("Invalid month name. Please try again.")


exercise_5()
