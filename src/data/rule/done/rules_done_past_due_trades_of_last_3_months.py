import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleDonePastDueTradesOfLast3Months(mongoengine.Document, RuleModel):

    meta = {
        'db_alias': 'core',
        'collection': 'rulesDonePastDueTradesOfLast3Months'
    }

