class TriangleChecker:
    @staticmethod
    def triangle_check(a, b, c):
        if any(i < 0 for i in [a, b, c]):
            return "З негативними числами нічого не вийде!"
        if any(type(i) not in [int, float] for i in [a, b, c]):
            return "Потрібно вводити тільки числа!"
        if (a + b) > c and (a + c) > b and (b + c) > a:
            return "Ура, можна побудувати трикутник! :)"
        else:
            return "Жаль, але з цього трикутник не зробити :("


triangle1 = TriangleChecker.triangle_check(3, 4, 5)
print(triangle1)
