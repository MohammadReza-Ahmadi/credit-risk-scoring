from typing import List

import redis
from redis import StrictRedis

from data.rule.done.rules_done_arrear_trades_between_last_3_to_12_months import RuleDoneArrearTradesBetweenLast3To12Months
from data.rule.done.rules_done_arrear_trades_of_last_3_months import RuleDoneArrearTradesOfLast3Months
from data.rule.done.rules_done_past_due_trades_between_last_3_to_12_months import RuleDonePastDueTradesBetweenLast3To12Months
from data.rule.done.rules_done_past_due_trades_of_last_3_months import RuleDonePastDueTradesOfLast3Months
from data.rule.done.rules_done_timely_trades_between_last_3_to_12_months import RuleDoneTimelyTradesOfLast3Months
from data.rule.done.rules_done_timely_trades_of_last_3_months import RuleDoneTimelyTradesBetweenLast3To12Months
from data.rule.done.rules_done_trades_average_delay_days_ratio import RuleDoneTradesAverageDelayDaysRatio
from data.rule.done.rules_done_trades_total_balance_ratio import RuleDoneTradesTotalBalanceRatio
from infrastructure.constants import redis_password, SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_max_val, rules_min_val, \
    SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS, SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, \
    SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, \
    SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, SET_RULES_DONE_TRADES_AVERAGE_DELAY_DAYS, SET_RULES_DONE_TRADES_AVERAGE_TOTAL_AMOUNT


