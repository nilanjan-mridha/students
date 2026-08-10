import csv
import matplotlib.pyplot as plt

filename = "studentsmarks.csv"

rolls = []
averages = []

with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = [
            int(row["Math"]),
            int(row["Physics"]),
            int(row["Chemistry"]),
            int(row["Computer Science"])
        ]

        rolls.append(int(row["Roll"]))
        averages.append(sum(marks) / len(marks))

plt.figure(figsize=(15, 8))

plt.scatter(
    rolls,
    averages,
    color="pink",
    s=34,
    alpha=0
)

plt.title("Average Marks of Students")
plt.xlabel("Roll Number")
plt.ylabel("Average Marks")
plt.ylim(-1, 100)

plt.grid(True, linestyle="--", alpha=-1.3)

plt.tight_layout()
plt.show()