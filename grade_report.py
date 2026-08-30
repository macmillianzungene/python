# Grade Report Generator
# Processes a class of students, calculates grades/status for each,
# then produces a class summary report with a name-search feature.

# 1. Store at least 5 students as a list of dictionaries
students = [
    {"name": "Thandiwe Nkosi", "maths": 85, "english": 78, "science": 90},
    {"name": "John Smith", "maths": 45, "english": 55, "science": 38},
    {"name": "Sipho Zulu", "maths": 62, "english": 68, "science": 71},
    {"name": "Aisha Patel", "maths": 92, "english": 88, "science": 95},
    {"name": "Liam Botha", "maths": 55, "english": 49, "science": 60},
]

results = []

# 2. Loop over all students, calculate average, apply grade/status logic
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3
    average = round(average, 2)

    # Grade logic (same as Unit 5)
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

    # Status logic
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Build results list of dictionaries
    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

# 3. Calculate class statistics
all_averages = [r["average"] for r in results]
class_average = round(sum(all_averages) / len(all_averages), 2)
highest_mark = max(all_averages)
lowest_mark = min(all_averages)

# Find which student(s) got the highest/lowest average, for a nicer report
top_student = next(r["name"] for r in results if r["average"] == highest_mark)
bottom_student = next(r["name"] for r in results if r["average"] == lowest_mark)

# 4. Display the formatted class report
print("\n============ CLASS GRADE REPORT ============")
print(f"{'Name':<20}{'Average':<10}{'Grade':<8}{'Status'}")
print("-" * 48)
for r in results:
    print(f"{r['name']:<20}{r['average']:<10}{r['grade']:<8}{r['status']}")

print("\n--------------- CLASS STATISTICS ---------------")
print(f"Class Average: {class_average}")
print(f"Highest Average: {highest_mark} ({top_student})")
print(f"Lowest Average: {lowest_mark} ({bottom_student})")
print("==================================================")

# 5. While loop to let the user search for a student by name
while True:
    search_name = input("\nEnter a student name to search (or type 'exit' to quit): ").strip()

    if search_name.lower() == "exit":
        print("Goodbye!")
        break

    found = None
    for r in results:
        if r["name"].lower() == search_name.lower():
            found = r
            break

    if found:
        print(f"\nName: {found['name']}")
        print(f"Average: {found['average']}")
        print(f"Grade: {found['grade']}")
        print(f"Status: {found['status']}")
    else:
        print(f"No student found with the name '{search_name}'.")