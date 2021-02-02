from mongoengine.queryset.visitor import Q
from redis import StrictRedis

from data.rules import Rule
from infrastructure.constants import rules_max_val, rules_min_val, \
    SET_RULES_PROFILE_MEMBERSHIP_DAYS_COUNTS, \
    H5_RULES_PROFILE_MEMBERSHIP_DAYS_COUNTS, SET_RULES_PROFILE_RECOMMENDED_TO_OTHERS_COUNTS, H8_RULES_PROFILE_RECOMMENDED_TO_OTHERS_COUNTS, \
    SET_RULES_PROFILE_STAR_COUNTS_AVGS, H9_RULES_PROFILE_STAR_COUNTS_AVGS, SET_RULES_UNDONE_UNDUE_TRADES_COUNTS, H10_RULES_UNDONE_UNDUE_TRADES_COUNTS, \
    SET_RULES_LOAN_TOTAL_COUNTS, H11_RULES_LOAN_TOTAL_COUNTS, SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, \
    SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, H6_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, \
    H7_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS
from service.util import get_score_from_dict, add_rule_to_dict


# noinspection DuplicatedCode
class RedisCachingRulesHistories:
    recreate_caches = True
    rds: [StrictRedis] = None

    def __init__(self, rds: StrictRedis) -> None:
        self.rds = rds
        super().__init__()

    def cache_rules(self):
        self.cache_rules_history_membership_days_counts_h5()
        self.cache_rules_history_done_timely_trades_of_last_3_months_h6()
        self.cache_rules_history_done_timely_trades_between_last_3_to_12_months_h7()
        self.cache_rules_history_recommended_to_others_counts_h8()
        self.cache_rules_history_star_counts_avgs_h9()
        self.cache_rules_history_undone_undue_trades_counts_h10()
        self.cache_rules_history_loans_total_counts_h11()

    # ---------------------------- set cache methods ----------------------------------- #
    def cache_rules_history_membership_days_counts_h5(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_PROFILE_MEMBERSHIP_DAYS_COUNTS)
        if not bool(self.rds.zcount(SET_RULES_PROFILE_MEMBERSHIP_DAYS_COUNTS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=H5_RULES_PROFILE_MEMBERSHIP_DAYS_COUNTS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_PROFILE_MEMBERSHIP_DAYS_COUNTS, rdict)
        print('caching rules_history_membership_days_counts_h5 are done.')

    def cache_rules_history_done_timely_trades_of_last_3_months_h6(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=H6_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, rdict)
        print('caching rules_history_done_timely_trades_of_last_3_months_h6 are done.')

    def cache_rules_history_done_timely_trades_between_last_3_to_12_months_h7(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=H7_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rdict)
        print('caching rules_history_done_timely_trades_between_last_3_to_12_months_h7 are done.')

    def cache_rules_history_recommended_to_others_counts_h8(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_PROFILE_RECOMMENDED_TO_OTHERS_COUNTS)
        if not bool(self.rds.zcount(SET_RULES_PROFILE_RECOMMENDED_TO_OTHERS_COUNTS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=H8_RULES_PROFILE_RECOMMENDED_TO_OTHERS_COUNTS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_PROFILE_RECOMMENDED_TO_OTHERS_COUNTS, rdict)
        print('caching rules_history_recommended_to_others_counts_h8 are done.')

    def cache_rules_history_star_counts_avgs_h9(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_PROFILE_STAR_COUNTS_AVGS)
        if not bool(self.rds.zcount(SET_RULES_PROFILE_STAR_COUNTS_AVGS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=H9_RULES_PROFILE_STAR_COUNTS_AVGS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_PROFILE_STAR_COUNTS_AVGS, rdict)
        print('caching rules_history_star_counts_avgs_h9 are done.')

    def cache_rules_history_undone_undue_trades_counts_h10(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_UNDONE_UNDUE_TRADES_COUNTS)
        if not bool(self.rds.zcount(SET_RULES_UNDONE_UNDUE_TRADES_COUNTS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=H10_RULES_UNDONE_UNDUE_TRADES_COUNTS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_UNDONE_UNDUE_TRADES_COUNTS, rdict)
        print('caching rules_history_undone_undue_trades_counts are done.')

    def cache_rules_history_loans_total_counts_h11(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_LOAN_TOTAL_COUNTS)
        if not bool(self.rds.zcount(SET_RULES_LOAN_TOTAL_COUNTS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=H11_RULES_LOAN_TOTAL_COUNTS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_LOAN_TOTAL_COUNTS, rdict)
        print('caching rules_history_loans_total_counts_h11 are done.')

    # ---------------------------- read cache methods ----------------------------------- #
    def get_score_of_rules_history_membership_days_counts_h5(self, membership_days_count):
        scores = self.rds.zrangebyscore(SET_RULES_PROFILE_MEMBERSHIP_DAYS_COUNTS, membership_days_count, rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_history_done_timely_trades_of_last_3_months_h6(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_TIMELY_TRADES_OF_LAST_3_MONTHS, trades_count, rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_history_done_timely_trades_between_last_3_to_12_months_h7(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_TIMELY_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, trades_count, rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_history_recommended_to_others_counts_h8(self, recommended_to_others_count):
        scores = self.rds.zrangebyscore(SET_RULES_PROFILE_RECOMMENDED_TO_OTHERS_COUNTS, recommended_to_others_count, rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_history_star_counts_avgs_h9(self, star_count_avg):
        scores = self.rds.zrangebyscore(SET_RULES_PROFILE_STAR_COUNTS_AVGS, star_count_avg, rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_history_undone_undue_trades_counts_h10(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_UNDONE_UNDUE_TRADES_COUNTS, trades_count, rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_history_loans_total_counts_h11(self, loan_count):
        scores = self.rds.zrangebyscore(SET_RULES_LOAN_TOTAL_COUNTS, loan_count, rules_max_val)
        return get_score_from_dict(scores)
