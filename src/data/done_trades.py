import mongoengine


class DoneTrade(mongoengine.Document):
    user_id = mongoengine.LongField()
    calculation_start_date = mongoengine.DateField()

    timely_trades_count_of_last_3_months = mongoengine.IntField()
    past_due_trades_count_of_last_3_months = mongoengine.IntField()
    arrear_trades_count_of_last_3_months = mongoengine.IntField()

    timely_trades_count_between_last_3_to_12_months = mongoengine.IntField()
    past_due_trades_count_between_last_3_to_12_months = mongoengine.IntField()
    arrear_trades_count_between_last_3_to_12_months = mongoengine.IntField()

    trades_total_amount = mongoengine.DecimalField()

    total_delay_days = mongoengine.IntField()

    meta = {
        'db_alias': 'core',
        'collection': 'doneTrades'
    }
