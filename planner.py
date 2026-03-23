from utils import get_weight

def generate_plan(subjects, daily_hours):
    for subject in subjects:
        weight = get_weight(subject["difficulty"])
        subject["priority"] = weight / subject["days"]

    total_priority = sum(s["priority"] for s in subjects)

    for subject in subjects:
        subject["hours"] = (subject["priority"] / total_priority) * daily_hours

    return subjects


def generate_multi_day_plan(subjects, daily_hours):
    plan = []

    max_days = max(sub["days"] for sub in subjects)

    for day in range(1, max_days + 1):
        active_subjects = [s for s in subjects if s["days"] >= day]

        daily_plan = generate_plan(active_subjects, daily_hours)

        plan.append({
            "day": day,
            "subjects": [s.copy() for s in daily_plan]
        })

    return plan
def update_progress(subjects):
    print("\n📌 Update Today's Progress:")

    for subject in subjects:
        done = input(f"Did you complete {subject['name']}? (yes/no): ")

        if done.lower() == "yes":
            subject["completed"] += 1

    return subjects
def generate_insights(subjects):
    print("\n📊 Insights:")

    for subject in subjects:
        if subject["completed"] < subject["days"] / 2:
            print(f"⚠️ You are behind in {subject['name']}")
        else:
            print(f"✅ Good progress in {subject['name']}")