import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleUnDoneUndueTradesTotalBalanceOfLastYearRatio(mongoengine.Document, RuleModel):
    min = mongoengine.FloatField()
    max = mongoengine.FloatField()
    meta = {
        'db_alias': 'core',
        'collection': 'rulesUnDoneUndueTradesTotalBalanceOfLastYearRatios'
    }
