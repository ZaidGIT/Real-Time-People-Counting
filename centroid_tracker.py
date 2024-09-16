from collections import OrderedDict
import numpy as np

class CentroidTracker:
    def __init__(self):
        self.nextObjectID = 0
        self.objects = OrderedDict()

    def update(self, detections):
        objects = OrderedDict()
        for (objectID, centroid) in self.objects.items():
            objects[objectID] = centroid

        for detection in detections:
            # Assuming detection is a bounding box (x, y, w, h)
            # You need to convert detection to centroid
            x, y, w, h = detection
            centroid = (x + w / 2, y + h / 2)

            # Add or update the tracked object
            objects[self.nextObjectID] = centroid
            self.nextObjectID += 1

        self.objects = objects
        return objects
