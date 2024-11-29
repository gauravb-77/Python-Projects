from datetime import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt


def add_expense():

    while True:
        date = input("Enter the date of expense (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            print(f"Valid date entered: {date.strftime("%Y-%m-%d")}")
            break
        except ValueError:
            print("Invalid date. Please use the format YYYY-MM-DD.")

    while True:
        amount = input("Enter the amount of expense: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Expense amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number as expense amount.")

    category = input("Enter the category of expense: ").strip()

    description = input("Enter the description of expense: ").strip()

    new_expense = {
        "Date": date.strftime("%Y-%m-%d"),
        "Amount": amount,
        "Category": category,
        "Description": description
    }

    # Load existing data
    try:
        df = pd.read_csv("expense_file.csv")
    except FileNotFoundError:
        # Create a new DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])

    # Append the new expense
    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)

    # Save back to the CSV
    df.to_csv("expense_file.csv", index=False)
    print("\n\nExpense added successfully.")


def view_expenses():

    try:
        df = pd.read_csv("expense_file.csv")

        if df.empty:
            print("\nNo expenses recorded yet.")
        else:
            # Capitalize headers for display
            df.columns = [col.capitalize() for col in df.columns]

            # Convert the "Date" column to datetime format
            df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")


            filter_choice = input("Do you want to filter by (1) Date or (2) Category? Press any other key to view all: ")

            # Filter by Date
            if filter_choice == '1':
                while True:
                    start_date = input("Enter the start date (YYYY-MM-DD): ")
                    try:
                        start_date = datetime.strptime(start_date, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format for starting date. Please use YYYY-MM-DD.")
                        continue

                    end_date = input("Enter the end date (YYYY-MM-DD): ")
                    try:
                        end_date = datetime.strptime(end_date, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format for ending date. Please use YYYY-MM-DD.")
                        continue

                    if start_date > end_date:
                        print("Starting must be lesser than ending date.")
                        continue

                    filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

                    if filtered_df.empty:
                        print(f"\nNo expenses found between {start_date.strftime("%Y-%m-%d")} - {end_date.strftime("%Y-%m-%d")}.")
                    else:
                        print(f"\n\nExpenses from {start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}:")
                        print(filtered_df.sort_values(by="Date", ascending=False).to_string(index=False))

                    break

            # Filter by Category
            elif filter_choice == '2':
                category = input("Enter the category (e.g., Food, Transport, Travel, Fuel): ").capitalize().strip()
                filtered_df = df[df["Category"].str.contains(category, case=False, na=False)]

                if filtered_df.empty:
                    print(f"\nNo expenses found for category: {category}.")
                else:
                    print(f"\nExpenses for category: {category}:")
                    print(filtered_df.sort_values(by="Date", ascending=False).to_string(index=False))

            else:
                print("\n**** All Expenses:")
                print(df.sort_values(by="Date", ascending=False).to_string(index=False))  # Displays the DataFrame as a table
    except pd.errors.ParserError:
        print("Error reading the CSV file. Please check the file format.")
    except FileNotFoundError:
        print("\nNo expenses recorded yet! Add an expense first.")
    except Exception as e:
        print(f"An error occurred: {e}")


def show_graphs(csv_file):
    try:
        df = pd.read_csv(csv_file)

        if df.empty:
            print("No expense data available to display.")
            return

        # Group data by category and sum amounts
        category_data = df.groupby("Category")["Amount"].sum()

        # Plot the bar chart
        plt.bar(category_data.index, category_data.values, color='skyblue')
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)  # Rotate labels for better visibility
        plt.tight_layout()  # Adjust layout
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def run():

    while True:
        print("\n** Personal Finance Tracker")
        choice = input("Enter your choice - 1 to Add Expense, 2 to View All Expenses as raw data, 3 to View Expense graphs, q to Exit: ")

        if choice == '1':
            expense = add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_graphs("expense_file.csv")
        elif choice.lower() == 'q':
            print("Thank you! Have a nice day :)")
            break
        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    run()