import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleDonePastDueTradesBetweenLast3To12Months(mongoengine.Document, RuleModel):
    # code = mongoengine.StringField()
    # min = mongoengine.IntField()
    # max = mongoengine.IntField()
    # score = mongoengine.IntField()
    # desc = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'rulesDonePastDueTradesBetweenLast3To12Months'
    }

