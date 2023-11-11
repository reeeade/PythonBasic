class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class TriangleChecker:
    @staticmethod
    def triangle_check(a, b, c):
        if any(type(i) not in [int, float] for i in [a, b, c]):
            return "Потрібно вводити тільки числа!"
        if any(i < 0 for i in [a, b, c]):
            return "З негативними числами нічого не вийде!"
        if (a + b) > c and (a + c) > b and (b + c) > a:
            return "Ура, можна побудувати трикутник! :)"
        else:
            return "Жаль, але з цього трикутник не зробити :("


class ExtTriangle(Triangle, TriangleChecker):
    def is_triangle(self):
        return TriangleChecker.triangle_check(self.a, self.b, self.c)


print("'''Можна побудувати'''".center(41, '-'))
triangle = ExtTriangle(3, 4, 5)
print(triangle.is_triangle().center(41))
print("'''З негативними числами'''".center(41, '-'))
triangle = ExtTriangle(-2, 4, 5)
print(triangle.is_triangle().center(41))
print("'''Не тільки числа'''".center(41, '-'))
triangle = ExtTriangle("4", 4, 2)
print(triangle.is_triangle().center(41))
print("'''Трикутник не зробити'''".center(41, '-'))
triangle = ExtTriangle(0, 4, 2)
print(triangle.is_triangle().center(41))
