import mongoengine


class Cheque(mongoengine.Document):
    user_id = mongoengine.LongField()

    unfixed_returned_cheques_count_of_last_3_months = mongoengine.IntField()
    unfixed_returned_cheques_count_between_last_3_to_12_months = mongoengine.IntField()
    unfixed_returned_cheques_count_of_more_12_months = mongoengine.IntField()
    unfixed_returned_cheques_count_of_last_5_years = mongoengine.IntField()

    unfixed_returned_cheques_total_balance = mongoengine.DecimalField()

    meta = {
        'db_alias': 'core',
        'collection': 'cheques'
    }
