import pandas as pd

# Student dataset
students = [
    {"name": "Ali", "math": 90, "science": 85, "english": 95, "average": 90.0},
    {"name": "Sara", "math": 80, "science": 75, "english": 88, "average": 81.0},
    {"name": "Ahmed", "math": 70, "science": 65, "english": 72, "average": 69.0},
    {"name": "Mariam", "math": 95, "science": 92, "english": 90, "average": 92.33},
    {"name": "Omar", "math": 78, "science": 82, "english": 80, "average": 80.0}
]

# Create DataFrame
df = pd.DataFrame(students)

print("===== STUDENT DATASET =====")
print(df)

# Dataset Information
print("\n===== DATASET INFO =====")
df.info()

# Statistical Summary
print("\n===== DATASET DESCRIPTION =====")
print(df.describe())

# Calculate Class Average using pandas
class_average = df["average"].mean()

print("\n===== CLASS AVERAGE =====")
print(round(class_average, 2))

# Students Above Class Average
above_average = df[df["average"] > class_average]

print("\n===== STUDENTS ABOVE CLASS AVERAGE =====")
print(above_average)

# Students Below Class Average
below_average = df[df["average"] < class_average]

print("\n===== STUDENTS BELOW CLASS AVERAGE =====")
print(below_average)

# Summary Table
summary = pd.DataFrame({
    "Metric": [
        "Number of Students",
        "Highest Average",
        "Lowest Average",
        "Class Average"
    ],
    "Value": [
        len(df),
        df["average"].max(),
        df["average"].min(),
        round(class_average, 2)
    ]
})

print("\n===== SUMMARY TABLE =====")
print(summary)

# Save dataset as JSON
df.to_json("students.json", orient="records", indent=4)

print("\nDataset saved successfully as students.json")
