import mongoengine

from src.data.rule.rule_model import RuleModel


# تعداد تسهیلات مشکوک الوصول در جریان
class RuleSuspiciousLoansTotalCount(mongoengine.Document, RuleModel):
    meta = {
        'db_alias': 'core',
        'collection': 'rulesSuspiciousLoansTotalCount'
    }
