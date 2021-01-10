import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleUnfixedReturnedChequesCountBetweenLast3To12Months(mongoengine.Document, RuleModel):
    meta = {
        'db_alias': 'core',
        'collection': 'rulesChequeUnfixedReturnedCountBetweenLast3To12Months'
    }
