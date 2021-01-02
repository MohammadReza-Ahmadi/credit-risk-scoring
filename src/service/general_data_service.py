import bson
import mongoengine

from src.data.done_trades import DoneTrade
from src.service.util import filter_dict_by_id


def get_document_by_user_id(doc: object, user_id: bson.ObjectId):
    if doc == DoneTrade.__name__:
        return DoneTrade.objects(user_id=user_id).first()


def save_document(doc: mongoengine.Document):
    doc.save()


def update_by_field(doc: mongoengine.Document, field_name: str, value):
    doc.update(**{field_name: value})


def update_by_fields_dict(doc: mongoengine.Document, dic: dict):
    doc.update(**dic)


def update_by_document(doc: mongoengine.Document):
    dic = filter_dict_by_id(doc.to_mongo().to_dict())
    doc.update(**dic)
