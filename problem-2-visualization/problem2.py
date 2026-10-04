import requests
import matplotlib.pyplot as plt

# API endpoint
url = "https://sainformatics.org/data/exams.json"

# Fetch data from API
response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()

# Select an exam
exam = data["intensive_2_exam_3_2026"]

# Get student scores
participants = exam["participants"]

# Calculate average score for each student
student_averages = {}

for student_id, scores in participants.items():
    if scores:
        average = sum(scores) / len(scores)
        student_averages[student_id] = average

# Display calculated averages
print("Student Average Scores:")

for student_id, average in student_averages.items():
    print(f"Student {student_id}: {average:.2f}")

# Create bar chart
student_ids = list(student_averages.keys())
averages = list(student_averages.values())

plt.figure(figsize=(12, 6))
plt.bar(student_ids, averages)

plt.xlabel("Student ID")
plt.ylabel("Average Score")
plt.title("Average Student Test Scores")

plt.xticks(rotation=90)
plt.tight_layout()

# Save chart
plt.savefig("student_average_scores.png")

# Display chart
plt.show()