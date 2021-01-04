import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleDoneTimelyTradesBetweenLast3To12Months(mongoengine.Document, RuleModel):

    meta = {
        'db_alias': 'core',
        'collection': 'rulesDoneTimelyTradesBetweenLast3To12Months'
    }

