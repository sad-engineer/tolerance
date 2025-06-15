#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
import unittest

from tolerance.core.enumerations import ToleranceFields


class TestToleranceFields(unittest.TestCase):
    def test_01_enum_values(self):
        """Тест значений enum"""
        self.assertIsNone(ToleranceFields.NONE.value)
        self.assertEqual(ToleranceFields.A.value, 'A')
        self.assertEqual(ToleranceFields.H.value, 'H')
        self.assertEqual(ToleranceFields.ZC.value, 'ZC')
        self.assertEqual(ToleranceFields.a.value, 'a')
        self.assertEqual(ToleranceFields.zc.value, 'zc')

    def test_02_enum_names(self):
        """Тест имен enum"""
        self.assertEqual(ToleranceFields.NONE.name, 'NONE')
        self.assertEqual(ToleranceFields.A.name, 'A')
        self.assertEqual(ToleranceFields.CD.name, 'CD')
        self.assertEqual(ToleranceFields.js.name, 'js')
        self.assertEqual(ToleranceFields.za.name, 'za')

    def test_03_get_display_names(self):
        """Тест получения отображаемых имен"""
        display_names = ToleranceFields.get_display_names()
        self.assertIsInstance(display_names, dict)
        self.assertEqual(len(display_names), 57)  # Всего 56 полей допусков + NONE
        self.assertEqual(display_names['NONE'], 'None')
        self.assertEqual(display_names['A'], 'A')
        self.assertEqual(display_names['H'], 'H')
        self.assertEqual(display_names['a'], 'a')
        self.assertEqual(display_names['zc'], 'zc')

    def test_04_enum_members(self):
        """Тест наличия всех необходимых членов enum"""
        expected_fields = {
            'NONE',
            'A',
            'B',
            'C',
            'CD',
            'D',
            'E',
            'EF',
            'F',
            'FG',
            'G',
            'H',
            'JS',
            'J',
            'K',
            'M',
            'N',
            'P',
            'R',
            'S',
            'T',
            'U',
            'V',
            'X',
            'Y',
            'Z',
            'ZA',
            'ZB',
            'ZC',
            'a',
            'b',
            'c',
            'cd',
            'd',
            'e',
            'ef',
            'f',
            'fg',
            'g',
            'h',
            'js',
            'j',
            'k',
            'm',
            'n',
            'p',
            'r',
            's',
            't',
            'u',
            'v',
            'x',
            'y',
            'z',
            'za',
            'zb',
            'zc',
        }
        actual_fields = {field.name for field in ToleranceFields}
        self.assertEqual(actual_fields, expected_fields)

    def test_05_value_equals_name(self):
        """Тест соответствия значений именам"""
        for field in ToleranceFields:
            if field.name == 'NONE':
                self.assertIsNone(field.value)
            else:
                self.assertEqual(field.value, field.name)


if __name__ == '__main__':
    unittest.main()
