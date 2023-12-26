import matplotlib.pyplot as plt
import numpy as np

initial_data = [
    {"surname": "student1", "grades": {"math": 90, "english": 85, "history": 92, "science": 88, "art": 95}},
    {"surname": "student2", "grades": {"math": 88, "english": 92, "history": 78, "science": 85, "art": 90}},
    {"surname": "student3", "grades": {"math": 23, "english": 56, "history": 67, "science": 45, "art": 43}},
    {"surname": "student4", "grades": {"math": 56, "english": 13, "history": 34, "science": 68, "art": 67}},
    {"surname": "student5", "grades": {"math": 87, "english": 52, "history": 23, "science": 12, "art": 12}},
    {"surname": "student6", "grades": {"math": 83, "english": 34, "history": 13, "science": 23, "art": 24}},
    {"surname": "student7", "grades": {"math": 13, "english": 63, "history": 24, "science": 34, "art": 24}},
    {"surname": "student8", "grades": {"math": 88, "english": 85, "history": 78, "science": 45, "art": 32}},
    {"surname": "student9", "grades": {"math": 53, "english": 36, "history": 67, "science": 56, "art": 12}},
    {"surname": "student10", "grades": {"math": 24, "english": 45, "history": 65, "science": 78, "art": 16}}
]

average_grades = []

for student in initial_data:
    surname = student["surname"]
    grades = student["grades"]
    average_grade = sum(grades.values()) / len(grades)
    average_grades.append({"surname": surname, "average_grade": average_grade})

total_average = sum([student["average_grade"] for student in average_grades])
percentages = [student["average_grade"] / total_average * 100 for student in average_grades]
colors = plt.cm.viridis(np.linspace(0, 1, len(average_grades)))
plt.pie(percentages, labels=[student["surname"] for student in average_grades], autopct='%1.1f%%', colors=colors)
plt.title("Середні бали учнів відносно загальної суми середніх балів")
plt.legend()
plt.show()