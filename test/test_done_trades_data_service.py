import unittest

import mongoengine

from src.data.done_trades import DoneTrade
from src.service import general_data_service as gs


class TestDoneTradesDataService(unittest.TestCase):

    def setUp(self):
        mongoengine.register_connection('core', 'credit-scoring')
        print("credit-scoring db connection is done in test class running.")

    def test_get_done_trades_for_user(self):
        # done_trade = dts.get_done_trades_for_user(1)
        done_trade = gs.get_document_by_user_id(DoneTrade.__name__, 1)
        print(done_trade.to_json())

    def test_update_by_document(self):
        # done_trade = dts.get_done_trades_for_user(1)
        done_trade = gs.get_document_by_user_id(DoneTrade.__name__, 1)
        print("before update: total_delay_days=", done_trade.total_delay_days)
        done_trade.total_delay_days = 15
        print(done_trade.to_json())
        # print(json.loads(done_trade.to_json()))
        # dts.update(done_trade)
        # dts.update_by_document(done_trade)
        gs.update_by_document(done_trade)
        print("after update: total_delay_days=", done_trade.total_delay_days)
        print(done_trade.to_json())

    def test_update_by_document_field(self):
        # done_trade = dts.get_done_trades_for_user(1)
        done_trade = gs.get_document_by_user_id(DoneTrade.__name__, 1)
        print("before update: total_delay_days=", done_trade.total_delay_days)
        print(done_trade.to_json())
        # dts.update_by_field(done_trade, DoneTrade.total_delay_days.name, 23)
        gs.update_by_field(done_trade, DoneTrade.total_delay_days.name, 23)
        done_trade = gs.get_document_by_user_id(DoneTrade.__name__, 1)
        print("after update: total_delay_days=", done_trade.total_delay_days)
        print(done_trade.to_json())

    def test_update_by_fields_dict(self):
        # done_trade = dts.get_done_trades_for_user(1)
        done_trade = gs.get_document_by_user_id(DoneTrade.__name__, 1)
        print("before update: total_delay_days=", done_trade.total_delay_days)
        print(done_trade.to_json())

        fields_dict = {
            DoneTrade.total_delay_days.name: 10,
            DoneTrade.past_due_trades_count_of_last_3_months.name: 11,
            DoneTrade.timely_trades_count_between_last_3_to_12_months.name: 12,
        }

        # dts.update_by_fields_dict(done_trade, fields_dict)
        gs.update_by_fields_dict(done_trade, fields_dict)
        done_trade = gs.get_document_by_user_id(DoneTrade.__name__, 1)
        print("after update: total_delay_days=", done_trade.total_delay_days)
        print(done_trade.to_json())


if __name__ == '__main__':
    unittest.main()
