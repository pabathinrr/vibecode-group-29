def calculate_student_result():
    # Ask for the student's name
    name = input("Enter student's name: ")

    try:
        # Ask for 3 subject marks (using float to allow decimal scores)
        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))

        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3

        # Determine Pass or Fail
        if average >= 40:
            status = "Pass"
        else:
            status = "Fail"

        # Display the results
        print("\n--- Result Summary ---")
        print(f"Student Name: {name}")
        print(f"Average Mark: {average:.2f}")
        print(f"Status:       {status}")

    except ValueError:
        # Handle the error if the user inputs text instead of numbers for the marks
        print("\nError: Please enter valid numerical values for the marks.")

# Run the function
if __name__ == "__main__":
    calculate_student_result()