import bson
import mongoengine

from src.data.done_trades import DoneTrade
from src.service.util import filter_dict_by_id


def get_done_trades_for_user(user_id: bson.ObjectId) -> DoneTrade:
    done_trade = DoneTrade.objects(user_id=user_id).first()
    return done_trade


# def get_done_trades_for_user(user_id: bson.ObjectId) -> List[DoneTrade]:
#     done_trades = DoneTrade.objects(user_id=user_id).all()
#     return list(done_trades)

def update_by_field(done_trad: DoneTrade, field_name: str, value):
    done_trad.update(**{field_name: value})


def update_by_fields_dict(done_trad: DoneTrade, dic: dict):
    done_trad.update(**dic)


def update(done_trade: DoneTrade):
    dic = filter_dict_by_id(done_trade.to_mongo().to_dict())
    done_trade.update(**dic)


def update_by_document(done_trade: mongoengine.Document):
    dic = filter_dict_by_id(done_trade.to_mongo().to_dict())
    done_trade.update(**dic)

    # done_trade.update(**{"total_delay_days": "0"})
    # done_trade.update(**{DoneTrade.total_delay_days.name: done_trade.total_delay_days})
    # fields = {'user_id': 1, 'successful_timely_trades_count_of_last_3_months': 2, 'successful_past_due_trades_count_of_last_3_months': 1, 'successful_arrear_trades_count_of_last_3_months': 5, 'successful_timely_trades_count_between_last_3_to_12_months': 7, 'successful_past_due_trades_count_between_last_3_to_12_months': 2, 'successful_arrear_trades_count_between_last_3_to_12_months': 3, 'successful_trades_total_amount': 100000000.0, 'total_delay_days': 6}
    # done_trade.update(**fields)
