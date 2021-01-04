import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleUnfixedReturnedChequesCountOfLast5Years(mongoengine.Document, RuleModel):
    meta = {
        'db_alias': 'core',
        'collection': 'rulesUnfixedReturnedChequesCountOfLast5Years'
    }
