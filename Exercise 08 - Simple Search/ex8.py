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
