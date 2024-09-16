class TrackableObject:
    def __init__(self, objectID):
        self.objectID = objectID
        self.centroids = []
        self.count = 0

    def update(self, centroid):
        self.centroids.append(centroid)
