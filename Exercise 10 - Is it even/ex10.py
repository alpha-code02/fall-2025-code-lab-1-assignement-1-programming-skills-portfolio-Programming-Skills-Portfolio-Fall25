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


exercise_10()
