import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleDoneArrearTradesOfLast3Months(mongoengine.Document, RuleModel):

    meta = {
        'db_alias': 'core',
        'collection': 'rulesDoneArrearTradesOfLast3Months'
    }

