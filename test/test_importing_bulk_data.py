import unittest

from src import program
from src.data.done_trades import DoneTrade
from src.service import general_data_service as gs
from src.service.util import get_random_digits_str


class TestImportRandomBulkData(unittest.TestCase):
    def setUp(self):
        program.launch_app()
        #     lower = get_random_lowercase_str(3)
        #     print(lower)
        #     upper = get_random_uppercase_str(7)
        #     print(upper)
        #     letters = get_random_letters_str(9)
        #     print(letters)
        #     digits = get_random_digits_str(24)
        #     print(digits)
        #     punctuation = get_random_punctuation_str(11)
        #     print(punctuation)

    def test_get_bulk_data(self):
        done_trades: DoneTrade = DoneTrade.objects(user_id=1).all()
        # print(user.to_json())
        print("all doneTrades are loaded.")
        for dt in done_trades:
            print(dt.to_json())

    def test_import_done_trades_data(self):
        DoneTrade.drop_collection()
        for i in range(1):
            dt = DoneTrade()
            dt.user_id = 1
            dt.timely_trades_count_of_last_3_months = get_random_digits_str(2)
            dt.timely_trades_count_between_last_3_to_12_months = get_random_digits_str(2)
            dt.past_due_trades_count_of_last_3_months = get_random_digits_str(2)
            dt.past_due_trades_count_between_last_3_to_12_months = get_random_digits_str(2)
            dt.arrear_trades_count_of_last_3_months = get_random_digits_str(2)
            dt.arrear_trades_count_between_last_3_to_12_months = get_random_digits_str(2)
            dt.trades_total_balance = get_random_digits_str(9)
            dt.total_delay_days = get_random_digits_str(2)
            gs.save_document(dt)
            print("flowing document is saved: ", dt.to_json())
