#!/usr/bin/env python

# === Módulo Hitos IV ===
"""
Modulo para manejar el archivo JSON de los hitos.

**Functions:**

* read_json
* milestone_number
* get_milestone
"""

# imports externos
import json


# === Lectura ===

def read_json(json_file='./data/hitos.json'):
    """
    Guarda en un diccionario el arhcivo JSON que le pasamos como parametro.

    **Args:**

    * json_file - El nombre (ruta) del archivo JSON que va a leer (default
        'hitos.json').

    **Returns:**

    * Un diccionario en el que se guarda el archivo JSON.
    """
    try:
        milestone_dict = {}
        with open(json_file, 'r') as f:
            milestone_dict = json.loads(f.read())
    except IOError as e:
        raise
    return milestone_dict


# === Número de milestones ===

def milestone_number(milestone_dict):
    """
    Comprueba el número de milestones que hay.

    **Args:**

    * milestone_dict - Diccionario con los milestones.

    **Returns:**

    * Número de milestones del proyecto
    """
    return len(milestone_dict['hitos'])


# === Obtención de milestones ===

def get_milestone(milestone_dict, milestone_id):
    """
    Obtiene un milestones a través de su id.

    **Args:**

    * milestone_dict - Diccionario con los milestones.
    * milestone_id - ID del milestones que queremos obtener

    **Returns:**

    * Un diccionario con el milestone indicado.
    """
    try:
        milestone = {}
        milestone = milestone_dict['hitos'][milestone_id]
    except Exception as e:
        raise
    return milestone
