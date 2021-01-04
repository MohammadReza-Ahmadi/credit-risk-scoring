import mongoengine

from src.data.rule.rule_model import RuleModel


# تعداد تسهیلات سررسید گذشته در جریان
class RulePastDueLoansTotalCount(mongoengine.Document, RuleModel):
    meta = {
        'db_alias': 'core',
        'collection': 'rulesPastDueLoansTotalCount'
    }
