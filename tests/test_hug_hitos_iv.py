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
import hug
import hug_hitos_iv as hhitos

assert init


# === Clase test ===
class HugHitosIvTest(unittest.TestCase):
    """Clase para testing del modulo hitos_iv."""

    __json_file_path = '../data/hitos.json'

    def test_index(self):
        """Comprueba si el estado es correcto."""
        result = hug.test.get(hhitos, '/')

        self.assertEqual(result.status, '200 OK')
        self.assertEqual(result.data, {'status': 'OK'})

    def test_get_all(self):
        """Devuelve correctamente todos los hitos."""
        result = hug.test.get(hhitos, '/all')

        self.assertEqual(result.status, '200 OK')
        self.assertFalse(result.data == {})
        self.assertEqual(result.data['hitos'][0]['file'], '0.Repositorio')

    def test_milestone_number(self):
        """Devuelve el numero de hitos."""
        result = hug.test.get(hhitos, '/number')

        self.assertEqual(result.status, '200 OK')
        self.assertEqual(result.data, 2)

    def test_get_one(self):
        """Devuelve el numero de hitos."""
        result0 = hug.test.get(hhitos, '/get/%d' % 0)
        result1 = hug.test.get(hhitos, '/get/%d' % 1)

        self.assertEqual(result0.status, '200 OK')
        self.assertEqual(result1.status, '200 OK')
        self.assertEqual(result0.data['file'], '0.Repositorio')
        self.assertEqual(result1.data['file'], '1.Infraestructura')


if __name__ == '__main__':
    unittest.main()
