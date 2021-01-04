import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleDoneTimelyTradesOfLast3Months(mongoengine.Document, RuleModel):

    meta = {
        'db_alias': 'core',
        'collection': 'rulesDoneTimelyTradesOfLast3Months'
    }

