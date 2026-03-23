import json
import os
from planner import generate_multi_day_plan, update_progress, generate_insights
import matplotlib.pyplot as plt

subjects = []

#  Check if data exists
if os.path.exists("data.json"):
    print("\n Existing plan found!")

    print("1. Continue existing plan")
    print("2. Create new plan")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        with open("data.json", "r") as f:
            subjects = json.load(f)

    elif choice == "2":
        subjects = []

    elif choice == "3":
        exit()

else:
    print("\n  No existing plan found. Create a new one.")
if not subjects:
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        name = input("Enter subject name: ")
        days = int(input("Days left: "))
        difficulty = input("Difficulty (easy/medium/hard): ")

        subjects.append({
            "name": name,
            "days": days,
            "difficulty": difficulty,
            "completed": 0
        })

    # Save new plan
    with open("data.json", "w") as f:
        json.dump(subjects, f, indent=4)
# Step 2: Save data (Phase 4)
with open("data.json", "w") as f:
    json.dump(subjects, f, indent=4)

# Step 3: Daily hours input
daily_hours = float(input("Enter daily study hours: "))

# Step 4: Generate plan
multi_plan = generate_multi_day_plan(subjects, daily_hours)

# Step 5: Display plan
print("\n  Your Smart Study Plan:\n")

for day in multi_plan:
    print(f"\nDay {day['day']}:")
    for sub in day["subjects"]:
        print(f"  {sub['name']} → {round(sub['hours'], 2)} hrs")
#  Graph for Day 1
day1 = multi_plan[0]

names = [s["name"] for s in day1["subjects"]]
hours = [s["hours"] for s in day1["subjects"]]

plt.bar(names, hours)
plt.xlabel("Subjects")
plt.ylabel("Hours")
plt.title("Day 1 Study Plan")
plt.show()
#  Update progress
subjects = update_progress(subjects)

with open("data.json", "w") as f:
    json.dump(subjects, f, indent=4)
generate_insights(subjects)
