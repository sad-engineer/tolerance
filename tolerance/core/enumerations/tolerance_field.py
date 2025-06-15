#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from enum import Enum


class ToleranceFields(Enum):
    """Поля допусков"""

    NONE = None
    # Прописные буквы
    A = 'A'
    B = 'B'
    C = 'C'
    CD = 'CD'
    D = 'D'
    E = 'E'
    EF = 'EF'
    F = 'F'
    FG = 'FG'
    G = 'G'
    H = 'H'
    JS = 'JS'
    J = 'J'
    K = 'K'
    M = 'M'
    N = 'N'
    P = 'P'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    V = 'V'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
    ZA = 'ZA'
    ZB = 'ZB'
    ZC = 'ZC'

    # Строчные буквы
    a = 'a'
    b = 'b'
    c = 'c'
    cd = 'cd'
    d = 'd'
    e = 'e'
    ef = 'ef'
    f = 'f'
    fg = 'fg'
    g = 'g'
    h = 'h'
    js = 'js'
    j = 'j'
    k = 'k'
    m = 'm'
    n = 'n'
    p = 'p'
    r = 'r'
    s = 's'
    t = 't'
    u = 'u'
    v = 'v'
    x = 'x'
    y = 'y'
    z = 'z'
    za = 'za'
    zb = 'zb'
    zc = 'zc'

    @classmethod
    def get_display_names(cls) -> dict[str, str]:
        """
        Получить словарь с отображаемыми названиями полей допусков.

        Returns:
            dict[str, str]: Словарь {название: название}
        """
        return {member.name: str(member.value) if member.value is not None else 'None' for member in cls}


if __name__ == "__main__":
    # Пример 1: Получение всех полей допусков
    print("Все поля допусков:")
    for field in ToleranceFields:
        print(f"{field.name} = {field.value}")
    print()

    # Пример 2: Получение конкретного поля допуска
    print("Примеры конкретных полей допусков:")
    print(f"NONE = {ToleranceFields.NONE.value}")
    print(f"H = {ToleranceFields.H.value}")
    print(f"js = {ToleranceFields.js.value}")
    print()

    # Пример 3: Сравнение полей допусков
    print("Сравнение полей допусков:")
    print(f"NONE == NONE: {ToleranceFields.NONE == ToleranceFields.NONE}")
    print(f"H == H: {ToleranceFields.H == ToleranceFields.H}")
    print(f"H == h: {ToleranceFields.H == ToleranceFields.h}")
    print()

    # Пример 4: Получение словаря отображаемых имен
    print("Словарь отображаемых имен:")
    display_names = ToleranceFields.get_display_names()
    for name, value in list(display_names.items())[:5]:  # Показываем первые 5 элементов
        print(f"{name}: {value}")
    print("...")
    print()

    # Пример 5: Проверка наличия поля допуска
    print("Проверка наличия полей допусков:")
    print(f"'NONE' in ToleranceFields: {'NONE' in ToleranceFields.__members__}")
    print(f"'H' in ToleranceFields: {'H' in ToleranceFields.__members__}")
    print(f"'X' in ToleranceFields: {'X' in ToleranceFields.__members__}")
    print(f"'W' in ToleranceFields: {'W' in ToleranceFields.__members__}")
    print()

    # Пример 6: Получение поля допуска по имени
    print("Получение поля допуска по имени:")
    try:
        field = ToleranceFields['NONE']
        print(f"ToleranceFields['NONE'] = {field.value}")
    except KeyError as e:
        print(f"Ошибка: {e}")

    try:
        field = ToleranceFields['H']
        print(f"ToleranceFields['H'] = {field.value}")
    except KeyError as e:
        print(f"Ошибка: {e}")

    try:
        field = ToleranceFields['W']
        print(f"ToleranceFields['W'] = {field.value}")
    except KeyError as e:
        print(f"Ошибка: {e}")
