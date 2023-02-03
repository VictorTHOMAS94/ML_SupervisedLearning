import random
import csv

# number of datapoints in the dataset
num_lines = 300

# number of columns in the dataset
num_cols = 6

# list to store the dataset
data = []

# mean values for each column
mean = [0, 5, 10, 15, 20, 25]

# standard deviation values for each column
std_dev = [1, 2, 3, 4, 5, 6]

# populate the dataset
for i in range(num_lines):
    line = []
    for j in range(num_cols):
        line.append(random.gauss(mean[j], std_dev[j]))
    data.append(line)

# change one column to integers
for i in range(num_lines):
    data[i][0] = int(data[i][0])

# change one column to floats
for i in range(num_lines):
    data[i][1] = float(data[i][1])

with open("artificial_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
