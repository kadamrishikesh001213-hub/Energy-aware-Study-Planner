import json
import os

# File name for data persistence
DATA_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from a JSON file. Returns an empty list if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Allows the user to input a new task with Difficulty and Urgency ratings."""
    print("\n--- Add New Task ---")
    name = input("Task Name (e.g., Learn Kanji): ")
    
    # Validation to ensure we get numbers between 1-10
    try:
        difficulty = int(input("Difficulty Level (1-10, where 10 is hardest): "))
        urgency = int(input("Urgency Level (1-10, where 10 is due now): "))
        
        new_task = {
            "name": name,
            "difficulty": difficulty,
            "urgency": urgency
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Successfully added '{name}'!")
    except ValueError:
        print("Invalid input! Please use numbers 1-10.")

def get_recommendations(tasks):
    """The Optimization Core: Matches user energy to task difficulty."""
    if not tasks:
        print("\nNo tasks found! Add some first.")
        return

    try:
        energy = int(input("\nHow is your mental energy right now? (1-10): "))
        
        # Optimization Formula: |Energy - Difficulty| + (10 - Urgency)
        # We sort by the lowest 'score' (best match)
        recommended = sorted(tasks, key=lambda x: abs(x['difficulty'] - energy) + (10 - x['urgency']))
        
        print(f"\n--- Top 3 Optimized Suggestions for Energy Level {energy} ---")
        for i, task in enumerate(recommended[:3], 1):
            match_type = "Peak Performance" if task['difficulty'] > 7 else "Steady Work" if task['difficulty'] > 4 else "Low-Stress/Recovery"
            print(f"{i}. {task['name']} (Difficulty: {task['difficulty']}, Type: {match_type})")
            
    except ValueError:
        print("Please enter a number between 1 and 10.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n================================")
        print("   ENERGY-AWARE STUDY PLANNER   ")
        print("================================")
        print("1. Add a New Task")
        print("2. Get Optimized Recommendations")
        print("3. View All Tasks")
        print("4. Clear All Tasks")
        print("5. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            get_recommendations(tasks)
        elif choice == "3":
            print("\n--- All Pending Tasks ---")
            for t in tasks:
                print(f"- {t['name']} [Diff: {t['difficulty']}, Urg: {t['urgency']}]")
        elif choice == "4":
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == 'y':
                tasks = []
                save_tasks(tasks)
                print("All tasks cleared.")
        elif choice == "5":
            print("Goodbye! Don't forget to take a break.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
