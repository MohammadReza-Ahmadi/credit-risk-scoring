import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleUnfixedReturnedChequesCountOfMore12Months(mongoengine.Document, RuleModel):
    meta = {
        'db_alias': 'core',
        'collection': 'rulesUnfixedReturnedChequesCountOfMore12Months'
    }
