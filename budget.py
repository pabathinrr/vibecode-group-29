while True:
    # Ask for student's name
    name = input("\nEnter student name (or type 'Exit' to stop): ")

    # Check if the user wants to exit
    if name.strip().lower() == 'exit':
        print("Exiting the program...")
        break

    # Ask for 3 subject marks
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))

    # Calculate average
    average = (mark1 + mark2 + mark3) / 3

    print("\n--- Result ---")
    print("Student Name:", name)
    print(f"Average: {average:.2f}")

    # Assign grade
    if average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 40:
        print("Grade: C")
    else:
        print("Grade: Fail")
    print("-" * 14)