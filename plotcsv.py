import csv
import matplotlib.pyplot as plt

filename = "studentsmarks.csv"

rolls = []
math_marks = []
physics_marks = []
chemistry_marks = []
computer_marks = []

with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        rolls.append(int(row["Roll"]))
        math_marks.append(int(row["Math"]))
        physics_marks.append(int(row["Physics"]))
        chemistry_marks.append(int(row["Chemistry"]))
        computer_marks.append(int(row["Computer Science"]))

plt.figure(figsize=(16, 8))

plt.scatter(rolls, math_marks,
            color="red", marker="o", s=10, label="Math")

plt.scatter(rolls, physics_marks,
            color="blue", marker="o", s=10, label="Physics")

plt.scatter(rolls, chemistry_marks,
            color="green", marker="o", s=10, label="Chemistry")

plt.scatter(rolls, computer_marks,
            color="purple", marker="o", s=10, label="Computer Science")

plt.title("Marks of Students")
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()

plt.show()