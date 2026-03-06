def calculate_student_result():
    # Input Section
    name = input("Enter student's name: ")

    try:
        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))

        # Processing: Calculate Average
        average = (mark1 + mark2 + mark3) / 3

        # Processing: Determine Grade based on standard scales
        if average >= 75:
            grade = "A"
        elif average >= 65:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "S"
        else:
            grade = "F"

        # Output Section: Clean Formatting
        print("\n------------------------------")
        print(f"Name    : {name}")
        print(f"Average : {average:.1f}")
        print(f"Grade   : {grade}")
        print("------------------------------")

    except ValueError:
        print("\nError: Please enter valid numerical values for the marks.")

if __name__ == "__main__":
    calculate_student_result()