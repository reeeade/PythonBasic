first_class = int(input("Учеников в первом классе: "))
second_class = int(input("Учеников во втором классе: "))
third_class = int(input("Учеников в третьем классе: "))
all_pupils = first_class + second_class + third_class
need = (all_pupils + 1) // 2
print("На", all_pupils, "учеников/ученика необходимо закупить парт:", need, "шт.")
