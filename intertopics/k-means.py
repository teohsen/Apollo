from typing import List
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
import numpy as np

# Generating random data
a = np.random.multivariate_normal([-2, -2], [[1.0, 0], [0, 1.0]], 50).T
b = np.random.multivariate_normal([2, -2], [[0.5, 0], [0, 0.5]], 50).T
c = np.random.multivariate_normal([2, 3], [[1.0, 0], [0, 1.5]], 50).T
X = np.hstack((a, b, c))

# plt.scatter(X[0], X[1])


# K-means Implementation
def distance(u, v):
    # Lets use squred l2 distance
    return np.linalg.norm(u-v)


def calculate_centroid(points):
    return np.mean(points, axis=0)  # axis=0 to collapse the rows


def get_closest_cluster(point, centroids):
    closest_cluster = None
    min_distance = float('inf')
    for i, centroid in enumerate(centroids):
        if distance(point, centroid) < min_distance:
            min_distance = distance(point, centroid)
            closest_cluster = i
    return closest_cluster


def k_means(points: List, k: int, max_error: float = 0.1, max_iterations: int = 100):
    """
    K-means is a 2-stage algorithm

    :param points:
    :param k:
    :param max_error:
    :param max_iterations:
    :return:
    """
    # i --> cluster
    # j --> a point
    n = points.__len__()
    points_to_cluster = [0] * n  # Cluster that each point belongs to

    # Initialize Centroids
    # Step 1: Pick k random points from input to use as initial centroids
    centroids = np.random.randint(low=0, high=n, size=k)
    cluster_to_centroid = points[centroids]

    # while not converged:
    while max_iterations > 0:
        max_iterations -= 1

        # Map: i -> list of points j assigned to cluster i
        cluster_to_points = [[] for _ in range(k)]

        # assign each point to its nearest centroid's cluster
        for j in range(n):
            i = get_closest_cluster(points[j], cluster_to_centroid)
            points_to_cluster[j] = i
            cluster_to_points[i].append(j)

        # recalculate each centroid to cluster mean
        for i, points_i in enumerate(cluster_to_points):
            cluster_to_centroid[i] = calculate_centroid(points[points_i])

    # return assignment
    return points_to_cluster, cluster_to_centroid


points = X.T
result, centroids = k_means(points, k=4)

# Visualize
colourmap = np.array(["r", "g", "b", "m"])  # {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
plt.scatter(X[0], X[1], c=colourmap[result])
plt.scatter(centroids[:, 0], centroids[:, 1], c='pink', s=100, marker="*")
