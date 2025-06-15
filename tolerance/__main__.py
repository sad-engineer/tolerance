from tolerance import Tolerance
from tolerance.core.accuracy_standard_field import AccuracyStandards
from tolerance.core.tolerance_field import ToleranceFields

# Создание допуска разными способами:
tolerance1 = Tolerance('H', 14)  # из строки и числа
tolerance2 = Tolerance('H', '14')  # из двух строк
tolerance3 = Tolerance.set_from_string('H14')  # из одной строки
tolerance4 = Tolerance(ToleranceFields.H, AccuracyStandards.IT14)  # из enum


# Использование в классе:
class MyClass:
    def __init__(self):
        self.tolerance = Tolerance.set_from_string('H14')

    def set_tolerance(self, value: str):
        self.tolerance.set_value(value)


# Пример использования:
obj = MyClass()
print(obj.tolerance)  # Выведет: H14
obj.set_tolerance('H7')
print(obj.tolerance)  # Выведет: H7

tolerance = Tolerance.set_from_string('H14')
print(tolerance)
tolerance.set_value("B5")
print(tolerance)

# Проверка на некорректные значения
try:
    tolerance.set_value("")  # Пустая строка
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    tolerance.set_value("X99")  # Несуществующий квалитет
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    tolerance.set_value("W14")  # Несуществующее поле допуска
except ValueError as e:
    print(f"Ошибка: {e}")
