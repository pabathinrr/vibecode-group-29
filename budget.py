def calculate_remaining_balance():
    try:
        # Ask for the total monthly budget
<<<<<<< HEAD
        total_budget = float(input("Enter your total monthly budget: "))

        # Ask for 3 expenses
        expense1 = float(input("Enter the amount for Expense 1: "))
        expense2 = float(input("Enter the amount for Expense 2: "))
        expense3 = float(input("Enter the amount for Expense 3: "))

        # Calculate the total expenses and remaining balance
        total_expenses = expense1 + expense2 + expense3
=======
        total_budget = float(input("Enter your total monthly budget (LKR): "))
        
        # Set up variables to keep track of expenses
        total_expenses = 0.0
        expense_count = 1

        print("\nEnter your expenses one by one. Type 'done' when you are finished.")
        
        # Loop to continuously ask for expenses
        while True:
            user_input = input(f"Enter the amount for Expense {expense_count} (or 'done'): ")
            
            # Check if the user wants to stop
            if user_input.strip().lower() == 'done':
                break
            
            # Try to convert the input to a number and add it to the total
            try:
                expense = float(user_input)
                total_expenses += expense
                expense_count += 1
            except ValueError:
                print("  -> Invalid input. Please enter a numerical value or 'done'.")

        # Calculate remaining balance
>>>>>>> 3796f7896f0049283b8ee3ca6e2d625193a0bd86
        remaining_balance = total_budget - total_expenses

        # Display the results
        print("\n--- Budget Summary ---")
<<<<<<< HEAD
        print(f"Total Budget:      ${total_budget:.2f}")
        print(f"Total Expenses:    ${total_expenses:.2f}")
        print("----------------------")
        
        # Display the remaining balance, alerting the user if they overspent
        if remaining_balance >= 0:
            print(f"Remaining Balance: ${remaining_balance:.2f}")
        else:
            print(f"Remaining Balance: -${abs(remaining_balance):.2f} (Over budget!)")

    except ValueError:
        # Handle the error if the user inputs text instead of numbers
        print("\nError: Please enter valid numerical values for your budget and expenses.")
=======
        print(f"Total Budget:      {total_budget:.2f} LKR")
        print(f"Total Expenses:    {total_expenses:.2f} LKR")
        print("----------------------")
        
        # Display the remaining balance with appropriate warnings
        if remaining_balance < 0:
            print(f"Remaining Balance: -{abs(remaining_balance):.2f} LKR")
            print("Warning: Over budget!")
        elif remaining_balance < 500:
            print(f"Remaining Balance: {remaining_balance:.2f} LKR")
            print("Warning: Low Funds")
        else:
            print(f"Remaining Balance: {remaining_balance:.2f} LKR")

    except ValueError:
        # Handle the error if the user inputs text instead of numbers for the initial budget
        print("\nError: Please enter a valid numerical value for your initial budget.")
>>>>>>> 3796f7896f0049283b8ee3ca6e2d625193a0bd86

# Run the function
if __name__ == "__main__":
    calculate_remaining_balance()