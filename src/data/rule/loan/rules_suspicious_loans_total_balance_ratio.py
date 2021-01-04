import mongoengine

from src.data.rule.rule_model import RuleModel


# نسبت مجموع کل مانده تسهیلات مشکوک‌الوصول به مجموع کل اصل و سود تسهیلات در جریان
class RuleSuspiciousLoansTotalBalanceRatio(mongoengine.Document, RuleModel):
    min = mongoengine.FloatField()
    max = mongoengine.FloatField()
    meta = {
        'db_alias': 'core',
        'collection': 'rulesSuspiciousLoansTotalBalanceRatios'
    }
