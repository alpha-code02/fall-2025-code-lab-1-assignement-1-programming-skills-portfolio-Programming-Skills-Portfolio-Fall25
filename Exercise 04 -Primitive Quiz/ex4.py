def exercise_1():
    word1 = "Coding"
    word2 = " is "
    word3 = "Cool"

    print(word1 + word2 + word3)


def exercise_2():
    a = 8
    b = 10
    total = a + b
    print("Exercise 2 - Sum of", a, "and", b, "is", total)


def exercise_3():
    name = "Ethan"
    hometown = "Dubai"
    age = 18

    biography = {"name": name, "hometown": hometown, "age": age}

    print(biography["name"], biography["hometown"], biography["age"], sep="\n")


def exercise_4():
    print("Exercise 4 - Capital Quiz")
    mode = input(
        "Type '1' to answer 1 question (Russia) or '10' for a 10-question European capitals quiz: "
    ).strip()

    def single_question():
        answer = input("What is the capital of Russia? ").strip()
        if answer.lower() == "moscow":
            print("Correct! :)")
        else:
            print("Wrong — the correct answer is moscow.")

    if mode == "1" or mode == "":
        single_question()
        return

    capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Portugal": "Lisbon",
        "Netherlands": "Amsterdam",
        "Belgium": "Brussels",
        "Switzerland": "Bern",
        "Austria": "Vienna",
        "Poland": "Warsaw",
    }
    score = 0
    for country, capital in capitals.items():
        ans = input(f"What is the capital of {country}? ").strip()
        if ans.lower() == capital.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect — the correct answer is {capital}.")
    print(f"Quiz finished. You scored {score} out of {len(capitals)}")


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


def exercise_6():
    correct_password = "12345"
    attempts = 3
    attempt = 0
    while attempt < attempts:
        password = input("Enter the password: ").strip()
        if password == correct_password:
            print("Access granted.")
            return
        else:
            attempt += 1
            print(f"Incorrect password. You have {attempts - attempt} attempts left.")
    print("Access denied. Too many incorrect attempts.")


def exercise_7():
    print("Counting up from 0 to 50:")
    for i in range(0, 51):
        print(i, end=" ")
    print("\n")

    print("Counting down from 50 to 0:")
    for i in range(50, -1, -1):
        print(i, end=" ")
    print("\n")

    print("Counting up from 30 to 50:")
    for i in range(30, 51):
        print(i, end=" ")
    print("\n")

    print("Counting down from 50 to 10 in steps of 2:")
    for i in range(50, 9, -2):
        print(i, end=" ")
    print("\n")

    print("Counting up from 100 to 200 in steps of 5:")
    for i in range(100, 200, 5):
        print(i, end=" ")
    print("\n")


def exercise_8():
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    print("Default list:", names)
    term = input("Enter name to search for (Leave empty to search for 'Sam'): ").strip()
    if term == "":
        term = "Sam"
    found = False
    for name in names:
        if name.lower() == term.lower():
            found = True
            break
    if found:
        print(f"{term} was found in the list.")
    else:
        print(f"{term} was NOT found in the list.")


def exercise_9():
    def hello():
        print("Hello")

    def main_func():
        hello()

    main_func()


def exercise_10():
    def is_even(n):
        try:
            n_int = int(n)
        except ValueError:
            return "Error: the input is not an integer."
        if n_int % 2 == 0:
            return f"{n_int} is even."
        else:
            return f"{n_int} is odd."

    num = input("Enter a number to test even/odd: ").strip()
    result = is_even(num)
    print(result)


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()
