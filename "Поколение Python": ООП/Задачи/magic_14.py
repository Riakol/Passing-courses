class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)) -> None:
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self) -> str:
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)
    
    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)
    
    def __invert__(self):
        r, g, b = [abs(c-255) for c in self.color]
        return ColoredPoint(self.y, self.x, (r, g, b))
    