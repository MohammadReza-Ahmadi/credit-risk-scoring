# from typing import List
#
# import redis
# from redis import StrictRedis
#
# from data.rule.done.rules_done_arrear_trades_between_last_3_to_12_months import \
#     RuleDoneArrearTradesBetweenLast3To12Months
# from infrastructure.constants import SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS
#
# redis_host = "localhost"
# redis_port = 6379
# redis_password = ""
# rules_min_val = 0
# rules_max_val = 999
# recreate_caches = False
#
#
# def get_redis_connection():
#     try:
#         pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password=redis_password, decode_responses=True)
#         r = redis.StrictRedis(connection_pool=pool)
#         print("credit-scoring redis connection is established.")
#     except Exception as e:
#         print(e)
#     return r
#
#
# def cache_rules():
#     rds = get_redis_connection()
#     cache_rules_done_arrear_trades_between_last_3_to_12_months(rds)
#     return rds
#
#
# def cache_rules_done_arrear_trades_between_last_3_to_12_months(rds: StrictRedis):
#     if recreate_caches:
#         rds.delete(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS)
#
#     if not bool(rds.zcount(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_min_val, rules_max_val)):
#         rules: List[RuleDoneArrearTradesBetweenLast3To12Months] = RuleDoneArrearTradesBetweenLast3To12Months.objects()
#         rdict = {}
#         for r in rules:
#             rdict.__setitem__(r.score, r.max)
#         rds.zadd(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rdict)
#     print('caching rules_done_arrear_trades_between_last_3_to_12_months are done.')
#
#
# def get_score_of_rules_done_arrear_trades_between_last_3_to_12_months(rds: StrictRedis, trades_count):
#     scores = rds.zrangebyscore(SET_RULES_DONE_ARREAR_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, trades_count, rules_max_val)
#     return int(scores[0])
#
#
# if __name__ == '__main__':
#     cache_rules()
