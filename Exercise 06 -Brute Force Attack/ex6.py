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


exercise_6()
