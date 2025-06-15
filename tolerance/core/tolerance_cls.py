#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Union

from tolerance.core.enumerations import AccuracyStandards
from tolerance.core.enumerations import ToleranceFields


class Tolerance:
    """Класс для работы с полями допусков и квалитетами точности"""

    def __init__(
        self,
        field: Union[str, ToleranceFields] = ToleranceFields.NONE,
        accuracy: Union[str, AccuracyStandards] = AccuracyStandards.NONE,
    ):
        """
        Инициализация допуска.

        Args:
            field (Union[str, ToleranceFields], optional): Поле допуска (например, 'H' или ToleranceFields.H)
            accuracy (Union[str, AccuracyStandards], optional): Квалитет точности
            (например, '14' или AccuracyStandards.IT14)
        """
        self.field = None
        self.accuracy = None

        if field is not None and accuracy is not None:
            self.field = self._parse_field(field)
            self.accuracy = self._parse_accuracy(accuracy)

    @staticmethod
    def _parse_field(field: Union[str, ToleranceFields]) -> ToleranceFields:
        """Преобразование поля допуска в enum"""
        if isinstance(field, ToleranceFields):
            return field

        # Ищем поле допуска по имени (регистронезависимо)
        field = field.upper()
        for member in ToleranceFields:
            if member.name == field:
                return member
        raise ValueError(f"Неизвестное поле допуска: {field}")

    @staticmethod
    def _parse_accuracy(accuracy: Union[str, AccuracyStandards]) -> AccuracyStandards:
        """Преобразование квалитета в enum"""
        if isinstance(accuracy, AccuracyStandards):
            return accuracy

        # Преобразуем строку в квалитет
        if isinstance(accuracy, str):
            accuracy = accuracy.strip()
            if accuracy.startswith('IT'):
                accuracy = accuracy[2:]

            # Ищем квалитет по значению
            for member in AccuracyStandards:
                if member.value == accuracy:
                    return member
        raise ValueError(f"Неизвестный квалитет: {accuracy}")

    def __str__(self) -> str:
        """Строковое представление допуска"""
        if self.field is None or self.accuracy is None:
            return ""
        if self.field == ToleranceFields.NONE or self.accuracy == AccuracyStandards.NONE:
            return ""
        return f"{self.field.value}{self.accuracy.value}"

    def __repr__(self) -> str:
        """Представление для отладки"""
        if self.field is None or self.accuracy is None:
            return "Tolerance()"
        return f"Tolerance(field={self.field.name}, accuracy=IT{self.accuracy.value})"

    @classmethod
    def set_from_string(cls, value: str) -> 'Tolerance':
        """
        Создание допуска из строки вида 'H14'.

        Args:
            value (str): Строка в формате 'H14'

        Returns:
            Tolerance: Объект допуска
        """
        if not value:
            raise ValueError("Пустая строка не может быть допуском")

        # Разделяем строку на поле допуска и квалитет
        field_str = value[0]
        accuracy_str = value[1:]

        tolerance = cls()
        tolerance.field = tolerance._parse_field(field_str)
        tolerance.accuracy = tolerance._parse_accuracy(accuracy_str)
        return tolerance

    def set_value(self, value: str) -> None:
        """
        Изменение допуска из строки вида 'H14'.

        Args:
            value (str): Строка в формате 'H14'
        """
        if not value:
            raise ValueError("Пустая строка не может быть допуском")

        # Разделяем строку на поле допуска и квалитет
        field_str = value[0]
        accuracy_str = value[1:]

        self.field = self._parse_field(field_str)
        self.accuracy = self._parse_accuracy(accuracy_str)

    def to_dict(self) -> dict:
        """
        Преобразование в словарь.

        Returns:
            dict: Словарь с полями допуска и квалитета
        """
        if self.field is None or self.accuracy is None:
            return {}
        if self.field == ToleranceFields.NONE or self.accuracy == AccuracyStandards.NONE:
            return {}
        return {'field': self.field.value, 'accuracy': self.accuracy.value}


if __name__ == "__main__":
    print("Пример 1: Создание допуска разными способами")
    print("-" * 50)

    # Создание из строки и числа
    t1 = Tolerance('H', '14')
    print(f"Tolerance('H', '14') = {t1}")

    # Создание из enum
    t2 = Tolerance(ToleranceFields.H, AccuracyStandards.IT14)
    print(f"Tolerance(ToleranceFields.H, AccuracyStandards.IT14) = {t2}")

    # Создание из строки
    t3 = Tolerance.set_from_string('H14')
    print(f"Tolerance.set_from_string('H14') = {t3}")
    print()

    print("Пример 2: Изменение допуска")
    print("-" * 50)
    t = Tolerance.set_from_string('H14')
    print(f"Исходный допуск: {t}")
    t.set_value('B5')
    print(f"После изменения: {t}")
    print()

    print("Пример 3: Преобразование в словарь")
    print("-" * 50)
    t = Tolerance.set_from_string('H14')
    print(f"Допуск: {t}")
    print(f"Словарь: {t.to_dict()}")
    print()

    print("Пример 4: Обработка ошибок")
    print("-" * 50)
    try:
        t = Tolerance.set_from_string('')
        print(f"Пустая строка: {t}")
    except ValueError as e:
        print(f"Ошибка при пустой строке: {e}")

    try:
        t = Tolerance.set_from_string('X99')
        print(f"Несуществующий квалитет: {t}")
    except ValueError as e:
        print(f"Ошибка при несуществующем квалитете: {e}")

    try:
        t = Tolerance.set_from_string('W14')
        print(f"Несуществующее поле допуска: {t}")
    except ValueError as e:
        print(f"Ошибка при несуществующем поле допуска: {e}")
    print()

    print("Пример 5: Использование в классе")
    print("-" * 50)

    class MyClass:
        def __init__(self):
            self.tolerance = Tolerance.set_from_string('H14')

        def set_tolerance(self, value: str):
            self.tolerance.set_value(value)

        def __str__(self):
            return f"Объект с допуском {self.tolerance}"

    obj = MyClass()
    print(f"Создан объект: {obj}")
    obj.set_tolerance('B5')
    print(f"После изменения допуска: {obj}")

    print("Пример 6")
    print("-" * 50)
    t1 = Tolerance('JS', '7')
    print(f"Tolerance('JS', '7') = {t1}")
    print(f"Словарь: {t1.to_dict()}")
