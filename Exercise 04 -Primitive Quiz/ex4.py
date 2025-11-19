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


exercise_4()
