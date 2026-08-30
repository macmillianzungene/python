# Student Grade Classifier that Collects a learner's marks for 3 subjects and produces a full report card.

# Collect learner name and marks
name = input("Enter learner's name: ")
subject1 = float(input("Enter mark for Subject 1: "))
subject2 = float(input("Enter mark for Subject 2: "))
subject3 = float(input("Enter mark for Subject 3: "))

# Calculate average
average = (subject1 + subject2 + subject3) / 3
average = round(average, 2)

# Assign letter grade based on average
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign Pass/Fail status
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Check each subject for intervention (below 40)
subjects = {
    "Subject 1": subject1,
    "Subject 2": subject2,
    "Subject 3": subject3
}

intervention_flags = []
for subject_name, mark in subjects.items():
    if mark < 40:
        intervention_flags.append(subject_name)

# Display the report card
print("\n========= REPORT CARD =========")
print(f"Learner Name: {name}")
print("--------------------------------")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print("--------------------------------")
print(f"Average: {average}")
print(f"Grade: {grade}")
print(f"Status: {status}")

if intervention_flags:
    flagged_subjects = ", ".join(intervention_flags)
    print(f"⚠ Needs Intervention: {flagged_subjects}")
else:
    print("No subjects flagged for intervention.")
print("================================")