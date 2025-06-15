#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
import unittest

from tolerance.core.enumerations import AccuracyStandards


class TestAccuracyStandards(unittest.TestCase):
    def test_01_enum_values(self):
        """Тест значений enum"""
        self.assertEqual(AccuracyStandards.IT01.value, '01')
        self.assertEqual(AccuracyStandards.IT0.value, '0')
        self.assertEqual(AccuracyStandards.IT1.value, '1')
        self.assertEqual(AccuracyStandards.IT17.value, '17')
        self.assertEqual(AccuracyStandards.NONE.value, None)

    def test_02_enum_names(self):
        """Тест имен enum"""
        self.assertEqual(AccuracyStandards.IT01.name, 'IT01')
        self.assertEqual(AccuracyStandards.IT0.name, 'IT0')
        self.assertEqual(AccuracyStandards.IT1.name, 'IT1')
        self.assertEqual(AccuracyStandards.IT17.name, 'IT17')
        self.assertEqual(AccuracyStandards.IT14.name, 'IT14')
        self.assertEqual(AccuracyStandards.NONE.name, 'NONE')

    def test_03_get_display_names(self):
        """Тест получения отображаемых имен"""
        display_names = AccuracyStandards.get_display_names()
        self.assertIsInstance(display_names, dict)
        self.assertEqual(display_names['IT01'], '01')
        self.assertEqual(display_names['IT14'], '14')
        self.assertEqual(display_names['NONE'], 'None')

    def test_04_sequential_values(self):
        """Тест последовательности значений"""
        values = [standard.value for standard in AccuracyStandards if standard.value is not None]
        self.assertEqual(values[0], '01')  # IT01
        self.assertEqual(values[-1], '17')  # IT17

    def test_05_value_format(self):
        """Тест формата значений"""
        for standard in AccuracyStandards:
            if standard.value is None:
                # Для NONE проверяем, что значение действительно None
                self.assertIsNone(standard.value)
            else:
                # Для остальных значений проверяем, что это строка с цифрами
                self.assertIsInstance(standard.value, str)
                self.assertTrue(standard.value.isdigit() or standard.value == '01')


if __name__ == '__main__':
    unittest.main()
