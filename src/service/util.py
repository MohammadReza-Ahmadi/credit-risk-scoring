import random
import string


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
