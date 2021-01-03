import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleDoneTradesTotalBalanceRatio(mongoengine.Document, RuleModel):
    # code = mongoengine.StringField()
    min = mongoengine.FloatField()
    max = mongoengine.FloatField()
    # score = mongoengine.IntField()
    # desc = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'rulesDoneTradesAverageTotalBalance'
    }
