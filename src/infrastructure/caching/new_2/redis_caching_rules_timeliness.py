from mongoengine.queryset.visitor import Q
from redis import StrictRedis

# from data.rule.profile.rules_profile_address_verifications import RuleProfileAddressVerification
# from data.rule.profile.rules_profile_membership_days_counts import RuleProfileMembershipDaysCount
# from data.rule.profile.rules_profile_military_service_status import RuleProfileMilitaryServiceStatus
# from data.rule.profile.rules_profile_recommended_to_others_counts import RuleProfileRecommendedToOthersCount
# from data.rule.profile.rules_profile_sim_card_ownerships import RuleProfileSimCardOwnership
# from data.rule.profile.rules_profile_star_counts_avgs import RuleProfileStarCountAvg
from data.rules import Rule
from infrastructure.constants import rules_max_val, rules_min_val, \
    SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, \
    SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, T23_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, \
    T22_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS
from service.util import get_score_from_dict, add_rule_to_dict


# noinspection DuplicatedCode
class RedisCachingRulesHistories:
    recreate_caches = True
    rds: [StrictRedis] = None

    def __init__(self, rds: StrictRedis) -> None:
        self.rds = rds
        super().__init__()

    def cache_rules(self):
        self.cache_rules_timeliness_done_past_due_trades_of_last_3_months_t22()


    # ---------------------------- set cache methods ----------------------------------- #
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

    def cache_rules_history_done_past_due_trades_between_last_3_to_12_months_t23(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS)

        if not bool(self.rds.zcount(SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=T23_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, rdict)
        print('caching rules_history_done_past_due_trades_between_last_3_to_12_months_h7 are done.')


    # ---------------------------- read cache methods ----------------------------------- #
    def get_score_of_rules_done_past_due_trades_of_last_3_months_h6(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_PAST_DUE_TRADES_OF_LAST_3_MONTHS, trades_count, rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_done_past_due_trades_between_last_3_to_12_months_h7(self, trades_count):
        scores = self.rds.zrangebyscore(SET_RULES_DONE_PAST_DUE_TRADES_BETWEEN_LAST_3_TO_12_MONTHS, trades_count, rules_max_val)
        return get_score_from_dict(scores)

