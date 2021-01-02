import mongoengine


class Profile(mongoengine.Document):
    user_id: mongoengine.LongField()
    has_kyc = mongoengine.BooleanField()
    military_service_status = mongoengine.StringField()
    sim_card_ownership = mongoengine.BooleanField()
    address_verification = mongoengine.BooleanField()
    membership_date = mongoengine.DateField()
    recommended_to_others_count = mongoengine.IntField()
    star_count = mongoengine.IntField()
    score = mongoengine.IntField()

    meta = {
        'db_alias': 'core',
        'collection': 'profiles'
    }
