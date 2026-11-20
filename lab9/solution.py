# Lab 9 - NumPy, Pandas & Matplotlib
import matplotlib
matplotlib.use("Agg")  # save figures to files instead of opening windows
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---- Part 1: NumPy ----
growth = np.array([4, 7, 5, 9, 6, 8])
average_growth = np.mean(growth)
maximum_growth = np.max(growth)
minimum_growth = np.min(growth)
total_growth = np.sum(growth)
print("Average growth:", average_growth)
print("Maximum growth:", maximum_growth)
print("Minimum growth:", minimum_growth)
print("Total growth:", total_growth)
assert (average_growth, maximum_growth, minimum_growth, total_growth) == (6.5, 9, 4, 39)

tall_plants = growth[growth > 5]
print(tall_plants)

# Task 1: Temperature monitoring
temperatures = np.array([22, 25, 21, 28, 24])
print("Average temperature:", np.mean(temperatures))
print("Highest:", np.max(temperatures), "Lowest:", np.min(temperatures))
hot = temperatures[temperatures > 23]
print("Above 23 C:", hot)
print("Days above 23 C:", np.sum(temperatures > 23))
assert np.sum(temperatures > 23) == 3

# ---- Part 2: Pandas ----
data = {
    "Plant": ["Rose", "Tulip", "Lily", "Rose", "Tulip"],
    "Initial_Height": [10, 12, 8, 11, 14],
    "Final_Height": [18, 20, 15, 17, 23],
    "Sunlight": [6, 7, 5, 8, 6],
}
plants_df = pd.DataFrame(data)
print(plants_df.head())
print("Shape:", plants_df.shape)
print("Columns:", plants_df.columns)

# The notebook's examples use a 'Height' column that this dataset does not have.
# The closest real column is Final_Height, so that is used here.
print(plants_df["Final_Height"])
taller_plants = plants_df[plants_df["Final_Height"] > 12]
print(taller_plants)

average_height = plants_df.groupby("Plant")["Final_Height"].mean()
print(average_height)

# Task 2
plants_df["Growth"] = plants_df["Final_Height"] - plants_df["Initial_Height"]
print(plants_df[["Plant", "Growth"]])
print(plants_df[plants_df["Growth"] > 7])
avg_growth = plants_df.groupby("Plant")["Growth"].mean()
print(avg_growth)
assert list(plants_df["Growth"]) == [8, 8, 7, 6, 9]

# ---- Part 3: Matplotlib ----
plants = ["Rose", "Tulip", "Lily"]
heights = [15, 20, 12]
plt.figure()
plt.bar(plants, heights)
plt.title("Plant Heights")
plt.xlabel("Plant")
plt.ylabel("Height (cm)")
plt.savefig("plant_heights_bar.png")
plt.close()

# Practice: four plants
names = ["Rose", "Tulip", "Lily", "Sunflower"]
final_heights = [15, 20, 12, 25]
plt.figure()
plt.bar(names, final_heights)
plt.title("Comparing Plant Heights")
plt.xlabel("Plant")
plt.ylabel("Height (cm)")
plt.savefig("plant_comparison_bar.png")
plt.close()

# Task 3: weekly growth line graph
weeks = [1, 2, 3, 4, 5]
weekly_growth = [3, 6, 9, 14, 20]
plt.figure()
plt.plot(weeks, weekly_growth, marker="o")
plt.title("Plant Growth Over Five Weeks")
plt.xlabel("Week")
plt.ylabel("Growth (cm)")
plt.grid(True)
plt.savefig("weekly_growth_line.png")
plt.close()

# ---- Part 4: Science fair ----
# Step 1
marks = {
    "Student": ["Asha", "Jess", "Meera", "Rohan", "Sara", "Dev"],
    "Physics": [85, 72, 95, 65, 88, 78],
    "Chemistry": [78, 88, 91, 70, 84, 76],
    "Biology": [92, 80, 89, 75, 90, 82],
}
students_df = pd.DataFrame(marks)
print(students_df)

# Step 2
physics = np.array(students_df["Physics"])
print("Average Physics:", np.mean(physics))
print("Highest Physics:", np.max(physics), "Lowest Physics:", np.min(physics))

# Step 3
students_df["Total"] = students_df[["Physics", "Chemistry", "Biology"]].sum(axis=1)
students_df["Average"] = students_df["Total"] / 3
print(students_df)
print("Average above 80:")
print(students_df[students_df["Average"] > 80])
top = students_df.loc[students_df["Average"].idxmax()]
print("Highest average:", top["Student"], round(top["Average"], 2))

# Step 4
plt.figure()
plt.bar(students_df["Student"], students_df["Average"])
plt.title("Average Score per Student")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.grid(axis="y")
plt.savefig("science_fair_averages.png")
plt.close()

# Step 5: answers
print("Q1 Highest Physics:", students_df.loc[students_df["Physics"].idxmax(), "Student"])
print("Q2 Average Physics:", round(np.mean(physics), 2))
print("Q3 Highest overall average:", top["Student"])
print("Q4 Students with average above 80:", int((students_df["Average"] > 80).sum()))

# Answer to "explain plants_df.groupby('Plant')['Height'].mean()":
# groupby('Plant') splits the rows into one group per plant name, ['Final_Height'] picks the
# column to average, and .mean() returns the average value for each group.
