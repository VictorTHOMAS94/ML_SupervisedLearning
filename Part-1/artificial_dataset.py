import csv
import random
import numpy as np


def generate_means_and_stds():
    means = np.random.uniform(low=0.0, high=5.0, size=6)
    stds = np.random.uniform(low=0.5, high=2.0, size=6)

    # Means and stds are different
    while len(np.unique(means)) < 6:
        means = np.random.uniform(low=0.0, high=5.0, size=6)
    while len(np.unique(stds)) < 6:
        stds = np.random.uniform(low=0.5, high=2.0, size=6)

    # At least one column has mean close to 2.5
    if np.abs(np.min(np.abs(means-2.5))) > 0.5:
        means[0] = 2.5

    return means, stds


def generate_data(means, stds, n_points=300):
    np.random.seed(0)
    data = np.zeros((n_points, 6))
    for i in range(6):
        data[:, i] = np.random.normal(
            loc=means[i], scale=stds[i], size=n_points)

    # At least one column contains integers
    data[:, 0] = np.round(data[:, 0])

    # At least one column contains floats
    data[:, 1] = data[:, 1] + 0.5

    # Generate positive and negative correlations
    data[:, 2] = 0.5 * data[:, 0] + 0.5 * data[:, 1]
    data[:, 3] = -0.5 * data[:, 0] - 0.5 * data[:, 1]

    # Generate a column with a correlation close to 0
    data[:, 4] = np.random.normal(loc=0, scale=1, size=n_points)

    return data


def save_to_csv(data):
    with open('artificial_dataset.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == '__main__':
    means, stds = generate_means_and_stds()
    data = generate_data(means, stds)
    save_to_csv(data)
