class Polygon:
    def __init__(self, sides_count):
        self.sides_count = sides_count

    def print_number_of_sides(self):
        print(f"It has {self.sides_count} sides")


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)


class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__(4)


class Pentagon(Polygon):
    def __init__(self):
        super().__init__(5)


class Hexagon(Polygon):
    def __init__(self):
        super().__init__(6)


Triangle().print_number_of_sides()
Pentagon().print_number_of_sides()
