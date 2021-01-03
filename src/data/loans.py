import mongoengine


class Loan(mongoengine.Document):
    user_id = mongoengine.LongField()

    loans_total_count = mongoengine.IntField()
    past_due_loans_total_count = mongoengine.IntField()
    arrear_loans_total_count = mongoengine.IntField()
    suspicious_loans_total_count = mongoengine.IntField()

    monthly_installments_total_balance = mongoengine.DecimalField()
    overdue_loans_total_balance = mongoengine.DecimalField()
    past_due_loans_total_balance = mongoengine.DecimalField()
    arrear_loans_total_balance = mongoengine.DecimalField()
    suspicious_loans_total_balance = mongoengine.DecimalField()

    meta = {
        'db_alias': 'core',
        'collection': 'loans'
    }
