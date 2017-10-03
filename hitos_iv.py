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


def milestone_number(milestone_dict):
    """Carga JSON file into a dictionary."""
    return len(milestone_dict['hitos'])


def get_milestone(milestone_dict, milestone_id):
    """Devuelve un hito en concreto."""
    try:
        milestone = {}
        milestone = milestone_dict['hitos'][milestone_id]
    except Exception as e:
        raise
    return milestone
