# ⚡ ZenStudy: The Energy-Aware Task Optimizer

**ZenStudy** is a command-line productivity tool designed for students who face academic burnout. Unlike traditional planners that only look at deadlines, ZenStudy uses a **weighted optimization algorithm** to match your current mental energy with the difficulty of your tasks.

## 🧠 The Problem
Most students struggle with "high-output" tasks when their mental energy is low, leading to burnout and frustration. This project was born from a need to manage study loads more humanely—optimizing for **mental state** rather than just **time**.

## 🚀 Key Features
* **Energy-Difficulty Matching:** Uses a mathematical formula to suggest the "best" task for your current state.
* **Data Persistence:** Automatically saves and loads your tasks using a local `tasks.json` file.
* **Urgency Weighting:** Prioritizes tasks that are due soon, but only if they fit your energy levels.
* **Dynamic Categories:** Automatically labels tasks as "Peak Performance," "Steady Work," or "Low-Stress/Recovery."

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Format:** JSON (for storage)
* **Libraries:** `os`, `json` (Built-in Python libraries)

## 💻 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ZenStudy.git](https://github.com/YOUR_USERNAME/ZenStudy.git)
   cd ZenStudy

2.Prerequisites:
 Ensure you have Python installed. You can check by running:
   python --version

3.Run the Application:
   python energy_planner.py

📖 How to Use:

 1.Add Your Tasks: Enter the name of your assignment (e.g., "Learn Japanese Kanji"), a difficulty rating (1-10), and an urgency rating (1-10).

 2.Check Your Energy: When you are ready to study, tell the app your current energy level (1 = Drained, 10 = Peak Performance).

 3.Get Optimized Suggestions: The app will calculate the "Cost" of each task using the formula:
  $$Score = |Energy - Difficulty| + (10 - Urgency)$$
  The app then recommends the tasks with the lowest scores, ensuring you aren't overworking yourself or wasting your high-energy hours on easy tasks.

Created by: Rishikesh Shashikant Kadam

Course: CSE -Vit Bhopal
