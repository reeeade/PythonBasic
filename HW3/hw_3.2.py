first_class = int(input("Учеников в первом классе: "))
second_class = int(input("Учеников во втором классе: "))
third_class = int(input("Учеников в третьем классе: "))
need = (first_class + 1) // 2 + (second_class + 1) // 2 + (third_class + 1) // 2
print("Необходимо закупить парт:", need, "шт.")
