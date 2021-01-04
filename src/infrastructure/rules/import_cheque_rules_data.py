from data.rule.cheque.rules_unfixed_returned_cheques_count_between_last_3_to_12_months import RuleUnfixedReturnedChequesCountBetweenLast3To12Months
from data.rule.cheque.rules_unfixed_returned_cheques_count_of_last_3_months import RuleUnfixedReturnedChequesCountOfLast3Months
from data.rule.cheque.rules_unfixed_returned_cheques_count_of_last_5_years import RuleUnfixedReturnedChequesCountOfLast5Years
from data.rule.cheque.rules_unfixed_returned_cheques_count_of_more_12_months import RuleUnfixedReturnedChequesCountOfMore12Months
from data.rule.cheque.rules_unfixed_returned_cheques_total_balance_ratio import RuleUnfixedReturnedChequesTotalBalanceRatios
from service.util import creat_rule
from src import program


def import_rules_unfixed_returned_cheques_total_balance_ratio():
    # DCAmountRatio = 0	20	V1701P20	کاربر چک برگشتی رفع سو اثر نشده ندارد
    rule = RuleUnfixedReturnedChequesTotalBalanceRatios()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'V1701P20', 0, 0, 20, 'کاربر چک برگشتی رفع سو اثر نشده ندارد'))

    # 0.001 <= DCAmountRatio ≤ 0.5	00	V1702P0	نسبت بین 0.001 و 0.5 می‌باشد
    rule = RuleUnfixedReturnedChequesTotalBalanceRatios()
    rule.save(creat_rule(rule, 'V1702P0', 0.001, 0.5, 0, 'نسبت بین 0.001 و 0.5 می‌باشد'))

    # 0.501 <= DCAmountRatio ≤ 1	-10	V1703N10	نسبت بین 0.501 و 1 می‌باشد
    rule = RuleUnfixedReturnedChequesTotalBalanceRatios()
    rule.save(creat_rule(rule, 'V1703N10', 0.501, 1, -10, 'نسبت بین 0.501 و 1 می‌باشد'))

    # 1.001 <= DCAmountRatio ≤ 1.5	-20	V1704N20	نسبت بین 1.001 و 1.5 می‌باشد
    rule = RuleUnfixedReturnedChequesTotalBalanceRatios()
    rule.save(creat_rule(rule, 'V1704N20', 1.001, 1.5, -20, 'نسبت بین 1.001 و 1.5 می‌باشد'))

    # 1.501 <= DCAmountRatio ≤ 2	-30	V1705N30	نسبت بین 1.501 و 2 می‌باشد
    rule = RuleUnfixedReturnedChequesTotalBalanceRatios()
    rule.save(creat_rule(rule, 'V1705N30', 1.501, 2, -30, 'نسبت بین 1.501 و 2 می‌باشد'))

    # DCAmountRatio >= 2.001	-40	V1706N40	نسبت بیش از 2 می‌باشد
    rule = RuleUnfixedReturnedChequesTotalBalanceRatios()
    rule.save(creat_rule(rule, 'V1706N40', 2.001, 999, -40, 'نسبت بیش از 2 می‌باشد'))


def import_rules_unfixed_returned_cheques_count_of_last_3_months():
    # DishonouredChequesL3M = 0	20	T2901P20	کاربر چک برگشتی ندارد
    rule = RuleUnfixedReturnedChequesCountOfLast3Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T2901P20', 0, 0, 20, 'کاربر چک برگشتی ندارد'))

    # DishonouredChequesL3M = 1	-10	T2902N10	کاربر ۱ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfLast3Months()
    rule.save(creat_rule(rule, 'T2902N10', 1, 1, -10, 'کاربر ۱ چک برگشتی دارد'))

    # DishonouredChequesL3M = 2	-20	T2903N20	کاربر ۲ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfLast3Months()
    rule.save(creat_rule(rule, 'T2903N20', 2, 2, -20, 'کاربر 2 چک برگشتی دارد'))

    # DishonouredChequesL3M = 3	-30	T2904N30	کاربر ۳ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfLast3Months()
    rule.save(creat_rule(rule, 'T2904N30', 3, 3, -30, 'کاربر 3 چک برگشتی دارد'))

    # DishonouredChequesL3M > 3	-40	T2905N40	کاربر بیش از ۳ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfLast3Months()
    rule.save(creat_rule(rule, 'T2905N40', 4, 999, -40, 'کاربر بیش از ۳ چک برگشتی دارد'))


