from math import sqrt

def knn(k, dataset, newpoint):
    # Calculate distances and store them in a list
    distances = [(calculate_distance(newpoint, point), point.label) for point in dataset]
    
    # Sort the list of distances
    sorted_distances = sorted(distances, key=lambda x: x[0])
    
    # Get the labels of the k nearest neighbors
    k_nearest_labels = [label for _, label in sorted_distances[:k]]
    
    # Find the most common label among the k nearest neighbors
    most_common_label = max(set(k_nearest_labels), key=k_nearest_labels.count)
    
    return most_common_label

def calculate_distance(point1, point2):
    # Calculate Euclidean distance
    distance = sqrt((point1.d1 - point2.d1)**2 + (point1.d2 - point2.d2)**2)
    return distance



# Basit bir veri kümesi tanımlayalım
class Point:
    def __init__(self, d1, d2, label):
        self.d1 = d1
        self.d2 = d2
        self.label = label

# Veri kümesi
dataset = [
    Point(1, 2, 'A'),
    Point(2, 3, 'A'),
    Point(3, 3, 'B'),
    Point(6, 5, 'B'),
    Point(7, 8, 'B')
    
]

# Yeni bir nokta
newpoint = Point(2, 2, None)

# k-NN algoritmasını çalıştır
k = 3
predicted_label = knn(k, dataset, newpoint)

print(f"Yeni noktanın tahmin edilen etiketi: {predicted_label}")