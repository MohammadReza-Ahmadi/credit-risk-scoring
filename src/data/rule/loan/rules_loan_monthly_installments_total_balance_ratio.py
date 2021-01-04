import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleMonthlyInstallmentsTotalBalanceRatio(mongoengine.Document, RuleModel):
    min = mongoengine.FloatField()
    max = mongoengine.FloatField()
    meta = {
        'db_alias': 'core',
        'collection': 'rulesMonthlyInstallmentsTotalBalanceRatios'
    }
