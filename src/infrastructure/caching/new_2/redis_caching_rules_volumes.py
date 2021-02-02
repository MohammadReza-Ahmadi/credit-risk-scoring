from mongoengine.queryset.visitor import Q
from redis import StrictRedis

from data.rules import Rule
from infrastructure.constants import rules_max_val, rules_min_val, \
    SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, \
    T22_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, SET_RULES_DONE_TRADES_AVERAGE_TOTAL_BALANCE_RATIOS, \
    V12_RULES_DONE_TRADES_AVERAGE_TOTAL_BALANCE_RATIOS
from service.util import get_score_from_dict, add_rule_to_dict


# noinspection DuplicatedCode
class RedisCachingRulesVolumes:
    recreate_caches = True
    rds: [StrictRedis] = None

    def __init__(self, rds: StrictRedis) -> None:
        self.rds = rds
        super().__init__()

    def cache_rules(self):
        self.cache_rules_timeliness_done_past_due_trades_of_last_3_months_t22()

    # ---------------------------- set cache methods ----------------------------------- #
    def cache_rules_done_trades_average_total_balance_ratios_v12(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_TRADES_AVERAGE_TOTAL_BALANCE_RATIOS)

        if not bool(self.rds.zcount(SET_RULES_DONE_TRADES_AVERAGE_TOTAL_BALANCE_RATIOS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=V12_RULES_DONE_TRADES_AVERAGE_TOTAL_BALANCE_RATIOS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_DONE_TRADES_AVERAGE_TOTAL_BALANCE_RATIOS, rdict)
        print('caching rules_done_trades_average_total_amount_v12 are done.')

    def cache_rules_timeliness_done_past_due_trades_of_last_3_months_t22(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=T22_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, rdict)
        print('caching rules_history_done_past_due_trades_of_last_3_months_h6 are done.')

    # ---------------------------- read cache methods ----------------------------------- #
    def get_score_of_rules_done_past_due_trades_of_last_3_months_h6(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, trades_count, rules_max_val)
        return get_score_from_dict(scores)
