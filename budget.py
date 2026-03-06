def calculate_remaining_balance():
    try:
        # Ask for the total monthly budget
        total_budget = float(input("Enter your total monthly budget (LKR): "))

        # Ask for 3 expenses
        expense1 = float(input("Enter the amount for Expense 1 (LKR): "))
        expense2 = float(input("Enter the amount for Expense 2 (LKR): "))
        expense3 = float(input("Enter the amount for Expense 3 (LKR): "))

        # Calculate the total expenses and remaining balance
        total_expenses = expense1 + expense2 + expense3
        remaining_balance = total_budget - total_expenses

        # Display the results
        print("\n--- Budget Summary ---")
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
        # Handle the error if the user inputs text instead of numbers
        print("\nError: Please enter valid numerical values for your budget and expenses.")

# Run the function
if __name__ == "__main__":
    calculate_remaining_balance()