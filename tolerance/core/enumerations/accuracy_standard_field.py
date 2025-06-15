#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from enum import Enum


class AccuracyStandards(Enum):
    """Квалитеты точности обработки"""

    NONE = None
    IT01 = '01'
    IT0 = '0'
    IT1 = '1'
    IT2 = '2'
    IT3 = '3'
    IT4 = '4'
    IT5 = '5'
    IT6 = '6'
    IT7 = '7'
    IT8 = '8'
    IT9 = '9'
    IT10 = '10'
    IT11 = '11'
    IT12 = '12'
    IT13 = '13'
    IT14 = '14'
    IT15 = '15'
    IT16 = '16'
    IT17 = '17'

    @classmethod
    def get_display_names(cls) -> dict[str, str]:
        """
        Получить словарь с отображаемыми названиями квалитетов.

        Returns:
            dict[str, str]: Словарь {название: значение}
        """
        return {member.name: str(member.value) if member.value is not None else 'None' for member in cls}


if __name__ == "__main__":
    # Пример 1: Получение всех квалитетов
    print("Все квалитеты:")
    for standard in AccuracyStandards:
        print(f"{standard.name} = {standard.value}")
    print()

    # Пример 2: Получение конкретного квалитета
    print("Примеры конкретных квалитетов:")
    print(f"NONE = {AccuracyStandards.NONE.value}")
    print(f"IT01 = {AccuracyStandards.IT01.value}")
    print(f"IT14 = {AccuracyStandards.IT14.value}")
    print()

    # Пример 3: Сравнение квалитетов
    print("Сравнение квалитетов:")
    print(f"NONE == NONE: {AccuracyStandards.NONE == AccuracyStandards.NONE}")
    print(f"IT14 == IT14: {AccuracyStandards.IT14 == AccuracyStandards.IT14}")
    print(f"IT14 == IT15: {AccuracyStandards.IT14 == AccuracyStandards.IT15}")
    print()

    # Пример 4: Получение словаря отображаемых имен
    print("Словарь отображаемых имен:")
    display_names = AccuracyStandards.get_display_names()
    for name, value in list(display_names.items())[:5]:  # Показываем первые 5 элементов
        print(f"{name}: {value}")
    print("...")
    print()

    # Пример 5: Проверка наличия квалитета
    print("Проверка наличия квалитетов:")
    print(f"'NONE' in AccuracyStandards: {'NONE' in AccuracyStandards.__members__}")
    print(f"'IT14' in AccuracyStandards: {'IT14' in AccuracyStandards.__members__}")
    print(f"'IT18' in AccuracyStandards: {'IT18' in AccuracyStandards.__members__}")
    print()

    # Пример 6: Получение квалитета по имени
    print("Получение квалитета по имени:")
    try:
        standard = AccuracyStandards['NONE']
        print(f"AccuracyStandards['NONE'] = {standard.value}")
    except KeyError as e:
        print(f"Ошибка: {e}")

    try:
        standard = AccuracyStandards['IT14']
        print(f"AccuracyStandards['IT14'] = {standard.value}")
    except KeyError as e:
        print(f"Ошибка: {e}")

    try:
        standard = AccuracyStandards['IT18']
        print(f"AccuracyStandards['IT18'] = {standard.value}")
    except KeyError as e:
        print(f"Ошибка: {e}")
