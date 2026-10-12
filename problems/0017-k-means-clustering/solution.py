
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = initial_centroids[:]

    for i in range(max_iterations):
        clusters = [[] for _ in range(k)]

        for point in points:
            distances = []
            for centroid in centroids:
                dist = sum((x-y)**2 for x, y in zip(point, centroid))
                distances.append(dist)

            nearest = distances.index(min(distances))
            clusters[nearest].append(point)

        new_centroids = []

        for j in range(k):
            if len(clusters[j]) == 0:
                new_centroids.append(centroids[j])
            else:
                mean = tuple(
                    sum(point[d] for point in clusters[j]) / len(clusters[j])
                    for d in range(len(centroids[j]))
                )
                new_centroids.append(mean)

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids
