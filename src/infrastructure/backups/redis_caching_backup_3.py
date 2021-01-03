import typing

import redis
from redis import StrictRedis

from data.rule.done.rules_done_arrear_trades_between_last_3_to_12_months import RuleDoneArrearTradesBetweenLast3To12Months
from data.rule.done.rules_done_arrear_trades_of_last_3_months import RuleDoneArrearTradesOfLast3Months
from infrastructure.constants import redis_password, SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_max_val, rules_min_val, \
    SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS

# noinspection DuplicatedCode
recreate_caches = True


def get_redis_connection():
    try:
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password=redis_password, decode_responses=True)
        rds = redis.StrictRedis(connection_pool=pool)
        # print("credit-scoring redis connection is established.")
    except Exception as e:
        print(e)
    return rds


def cache_rules():
    rds = get_redis_connection()
    cache_rules_done_arrear_trades_of_last_3_months(rds)
    cache_rules_done_arrear_trades_between_last_3_to_12_months(rds)


# noinspection DuplicatedCode
def cache_rules_done_arrear_trades_of_last_3_months(rds: [StrictRedis]):
    if recreate_caches:
        rds.delete(SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS)
    if not bool(rds.zcount(SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS, rules_min_val, rules_max_val)):
        rules: typing.List[RuleDoneArrearTradesOfLast3Months] = RuleDoneArrearTradesOfLast3Months.objects()
        rdict = {}
        for r in rules:
            rdict.__setitem__(r.score, r.max)
        rds.zadd(SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS, rdict)
    print('caching rules_done_arrear_trades_of_last_3_months are done.')


# noinspection DuplicatedCode
def cache_rules_done_arrear_trades_between_last_3_to_12_months(rds: [StrictRedis]):
    if recreate_caches:
        rds.delete(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS)

    if not bool(rds.zcount(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_min_val, rules_max_val)):
        rules: typing.List[RuleDoneArrearTradesBetweenLast3To12Months] = RuleDoneArrearTradesBetweenLast3To12Months.objects()
        rdict = {}
        for r in rules:
            rdict.__setitem__(r.score, r.max)
        rds.zadd(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rdict)
    print('caching rules_done_arrear_trades_between_last_3_to_12_months are done.')


# find methods part #
def get_score_of_rules_done_arrear_trades_of_last_3_months(trades_count):
    rds = get_redis_connection()
    scores = rds.zrangebyscore(SET_RULES_DONE_ARREAR_TRADES_OF_LAST_3_MONTHS, trades_count, rules_max_val)
    return int(scores[0])


def get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(trades_count, rds=None):
    if rds is None:
        rds = get_redis_connection()
    scores = rds.zrangebyscore(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, trades_count, rules_max_val)
    return int(scores[0])
