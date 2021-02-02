import random
import string

from mongoengine.queryset.visitor import Q

from data.rule.rule_model import RuleModel
from data.rules import Rule
from infrastructure.constants import score_deliminator, NORMALIZATION_MAX_SCORE, ONE_HUNDRED


def create_new_rule(rule: Rule, level, parent: str, code: str, title: str, impact_percent: float, score: int = None, min_val: float = None,
                    max_val: float = None):
    rule.level = level
    rule.parent = parent
    rule.code = code
    rule.title = title
    rule.impact_percent = impact_percent
    rule.score = score
    rule.min = min_val
    rule.max = min_val if max_val is None else max_val
    return rule


def create_rule(rule: RuleModel, code: str, min_val, max_val, score: int, impact_percent: float, desc: str):
    rule.code = code
    rule.min = min_val
    rule.max = max_val
    rule.score = score
    rule.desc = desc
    return rule


def create_rule_by_status_code(rule: RuleModel, code: str, status_code: int, score: int, impact_percent: float, desc: str):
    rule.code = code
    rule.status_code = status_code
    rule.score = score
    rule.desc = desc
    return rule


def get_score_from_dict(scores: {}):
    return int(scores[0].split(score_deliminator)[0])


def get_max_score_from_dict(scores: {}):
    return int(scores[len(scores)-1].split(score_deliminator)[0])


def get_score_code_from_dict(scores: {}):
    return scores[0].split(score_deliminator)[1]


def add_rule_to_dict(rdict: {}, r: Rule):
    rdict.__setitem__((str(r.score) + score_deliminator + r.code), r.max)
    return rdict


def calculate_normalized_score(parent_code: str, score: int):
    rules: [Rule] = Rule.objects(Q(parent=parent_code, score=score))
    # print(rules[0].impact_percent)
    percent = rules[0].impact_percent
    # normalized_score = round(percent * NORMALIZATION_MAX_SCORE / ONE_HUNDRED)
    normalized_score = (percent * NORMALIZATION_MAX_SCORE / ONE_HUNDRED)
    if score < 0:
        normalized_score = (normalized_score * -1)
    print('\nnormalized_score= {} , percent= {}'.format(normalized_score, percent))
    return normalized_score


def add_rule_model_to_dict(rdict: {}, r: RuleModel):
    rdict.__setitem__((str(r.score) + score_deliminator + r.code), r.max)
    return rdict


def add_rule_model_to_dict_by_rds_score(rdict: {}, r: RuleModel, rds_score: int):
    rdict.__setitem__((str(r.score) + score_deliminator + r.code), rds_score)
    return rdict


def add_item_to_dict(rdict: {}, key, value):
    rdict.__setitem__(key, value)
    return rdict


def filter_dict(dic: dict, filtered_item) -> dict:
    nd = {}
    for key, value in dic.items():
        if key != filtered_item:
            nd[key] = value
    return nd


def filter_dict_by_id(dic) -> dict:
    return filter_dict(dic, "_id")


# Random Generator Functions #
# generate random lowercase str by fix length
def get_random_lowercase_str(str_len):
    letters = string.ascii_lowercase
    # print(''.join(random.choice(letters) for i in range(10)))
    rand_str = random_choice(letters, str_len)
    return rand_str


# generate random uppercase str by fix length
def get_random_uppercase_str(str_len):
    letters = string.ascii_uppercase
    rand_str = random_choice(letters, str_len)
    return rand_str


# generate random letters str by fix length
def get_random_letters_str(str_len):
    letters = string.ascii_letters
    rand_str = random_choice(letters, str_len)
    return rand_str


# generate random digits str by fix length
def get_random_digits_str(str_len):
    letters = string.digits
    rand_digits = random_choice(letters, str_len)
    return rand_digits


# generate random punctuation str by fix length
def get_random_punctuation_str(str_len):
    letters = string.punctuation
    rand_str = random_choice(letters, str_len)
    return rand_str


def random_choice(letters, str_len):
    return ''.join(random.choice(letters) for i in range(str_len))
