import mongoengine

from src.data.rule.rule_model import RuleModel


class RulesUnfixedReturnedChequesCountOfLast3Months(mongoengine.Document, RuleModel):
    meta = {
        'db_alias': 'core',
        'collection': 'rulesUnfixedReturnedChequesCountOfLast3Months'
    }
