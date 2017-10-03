#!/usr/bin/env python
"""Modulo de funciones para manejar el archivo JSON de los hitos."""

import json


def read_json(json_file='hitos.json'):
    """Devuelve un diccionario con el archivo JSON."""
    try:
        milestone_dict = {}
        with open(json_file, 'r') as f:
            milestone_dict = json.loads(f.read())
    except Exception as e:
        raise
    return milestone_dict
