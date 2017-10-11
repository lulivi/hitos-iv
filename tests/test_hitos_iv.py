#!/usr/bin/env python

# === Test del módulo Hitos IV ===
"""
Modulo para testear el archivo JSON de los hitos.

**Functions:**

* test_read_json
* test_milestone_number
* test_get_milestone
"""

# imports externos
import unittest

# imports locales
import __init__ as init
import hitos_iv

# === Clase test ===


class HitosIvTest(unittest.TestCase):
    """Clase para testing del modulo hitos_iv."""

    __json_file_path = '../data/hitos.json'

    def test_read_json(self):
        """Comprueba si lee correctamente el fichero."""
        self.assertFalse(
            hitos_iv.read_json(self.__json_file_path) == {},
            'Diccionario no vacío')

    def test_milestone_number(self):
        """Comprueba si el numero de milestones es correcto."""
        mil_dict = hitos_iv.read_json(self.__json_file_path)
        self.assertEqual(
            hitos_iv.milestone_number(mil_dict), 2, 'Número correcto de hitos')

    def test_get_milestone(self):
        """Comprueba si devuelve un objeto milestone correcto."""
        mil_dict = hitos_iv.read_json(self.__json_file_path)
        self.assertFalse(
            hitos_iv.get_milestone(mil_dict, 0) == {}, 'Hito no vacío')
        self.assertFalse(
            hitos_iv.get_milestone(mil_dict, 1) == {},
            'Accede a indice correcto')
        with self.assertRaises(IndexError):
            hitos_iv.get_milestone(mil_dict, 2)


if __name__ == '__main__':
    unittest.main()