def import_rules_unfixed_returned_cheques_count_between_last_3_to_12_months():
    # DishonouredChequesL3-12M = 0	20	T3001P20	کاربر چک برگشتی ندارد
    rule = RuleUnfixedReturnedChequesCountBetweenLast3To12Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T3001P20', 0, 0, 20, 'کاربر چک برگشتی ندارد'))

    # DishonouredChequesL3-12M = 1	-10	T3002N30	کاربر ۱ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T3002N30', 1, 1, -30, 'کاربر ۱ چک برگشتی دارد'))

    # DishonouredChequesL3-12M = 2	-20	T3003N40	کاربر ۲ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T3003N40', 2, 2, -40, 'کاربر 2 چک برگشتی دارد'))

    # DishonouredChequesL3-12M = 3	-30	T3004N50	کاربر ۳ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T3004N50', 3, 3, -50, 'کاربر 3 چک برگشتی دارد'))

    # DishonouredChequesL3-12M > 3	-40	T3005N60	کاربر بیش از ۳ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T3005N60', 4, 999, -60, 'کاربر بیش از ۳ چک برگشتی دارد'))


def import_rules_unfixed_returned_cheques_count_of_more_12_months():
    # DishonouredChequesA12M = 0	20	T3101P20	کاربر چک برگشتی ندارد
    rule = RuleUnfixedReturnedChequesCountOfMore12Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T3101P20', 0, 0, 20, 'کاربر چک برگشتی ندارد'))

    # DishonouredChequesA12M = 1	-40	T3102N40	کاربر ۱ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfMore12Months()
    rule.save(creat_rule(rule, 'T3102N40', 1, 1, -40, 'کاربر ۱ چک برگشتی دارد'))

    # DishonouredChequesA12M = 2	-50	T3103N50	کاربر ۲ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfMore12Months()
    rule.save(creat_rule(rule, 'T3103N50', 2, 2, -50, 'کاربر ۲ چک برگشتی دارد'))

    # DishonouredChequesA12M = 3	-60	T3104N60	کاربر ۳ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfMore12Months()
    rule.save(creat_rule(rule, 'T3104N60', 3, 3, -60, 'کاربر ۳ چک برگشتی دارد'))

    # DishonouredChequesA12M >= 4	-70	T3105N70	کاربر بیش از ۳ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfMore12Months()
    rule.save(creat_rule(rule, 'T3105N70', 4, 999, -70, 'کاربر بیش از ۳ چک برگشتی دارد'))


def import_rules_unfixed_returned_cheques_count_of_last_5_years():
    # DishonouredChequesA12M = 0	20	T3101P20	کاربر چک برگشتی ندارد
    rule = RuleUnfixedReturnedChequesCountOfLast5Years()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T3101P20', 0, 0, 20, 'کاربر چک برگشتی ندارد'))

    # DishonouredChequesA12M = 1	-40	T3102N40	کاربر ۱ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfLast5Years()
    rule.save(creat_rule(rule, 'T3102N40', 1, 1, -40, 'کاربر ۱ چک برگشتی دارد'))

    # DishonouredChequesA12M = 2	-50	T3103N50	کاربر ۲ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfLast5Years()
    rule.save(creat_rule(rule, 'T3103N50', 2, 2, -50, 'کاربر ۲ چک برگشتی دارد'))

    # DishonouredChequesA12M = 3	-60	T3104N60	کاربر ۳ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfLast5Years()
    rule.save(creat_rule(rule, 'T3104N60', 3, 3, -60, 'کاربر ۳ چک برگشتی دارد'))

    # DishonouredChequesA12M >= 4	-70	T3105N70	کاربر بیش از ۳ چک برگشتی دارد
    rule = RuleUnfixedReturnedChequesCountOfLast5Years()
    rule.save(creat_rule(rule, 'T3105N70', 4, 999, -70, 'کاربر بیش از ۳ چک برگشتی دارد'))


if __name__ == '__main__':
    program.launch_app()
    import_rules_unfixed_returned_cheques_count_between_last_3_to_12_months()
    import_rules_unfixed_returned_cheques_count_of_last_3_months()
    import_rules_unfixed_returned_cheques_count_of_last_5_years()
    import_rules_unfixed_returned_cheques_count_of_more_12_months()
    import_rules_unfixed_returned_cheques_total_balance_ratio()
