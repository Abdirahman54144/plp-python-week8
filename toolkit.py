# Personal Mini-Toolkit Final Project
# Author: Abdirahman Diis Abdullahi
# This program combines menus, loops, lists, conditionals, and f-strings into an interactive toolkit.

import random

def number_guessing_game():
    """Tool 1: A number guessing game using loops and conditionals."""
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

def todo_list_manager():
    """Tool 2: A task manager using lists, loops, and conditionals."""
    print("\n--- Todo List Manager ---")
    tasks = []
    
    while True:
        action = input("\nOptions: [1] Add Task [2] View Tasks [3] Remove Task [4] Back to Main Menu\nChoose an option (1-4): ").strip()
        
        if action == "1":
            task = input("Enter the task description: ").strip()
            if task:
                tasks.append(task)
                print(f"'{task}' has been added successfully.")
        elif action == "2":
            print("\nCurrent Tasks:")
            if not tasks:
                print("Your task list is empty.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif action == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            try:
                rem_idx = int(input("Enter task number to remove: "))
                if 1 <= rem_idx <= len(tasks):
                    removed = tasks.pop(rem_idx - 1)
                    print(f"'{removed}' has been removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif action == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

def temperature_converter():
    """Tool 3: Converts temperatures between Celsius and Fahrenheit."""
    print("\n--- Temperature Converter ---")
    choice = input("Convert from: [1] Celsius to Fahrenheit [2] Fahrenheit to Celsius\nSelect (1 or 2): ").strip()
    
    if choice == "1":
        try:
            c = float(input("Enter temperature in Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c}°C is equal to {f:.1f}°F.")
        except ValueError:
            print("Invalid temperature input.")
    elif choice == "2":
        try:
            f = float(input("Enter temperature in Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f}°F is equal to {c:.1f}°C.")
        except ValueError:
            print("Invalid temperature input.")
    else:
        print("Invalid choice.")

def main():
    """Main function to run the interactive toolkit menu loop."""
    print("Welcome to your Personal Mini-Toolkit!")
    
    while True:
        print("\n==============================")
        print("   PERSONAL MINI-TOOLKIT      ")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. Todo List Manager")
        print("3. Temperature Converter")
        print("4. Quit")
        print("==============================")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_list_manager()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option from 1 to 4.")

if __name__ == "__main__":
    main()