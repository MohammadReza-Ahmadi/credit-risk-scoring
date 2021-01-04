import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleDonePastDueTradesBetweenLast3To12Months(mongoengine.Document, RuleModel):

    meta = {
        'db_alias': 'core',
        'collection': 'rulesDonePastDueTradesBetweenLast3To12Months'
    }

