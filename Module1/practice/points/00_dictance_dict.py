def distance(p1, p2):
    return (((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5)


# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
