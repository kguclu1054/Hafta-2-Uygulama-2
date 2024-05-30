import math

# 1. Noktaların Tanımlanması
points = [(2, 3), (4, 5), (1, 1), (7, 8), (9, 6)]

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini hesaplar."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# 3. Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
