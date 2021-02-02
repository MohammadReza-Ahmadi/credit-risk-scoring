import mongoengine


class Rule(mongoengine.Document):
    level = mongoengine.IntField()
    code = mongoengine.StringField()
    parent = mongoengine.StringField()
    title = mongoengine.StringField()
    impact_percent = mongoengine.FloatField()
    score = mongoengine.IntField()
    min = mongoengine.FloatField()
    max = mongoengine.FloatField()

    # parameterized constructor
    # def __init__(self, level, code: str, title: str, impact_percent: float, score: int = None, min_val: float = None, max_val: float = None):
    #     self.level = level
    #     self.code = code
    #     self.title = title
    #     self.impact_percent = impact_percent
    #     self.score = score
    #     self.min = min_val
    #     self.max = min_val if max_val is None else max_val

    meta = {
        'db_alias': 'core',
        'collection': 'rules'
    }
