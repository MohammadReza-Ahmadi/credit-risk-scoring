import mongoengine

from src.data.rule.rule_model import RuleModel


class RulesUnfixedReturnedChequesTotalBalanceRatio(mongoengine.Document, RuleModel):
    meta = {
        'db_alias': 'core',
        'collection': 'rulesUnfixedReturnedChequesTotalBalanceRatios'
    }
