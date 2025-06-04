# This is a solution for test task.

# Steps for solving the task:
# 1. Define abstract class Figure.
# 2. Implement subclasses like Triangle, Circle, Square, Rectangle inheriting from Figure.
# 3. Implement sub-factory functions like parsing line, etc.
# 4. Implement factory function.


import math


# Abstract class
class Figure:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.name} Perimeter {int(self.perimeter())} Area {int(self.area())}"


# Subclasses
class Square(Figure):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side * self.side


class Rectangle(Figure):
    def __init__(self, x1, y1, x2, y2):
        super().__init__("Rectangle")
        self.width = abs(x1 - x2)
        self.height = abs(y1 - y2)

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__("Triangle")
        self.a = math.dist((x1, y1), (x2, y2))
        self.b = math.dist((x2, y2), (x3, y3))
        self.c = math.dist((x3, y3), (x1, y1))

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Sub-factory fanctions
def parse_square(values):
    side = float(values[values.index("Side") + 1])
    return Square(side)


def parse_rectangle(values):
    topRight_index = values.index("TopRight") + 1
    bottomLeft_index = values.index("BottomLeft") + 1
    x1, y1 = float(values[topRight_index]), float(values[topRight_index + 1])
    x2, y2 = float(values[bottomLeft_index]), float(values[bottomLeft_index + 1])
    return Rectangle(x1, y1, x2, y2)


def parse_circle(values):
    radius = float(values[values.index("Radius") + 1])
    return Circle(radius)


def parse_triangle(values):
    p1_index = values.index("Point1") + 1
    p2_index = values.index("Point2") + 2
    p3_index = values.index("Point3") + 3

    x1, y1 = float(values[p1_index]), float(values[p1_index + 1])
    x2, y2 = float(values[p2_index]), float(values[p2_index + 1])
    x3, y3 = float(values[p3_index]), float(values[p3_index + 1])

    return Triangle(x1, y1, x2, y2, x3, y3)


def create_shape(line):
    values = line.strip().split()

    shape = values[0]

    if shape == "Square":
        return parse_square(values)
    elif shape == "Rectangle":
        return parse_rectangle(values)
    elif shape == "Circle":
        return parse_circle(values)
    elif shape == "Triangle":
        return parse_triangle(values)
    else:
        raise ValueError(f"Unknown shape: {shape}")


# Factory function
def main():
    input_lines = []
    output_lines = []

    filename = input("Enter filename (or leave empty to use manual input): ").strip()

    if filename:
        try:
            with open(filename, 'r') as f:
                input_lines = f.read().strip().split('\n')
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return
    else:
        print("Enter shape data (one per line). Type 'END' when done:")
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            input_lines.append(line)

    for line in input_lines:
        if line.strip():
            try:
                shape_obj = create_shape(line)
                output = str(shape_obj)
                print(output)
                output_lines.append(output)
            except Exception as e:
                error_msg = f"Could not parse line: {line}. Error: {e}"
                print(error_msg)
                output_lines.append(error_msg)

    with open("results.txt", "w") as f:
        for line in output_lines:
            f.write(line + "\n")

    print("\n Output saved to results.txt")


if __name__ == "__main__":
    main()
