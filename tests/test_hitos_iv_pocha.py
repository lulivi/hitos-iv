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
from pocha import describe, it

# imports locales
import __init__ as init
import hitos_iv

assert init


json_file_path = '../data/hitos.json'

mil_dict = hitos_iv.read_json(json_file_path)


# === Reader ===
@describe('hitos_iv reader test')
def test_read_json_pocha():

    @it('can verify if the JSON is not empty')
    def not_empty():
        assert hitos_iv.read_json(json_file_path) != {}


# === Number getter ===
@describe('hitos_iv milestone number test')
def test_milestone_number_pocha():

    @it('can verify if the number of milestones is 2')
    def correct_number():
        assert hitos_iv.milestone_number(mil_dict) == 2


# === Milestone getter ===
@describe('hitos_iv get milestone test')
def test_get_milestone_pocha():

    @it('can verify if milestone one is not empty')
    def first_milestone_not_empty():
        assert hitos_iv.get_milestone(mil_dict, 0) != {}

    @it('can verify if milestone two is not empty')
    def second_milestone_not_empty():
        assert hitos_iv.get_milestone(mil_dict, 1) != {}

    @it('can verify that you can not acces an invalid item')
    def cant_acces_wrong_index():
        try:
            hitos_iv.get_milestone(mil_dict, 2)
        except IndexError:
            assert True

#     @it('can verify if the JSON is not empty')
#     def test_milestone_number_pocha():
#         """Comprueba si el numero de milestones es correcto."""
#         mil_dict = hitos_iv.read_json(self.__json_file_path)
#         self.assertEqual(
#             hitos_iv.milestone_number(mil_dict), 2, 'Número correcto de hitos')
#
#     def test_get_milestone_pocha():
#         """Comprueba si devuelve un objeto milestone correcto."""
#         mil_dict = hitos_iv.read_json(self.__json_file_path)
#         self.assertFalse(
#             hitos_iv.get_milestone(mil_dict, 0) == {}, 'Hito no vacío')
#         self.assertFalse(
#             hitos_iv.get_milestone(mil_dict, 1) == {},
#             'Accede a indice correcto')
#         with self.assertRaises(IndexError):
#             hitos_iv.get_milestone(mil_dict, 2)
#
#
# if __name__ == '__main__':
    # unittest.main()
