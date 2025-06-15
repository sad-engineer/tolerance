#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
import unittest

from tolerance.core.enumerations import AccuracyStandards, ToleranceFields
from tolerance.core.tolerance_cls import Tolerance


class TestTolerance(unittest.TestCase):
    def setUp(self):
        """Подготовка тестового окружения"""
        self.tolerance = Tolerance()

    def test_01_init_with_strings(self):
        """Тест инициализации из строк"""
        tolerance = Tolerance('H', '14')
        self.assertEqual(str(tolerance), 'H14')
        self.assertEqual(tolerance.field, ToleranceFields.H)
        self.assertEqual(tolerance.accuracy, AccuracyStandards.IT14)

    def test_02_init_with_enums(self):
        """Тест инициализации из enum"""
        tolerance = Tolerance(ToleranceFields.H, AccuracyStandards.IT14)
        self.assertEqual(str(tolerance), 'H14')
        self.assertEqual(tolerance.field, ToleranceFields.H)
        self.assertEqual(tolerance.accuracy, AccuracyStandards.IT14)

    def test_03_set_from_string(self):
        """Тест создания из строки"""
        tolerance = Tolerance.set_from_string('H14')
        self.assertEqual(str(tolerance), 'H14')
        self.assertEqual(tolerance.field, ToleranceFields.H)
        self.assertEqual(tolerance.accuracy, AccuracyStandards.IT14)

    def test_04_set_value(self):
        """Тест изменения значения"""
        tolerance = Tolerance.set_from_string('H14')
        tolerance.set_value('B5')
        self.assertEqual(str(tolerance), 'B5')
        self.assertEqual(tolerance.field, ToleranceFields.B)
        self.assertEqual(tolerance.accuracy, AccuracyStandards.IT5)

    def test_05_invalid_field(self):
        """Тест некорректного поля допуска"""
        with self.assertRaises(ValueError):
            Tolerance('W', '14')

    def test_06_invalid_accuracy(self):
        """Тест некорректного квалитета"""
        with self.assertRaises(ValueError):
            Tolerance('H', '99')

    def test_07_empty_string(self):
        """Тест пустой строки"""
        with self.assertRaises(ValueError):
            Tolerance.set_from_string('')

    def test_08_to_dict(self):
        """Тест преобразования в словарь"""
        tolerance = Tolerance.set_from_string('H14')
        expected = {'field': 'H', 'accuracy': '14'}
        self.assertEqual(tolerance.to_dict(), expected)

    def test_09_repr(self):
        """Тест строкового представления для отладки"""
        tolerance = Tolerance.set_from_string('H14')
        self.assertEqual(repr(tolerance), "Tolerance(field=H, accuracy=IT14)")

    def test_10_case_insensitive_field(self):
        """Тест регистронезависимости поля допуска"""
        tolerance = Tolerance('h', '14')
        self.assertEqual(tolerance.field, ToleranceFields.H)

    def test_11_accuracy_with_it_prefix(self):
        """Тест квалитета с префиксом IT"""
        tolerance = Tolerance('H', 'IT14')
        self.assertEqual(tolerance.accuracy, AccuracyStandards.IT14)

    def test_12_js_field(self):
        """Тест поля допуска JS"""
        tolerance = Tolerance('JS', '7')
        self.assertEqual(str(tolerance), 'JS7')
        self.assertEqual(tolerance.field, ToleranceFields.JS)
        self.assertEqual(tolerance.accuracy, AccuracyStandards.IT7)

    def test_13_empty_tolerance(self):
        """Тест пустого допуска"""
        tolerance = Tolerance()
        self.assertEqual(str(tolerance), '')
        self.assertEqual(tolerance.to_dict(), {})


if __name__ == '__main__':
    unittest.main()
