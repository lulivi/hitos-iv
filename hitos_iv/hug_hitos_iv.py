"""module hug_hitos_iv."""
import hug
import hitos_iv

json_path = '../data/hitos.json'


@hug.get('/')
def index():
    """Retunr web status."""
    return {'status': 'OK'}


@hug.get('/all')
def get_all():
    """Return all milestones."""
    return hitos_iv.read_json(json_path)


@hug.get('/number')
def milestone_number():
    """Return all milestones."""
    milestones = hitos_iv.read_json(json_path)
    return hitos_iv.milestone_number(milestones)


@hug.get('/get/{id}')
def get_one(id: int):
    """Return one milestone."""
    milestones = hitos_iv.read_json(json_path)
    return hitos_iv.get_milestone(milestones, id)
