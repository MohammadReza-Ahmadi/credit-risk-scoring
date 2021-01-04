import mongoengine

from src.data.rule.rule_model import RuleModel


# نسبت مجموع کل مانده تسهیلات جاری به میانگین مجموع کل مانده تسهیلات جاری سایر کاربران
class RuleOverdueLoansTotalBalanceRatio(mongoengine.Document, RuleModel):
    min = mongoengine.FloatField()
    max = mongoengine.FloatField()
    meta = {
        'db_alias': 'core',
        'collection': 'rulesOverdueLoansTotalBalanceRatios'
    }
