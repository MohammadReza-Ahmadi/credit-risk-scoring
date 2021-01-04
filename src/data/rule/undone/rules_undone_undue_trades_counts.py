import mongoengine

from src.data.rule.rule_model import RuleModel


# تعداد تعاملات جاری سررسید نشده
class RuleUnDoneUndueTradesCount(mongoengine.Document, RuleModel):
    meta = {
        'db_alias': 'core',
        'collection': 'rulesUnDoneUndueTradesCounts'
    }
