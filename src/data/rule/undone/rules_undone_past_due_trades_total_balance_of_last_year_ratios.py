import mongoengine

from src.data.rule.rule_model import RuleModel


# نسبت مجموع مبالغ تعاملات سررسید گذشته خاتمه ‌نیافته به مجموع مبالغ تعاملات موفق کاربر در یکسال گذشته
class RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio(mongoengine.Document, RuleModel):
    min = mongoengine.FloatField()
    max = mongoengine.FloatField()
    meta = {
        'db_alias': 'core',
        'collection': 'rulesUnDonePastDueTradesTotalBalanceOfLastYearRatios'
    }