# noinspection DuplicatedCode
class RedisCaching:
    recreate_caches = True
    rds: [StrictRedis] = None

    def __init__(self):
        try:
            pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password=redis_password, decode_responses=True)
            self.rds = redis.StrictRedis(connection_pool=pool)
            print("credit-scoring redis connection is established.")
        except Exception as e:
            print(e)

    def cache_rules(self):
        self.cache_rules_done_arrear_trades_of_last_3_months()
        self.cache_rules_done_arrear_trades_between_last_3_to_12_months()
        self.cache_rules_done_past_due_trades_of_last_3_months()
        self.cache_rules_done_past_due_trades_between_last_3_to_12_months()
        self.cache_rules_done_timely_trades_of_last_3_months()
        self.cache_rules_done_timely_trades_between_last_3_to_12_months()
        self.cache_rules_done_trades_average_delay_days()
        self.cache_rules_done_trades_average_total_amount()

    # ---------------------------- cache methods ----------------------------------- #
    def cache_rules_done_arrear_trades_of_last_3_months(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS)
        if not bool(self.rds.zcount(SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS, rules_min_val, rules_max_val)):
            rules: List[RuleDoneArrearTradesOfLast3Months] = RuleDoneArrearTradesOfLast3Months.objects()
            rdict = {}
            for r in rules:
                rdict.__setitem__(r.score, r.max)
            self.rds.zadd(SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS, rdict)
        print('caching rules_done_arrear_trades_of_last_3_months are done.')

    def cache_rules_done_arrear_trades_between_last_3_to_12_months(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_min_val, rules_max_val)):
            rules: List[RuleDoneArrearTradesBetweenLast3To12Months] = RuleDoneArrearTradesBetweenLast3To12Months.objects()
            rdict = {}
            for r in rules:
                rdict.__setitem__(r.score, r.max)
            self.rds.zadd(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rdict)
        print('caching rules_done_arrear_trades_between_last_3_to_12_months are done.')

    def cache_rules_done_past_due_trades_of_last_3_months(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, rules_min_val, rules_max_val)):
            rules: List[RuleDonePastDueTradesOfLast3Months] = RuleDonePastDueTradesOfLast3Months.objects()
            rdict = {}
            for r in rules:
                rdict.__setitem__(r.score, r.max)
            self.rds.zadd(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, rdict)
        print('caching rules_done_past_due_trades_of_last_3_months are done.')

    def cache_rules_done_past_due_trades_between_last_3_to_12_months(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_min_val, rules_max_val)):
            rules: List[RuleDonePastDueTradesBetweenLast3To12Months] = RuleDonePastDueTradesBetweenLast3To12Months.objects()
            rdict = {}
            for r in rules:
                rdict.__setitem__(r.score, r.max)
            self.rds.zadd(SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rdict)
        print('caching rules_done_past_due_trades_between_last_3_to_12_months are done.')

    def cache_rules_done_timely_trades_of_last_3_months(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, rules_min_val, rules_max_val)):
            rules: List[RuleDoneTimelyTradesOfLast3Months] = RuleDoneTimelyTradesOfLast3Months.objects()
            rdict = {}
            for r in rules:
                rdict.__setitem__(r.score, r.max)
            self.rds.zadd(SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, rdict)
        print('caching rules_timely_due_trades_of_last_3_months are done.')

    def cache_rules_done_timely_trades_between_last_3_to_12_months(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_min_val, rules_max_val)):
            rules: List[RuleDoneTimelyTradesBetweenLast3To12Months] = RuleDoneTimelyTradesBetweenLast3To12Months.objects()
            rdict = {}
            for r in rules:
                rdict.__setitem__(r.score, r.max)
            self.rds.zadd(SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rdict)
        print('caching rules_done_timely_trades_between_last_3_to_12_months are done.')

    def cache_rules_done_trades_average_delay_days(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_TRADES_AVERAGE_DELAY_DAYS)

        if not bool(self.rds.zcount(SET_RULES_DONE_TRADES_AVERAGE_DELAY_DAYS, rules_min_val, rules_max_val)):
            rules: List[RuleDoneTradesAverageDelayDaysRatio] = RuleDoneTradesAverageDelayDaysRatio.objects()
            rdict = {}
            for r in rules:
                rdict.__setitem__(r.score, r.max)
            self.rds.zadd(SET_RULES_DONE_TRADES_AVERAGE_DELAY_DAYS, rdict)
        print('caching rules_done_trades_average_delay_days are done.')

    def cache_rules_done_trades_average_total_amount(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_TRADES_AVERAGE_TOTAL_AMOUNT)

        if not bool(self.rds.zcount(SET_RULES_DONE_TRADES_AVERAGE_TOTAL_AMOUNT, rules_min_val, rules_max_val)):
            rules: List[RuleDoneTradesTotalBalanceRatio] = RuleDoneTradesTotalBalanceRatio.objects()
            rdict = {}
            for r in rules:
                rdict.__setitem__(r.score, r.max)
            self.rds.zadd(SET_RULES_DONE_TRADES_AVERAGE_TOTAL_AMOUNT, rdict)
        print('caching rules_done_trades_average_total_amount are done.')

    # ---------------------------- find methods ----------------------------------- #
    def get_score_of_rules_done_arrear_trades_of_last_3_months(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS, trades_count, rules_max_val)
        return int(scores[0])

    def get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, trades_count, rules_max_val)
        return int(scores[0])

    def get_score_of_rules_done_past_due_trades_of_last_3_months(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, trades_count, rules_max_val)
        return int(scores[0])

    def get_score_of_rules_done_past_due_trades_between_last_3_to_12_months(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, trades_count, rules_max_val)
        return int(scores[0])

    def get_score_of_rules_done_timely_trades_of_last_3_months(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, trades_count, rules_max_val)
        return int(scores[0])

    def get_score_of_rules_done_timely_trades_between_last_3_to_12_months(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, trades_count, rules_max_val)
        return int(scores[0])

    def get_score_of_rules_done_trades_average_delay_days(self, average_delay_days):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_TRADES_AVERAGE_DELAY_DAYS, average_delay_days, rules_max_val)
        return int(scores[0])

    def get_score_of_rules_done_trades_average_total_amount(self, average_total_amount):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_TRADES_AVERAGE_TOTAL_AMOUNT, average_total_amount, rules_max_val)
        return int(scores[0])
