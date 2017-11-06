"""module hug_hitos_iv."""
import hug
import hitos_iv

json_path = '../data/hitos.json'
hitos_iv_json = hitos_iv.read_json(json_path)


# === Get `/` ===
@hug.get('/')
def index():
    """Retunr web status."""
    return {'status': 'OK'}


# === Get `/all` ===
@hug.get('/all')
def get_all():
    """Return all milestones."""
    return hitos_iv.read_json(json_path)


# === Get `/number` ===
@hug.get('/number')
def milestone_number():
    """Return all milestones."""
    return hitos_iv.milestone_number(hitos_iv_json)


# === Get `/get/{id}` ===
@hug.get('/get/{id}')
def get_one(id: int):
    """Return one milestone."""
    return hitos_iv.get_milestone(hitos_iv_json, id)
