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
    SET_RULES_PROFILE_HAS_KYCS, SET_RULES_PROFILE_ADDRESS_VERIFICATIONS, SET_RULES_PROFILE_MILITARY_SERVICE_STATUS, \
    SET_RULES_PROFILE_SIM_CARD_OWNERSHIPS, \
    I1_RULES_PROFILE_HAS_KYCS, I4_RULES_PROFILE_ADDRESS_VERIFICATIONS, I2_RULES_PROFILE_MILITARY_SERVICE_STATUS, \
    I3_RULES_PROFILE_SIM_CARD_OWNERSHIPS
from infrastructure.scoring_enums import ProfileMilitaryServiceStatusEnum
from service.util import get_score_from_dict, add_rule_to_dict


# noinspection DuplicatedCode
class RedisCachingRulesIdentities:
    recreate_caches = True
    rds: [StrictRedis] = None

    def __init__(self, rds: StrictRedis) -> None:
        self.rds = rds
        super().__init__()

    def cache_rules(self):
        self.cache_rules_identity_has_kycs_i1()
        self.cache_rules_profile_military_service_status_i2()
        self.cache_rules_profile_sim_card_ownerships_i3()
        self.cache_rules_identity_address_verifications_i4()

    # ---------------------------- set cache methods ----------------------------------- #
    def cache_rules_identity_has_kycs_i1(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_PROFILE_HAS_KYCS)
        if not bool(self.rds.zcount(SET_RULES_PROFILE_HAS_KYCS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=I1_RULES_PROFILE_HAS_KYCS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_PROFILE_HAS_KYCS, rdict)
            print('caching rules_profile_has_kycs_i1 are done.')

    def cache_rules_profile_military_service_status_i2(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_PROFILE_MILITARY_SERVICE_STATUS)
        if not bool(self.rds.zcount(SET_RULES_PROFILE_MILITARY_SERVICE_STATUS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=I2_RULES_PROFILE_MILITARY_SERVICE_STATUS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_PROFILE_MILITARY_SERVICE_STATUS, rdict)
        print('caching rules_profile_military_service_status are done.')

    def cache_rules_profile_sim_card_ownerships_i3(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_PROFILE_SIM_CARD_OWNERSHIPS)
        if not bool(self.rds.zcount(SET_RULES_PROFILE_SIM_CARD_OWNERSHIPS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=I3_RULES_PROFILE_SIM_CARD_OWNERSHIPS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_PROFILE_SIM_CARD_OWNERSHIPS, rdict)
        print('caching rules_profile_sim_card_ownerships are done.')

    def cache_rules_identity_address_verifications_i4(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_PROFILE_ADDRESS_VERIFICATIONS)
        if not bool(self.rds.zcount(SET_RULES_PROFILE_ADDRESS_VERIFICATIONS, rules_min_val, rules_max_val)):
            rules: [Rule] = Rule.objects(Q(parent=I4_RULES_PROFILE_ADDRESS_VERIFICATIONS))
            rdict = {}
            for r in rules:
                add_rule_to_dict(rdict, r)
            self.rds.zadd(SET_RULES_PROFILE_ADDRESS_VERIFICATIONS, rdict)
        print('caching rules_profile_address_verifications are done.')

    # ---------------------------- read cache methods ----------------------------------- #
    def get_score_of_rules_identity_has_kycs_i1(self, has_kyc):
        scores = self.rds.zrangebyscore(SET_RULES_PROFILE_HAS_KYCS, int(has_kyc), rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_identity_military_service_status_i2(self, military_service_status: ProfileMilitaryServiceStatusEnum):
        scores = self.rds.zrangebyscore(SET_RULES_PROFILE_MILITARY_SERVICE_STATUS, military_service_status.value, rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_identity_sim_card_ownerships_i3(self, sim_card_ownership):
        scores = self.rds.zrangebyscore(SET_RULES_PROFILE_SIM_CARD_OWNERSHIPS, int(sim_card_ownership), rules_max_val)
        return get_score_from_dict(scores)

    def get_score_of_rules_identity_address_verifications_i4(self, address_verification):
        scores = self.rds.zrangebyscore(SET_RULES_PROFILE_ADDRESS_VERIFICATIONS, int(address_verification), rules_max_val)
        return get_score_from_dict(scores)
