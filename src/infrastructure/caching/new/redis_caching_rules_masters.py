from mongoengine.queryset.visitor import Q
from redis import StrictRedis

from data.rules import Rule
from infrastructure.constants import IDENTITIES, \
    SET_RULES_IDENTITIES_MASTER, SET_RULES_HISTORIES_MASTER, HISTORIES, SET_RULES_VOLUMES_MASTER, VOLUMES, SET_RULES_TIMELINESS_MASTER, TIMELINESS, \
    PERCENT, SCORE


# noinspection DuplicatedCode
class RedisCachingRulesMasters:
    recreate_caches = True
    rds: [StrictRedis] = None

    def __init__(self, rds: StrictRedis) -> None:
        self.rds = rds
        super().__init__()

    def cache_rules(self):
        self.cache_rule_identities_master()
        self.cache_rule_histories_master()
        self.cache_rule_volumes_master()
        self.cache_rule_timeliness_master()

    # ---------------------------- set cache methods ----------------------------------- #
    def cache_rule_identities_master(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_IDENTITIES_MASTER)
        if not bool(self.rds.get(SET_RULES_IDENTITIES_MASTER)):
            rule: Rule = Rule.objects(Q(code=IDENTITIES)).first()
            self.rds.hmset(SET_RULES_IDENTITIES_MASTER, {PERCENT: rule.impact_percent, SCORE: rule.score})
        print('caching set_rules_identities_master are done.')

    def cache_rule_histories_master(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_HISTORIES_MASTER)
        if not bool(self.rds.get(SET_RULES_HISTORIES_MASTER)):
            rule: Rule = Rule.objects(Q(code=HISTORIES)).first()
            self.rds.hmset(SET_RULES_HISTORIES_MASTER, {PERCENT: rule.impact_percent, SCORE: rule.score})
        print('caching set_rules_histories_master are done.')

    def cache_rule_volumes_master(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_VOLUMES_MASTER)
        if not bool(self.rds.get(SET_RULES_VOLUMES_MASTER)):
            rule: Rule = Rule.objects(Q(code=VOLUMES)).first()
            self.rds.hmset(SET_RULES_VOLUMES_MASTER, {PERCENT: rule.impact_percent, SCORE: rule.score})
        print('caching set_rules_volumes_master are done.')

    def cache_rule_timeliness_master(self):
        if self.recreate_caches:
            self.rds.delete(SET_RULES_TIMELINESS_MASTER)
        if not bool(self.rds.get(SET_RULES_TIMELINESS_MASTER)):
            rule: Rule = Rule.objects(Q(code=TIMELINESS)).first()
            self.rds.hmset(SET_RULES_TIMELINESS_MASTER, {PERCENT: rule.impact_percent, SCORE: rule.score})
        print('caching set_rules_timeliness_master are done.')

    # ---------------------------- read cache methods ----------------------------------- #
    def get_impact_percent_of_rule_identities_master(self):
        return self.rds.hget(SET_RULES_IDENTITIES_MASTER, PERCENT)

    def get_score_of_rule_identities_master(self):
        return self.rds.hget(SET_RULES_IDENTITIES_MASTER, SCORE)

    def get_impact_percent_of_rule_histories_master(self):
        return self.rds.hget(SET_RULES_HISTORIES_MASTER, PERCENT)

    def get_score_of_rule_histories_master(self):
        return self.rds.hget(SET_RULES_HISTORIES_MASTER, SCORE)

    def get_impact_percent_of_rule_volumes_master(self):
        return self.rds.hget(SET_RULES_VOLUMES_MASTER, PERCENT)

    def get_score_of_rule_volumes_master(self):
        return self.rds.hget(SET_RULES_VOLUMES_MASTER, SCORE)

    def get_impact_percent_of_rule_timeliness_master(self):
        return self.rds.hget(SET_RULES_TIMELINESS_MASTER, PERCENT)

    def get_score_of_rule_timeliness_master(self):
        return self.rds.hget(SET_RULES_TIMELINESS_MASTER, SCORE)
