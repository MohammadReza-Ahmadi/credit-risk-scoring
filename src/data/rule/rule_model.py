import mongoengine


class RuleModel:
    code = mongoengine.StringField()
    min = mongoengine.IntField()
    max = mongoengine.IntField()
    score = mongoengine.IntField()
    desc = mongoengine.StringField()

