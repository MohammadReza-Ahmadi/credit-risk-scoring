import datetime
import unittest
from typing import List

import redis
from redis import StrictRedis

from data.rule.done.rules_done_arrear_trades_between_last_3_to_12_months import RuleDoneArrearTradesBetweenLast3To12Months
from infrastructure.constants import SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS
from infrastructure.caching.redis_caching import RedisCaching
# from infrastructure.redis_caching import RedisCaching
from infrastructure.backups.redis_caching_backup_3 import get_score_of_rules_done_arrear_trades_between_last_3_to_12_months, get_redis_connection
from program import create_db_connection


class TestRedisCaching(unittest.TestCase):
    rds: [StrictRedis] = None

    def setUp(self) -> None:
        create_db_connection()

    def test_cache_rules_done_arrear_trades_between_last_3_to_12_months_base_test(self):
        rds = RedisCaching().get_redis_connection()
        sample_range_dict = {20: 0, 5: 1, -5: 3, -10: 6, -20: 10, -30: 999}
        rds.zadd('sample_range', sample_range_dict)
        scores = rds.zrangebyscore('sample_range', 0, 999)
        actual = int(scores[0])
        expected = 20
        self.assertEqual(expected, actual)

        scores = rds.zrangebyscore('sample_range', 3, 999)
        actual = int(scores[0])
        expected = -5
        self.assertEqual(expected, actual)

        scores = rds.zrangebyscore('sample_range', 4, 999)
        actual = int(scores[0])
        expected = -10
        self.assertEqual(expected, actual)

        scores = rds.zrangebyscore('sample_range', 5, 999)
        actual = int(scores[0])
        expected = -10
        self.assertEqual(expected, actual)

        scores = rds.zrangebyscore('sample_range', 6, 999)
        actual = int(scores[0])
        expected = -10
        self.assertEqual(expected, actual)

        scores = rds.zrangebyscore('sample_range', 7, 999)
        actual = int(scores[0])
        expected = -20
        self.assertEqual(expected, actual)
        rds.delete('sample_range')

    def test_cache_and_get_rules_done_arrear_trades_of_last_3_months(self):
        rc = RedisCaching()
        rc.cache_rules()
        # test -0 #
        actual = rc.get_score_of_rules_done_arrear_trades_of_last_3_months(0)
        expected = 0
        self.assertEqual(expected, actual)
        # test -1 #
        actual = rc.get_score_of_rules_done_arrear_trades_of_last_3_months(1)
        expected = 10
        self.assertEqual(expected, actual)
        # test -2 #
        actual = rc.get_score_of_rules_done_arrear_trades_of_last_3_months(2)
        expected = 20
        self.assertEqual(expected, actual)
        # test -3 #
        actual = rc.get_score_of_rules_done_arrear_trades_of_last_3_months(3)
        expected = 30
        self.assertEqual(expected, actual)
        # test -4 #
        actual = rc.get_score_of_rules_done_arrear_trades_of_last_3_months(4)
        expected = 40
        self.assertEqual(expected, actual)
        # test -5 #
        actual = rc.get_score_of_rules_done_arrear_trades_of_last_3_months(12)
        expected = 40
        self.assertEqual(expected, actual)

    def test_cache_and_get_rules_done_arrear_trades_between_last_3_to_12_months(self):
        rc = RedisCaching()
        rc.cache_rules_done_arrear_trades_between_last_3_to_12_months()
        # test -1 #
        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(7)
        expected = -20
        self.assertEqual(expected, actual)
        # test -2 #
        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(12)
        expected = -30
        self.assertEqual(expected, actual)
        # test -3 #
        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(27)
        expected = -30
        self.assertEqual(expected, actual)
        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(0)
        expected = 20
        self.assertEqual(expected, actual)
        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(1)
        expected = 5
        self.assertEqual(expected, actual)
        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(2)
        expected = -5
        self.assertEqual(expected, actual)
        # test -2 #
        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(3)
        expected = -5
        self.assertEqual(expected, actual)

        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(4)
        expected = -10
        self.assertEqual(expected, actual)

        actual = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(6)
        expected = -10
        self.assertEqual(expected, actual)

    def test_cache_rules_done_trades_total_amount(self):
        rc = RedisCaching()
        rc.cache_rules_done_trades_average_total_amount()
        # test-1
        actual = rc.get_score_of_rules_done_trades_average_total_amount(0.001)
        expected = 10
        self.assertEqual(expected, actual)
        # test-2
        actual = rc.get_score_of_rules_done_trades_average_total_amount(0.501)
        expected = 20
        self.assertEqual(expected, actual)
        # test-3
        actual = rc.get_score_of_rules_done_trades_average_total_amount(1)
        expected = 20
        self.assertEqual(expected, actual)
        # test-4
        actual = rc.get_score_of_rules_done_trades_average_total_amount(1.001)
        expected = 30
        self.assertEqual(expected, actual)

    # ------- speed tests ------------------- #
    def test_read_and_find_speed_from_db(self):
        print('start reading ...')
        s = datetime.datetime.now()
        for i in range(10000):
            rules: List[RuleDoneArrearTradesBetweenLast3To12Months] = RuleDoneArrearTradesBetweenLast3To12Months.objects()
            for r in rules:
                if r.min <= 7 <= r.max:
                    socre = r.score
                    break

        e = datetime.datetime.now()
        print('end reading in: ', (e - s))

    def test_read_and_find_speed_from_cache_pure(self):
        print('start reading ...')
        s = datetime.datetime.now()

        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='', decode_responses=True)
        rds = redis.StrictRedis(connection_pool=pool)

        for i in range(1000):
            scores = rds.zrangebyscore(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, 7, 999)
            score = scores[0]

        e = datetime.datetime.now()
        print('end reading in: ', (e - s))

    def test_read_and_find_speed_from_cache_module(self):
        print('start reading ...')
        s = datetime.datetime.now()
        rds = get_redis_connection()
        for i in range(1000):
            score = get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(7, rds)

        e = datetime.datetime.now()
        print('end reading in: ', (e - s))

    def test_read_and_find_speed_from_cache_class(self):
        print('start reading ...')
        rc = RedisCaching()
        s = datetime.datetime.now()
        # rc.cache_rules()
        for i in range(10000):
            score = rc.get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(7)

        e = datetime.datetime.now()
        print('end reading in: ', (e - s))


if __name__ == '__main__':
    unittest.main()
