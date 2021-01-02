from src import program
from src.data.rule.done.rules_done_arrear_trades_between_last_3_to_12_months import \
    RuleDoneArrearTradesBetweenLast3To12Months
from src.data.rule.done.rules_done_arrear_trades_of_last_3_months import RuleDoneArrearTradesOfLast3Months
from src.data.rule.done.rules_done_trades_average_delay_days import RuleDoneTradesAverageDelayDays
from src.data.rule.done.rules_done_past_due_trades_between_last_3_to_12_months import \
    RuleDonePastDueTradesBetweenLast3To12Months
from src.data.rule.done.rules_done_past_due_trades_of_last_3_months import RuleDonePastDueTradesOfLast3Months
from src.data.rule.done.rules_done_timely_trades_of_last_3_months import RuleDoneTimelyTradesBetweenLast3To12Months
from src.data.rule.done.rules_done_trades_average_total_amount import RuleDoneTradesAverageTotalAmount
from src.data.rule.rule_model import RuleModel


def import_rules_done_arrear_trades_between_last_3_to_12_months():
    # 0 <= A30DayDelay3-12M <= 0  20	T2501P20	کاربر در یکسال گذشته هیچ تعامل معوقی نداشته است
    rule = RuleDoneArrearTradesBetweenLast3To12Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T2501P20', 0, 0, 20, 'کاربر در یکسال گذشته هیچ تعامل معوقی نداشته است'))

    # 1 <= A30DayDelay3-12M <= 1  05	T2502P5 	کاربر در یکسال گذشته 1 تعامل معوق داشته است
    rule = RuleDoneArrearTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T2502P5', 1, 1, 5, 'کاربر در یکسال گذشته 1 تعامل معوق داشته است'))

    # 2 <= A30DayDelay3-12M ≤ 3	 -05	T2503N5 	کاربر در یکسال گذشته بین 2 تا 3 تعامل معوق داشته است
    rule = RuleDoneArrearTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T2503N5', 2, 3, -5, 'کاربر در یکسال گذشته بین 2 تا 3 تعامل معوق داشته است'))

    # 4 <= A30DayDelay3-12M ≤ 6	 -10	T2504N10	کاربر در یکسال گذشته بین 4 تا 6 تعامل معوق داشته است
    rule = RuleDoneArrearTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T2504N10', 4, 6, -10, 'کاربر در یکسال گذشته بین 4 تا 6 تعامل معوق داشته است'))

    # 7 <= A30DayDelay3-12M ≤ 10 -20	T2505N20	کاربر در یکسال گذشته بین 7 تا 10 تعامل معوق داشته است
    rule = RuleDoneArrearTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T2505N20', 7, 10, -20, 'کاربر در یکسال گذشته بین 7 تا 10 تعامل معوق داشته است'))

    # 11 <= A30DayDelay3-12M <= 999	-30	T2506N30	کاربر در یکسال گذشته بیش از 10 تعامل معوق داشته است
    rule = RuleDoneArrearTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T2506N30', 11, 999, -30, 'کاربر در یکسال گذشته 10 تعامل معوق داشته است'))


def import_rules_done_arrear_trades_of_last_3_months():
    # A30DayDelayLast3M = 0	20	T2401P20	کاربر در سه ماه گذشته هیچ تعامل معوقی نداشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T2401P20', 0, 0, 20, 'کاربر در سه ماه گذشته هیچ تعامل معوقی نداشته است'))

    # A30DayDelayLast3M = 1	00	T2402P0	کاربر در سه ماه گذشته 1 تعامل معوق داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(creat_rule(rule, 'T2402P0', 1, 1, 0, 'کاربر در سه ماه گذشته 1 تعامل معوق داشته است'))

    # 2 <= A30DayDelayLast3M ≤ 3	-10	T2403N10	کاربر در سه ماه گذشته بین 2 تا 3 تعامل معوق داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(creat_rule(rule, 'T2403N10', 2, 3, -10, 'کاربر در سه ماه گذشته بین 2 تا 3 تعامل معوق داشته است'))

    # 4 <= A30DayDelayLast3M ≤ 6	-20	T2404N20	کاربر در سه ماه گذشته بین 4 تا 6 تعامل معوق داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(creat_rule(rule, 'T2404N20', 4, 6, -20, 'کاربر در سه ماه گذشته بین 4 تا 6 تعامل معوق داشته است'))

    # 7 <= A30DayDelayLast3M ≤ 10	-30	T2405N30	کاربر در سه ماه گذشته بین 7 تا 10 تعامل معوق داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(creat_rule(rule, 'T2405N30', 7, 10, -30, 'کاربر در سه ماه گذشته بین 7 تا 10 تعامل معوق داشته است'))

    # 11 <= A30DayDelayLast3M <= 999 -40 T2406N40	کاربر در سه ماه گذشته بیش از 10 تعامل معوق داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(creat_rule(rule, 'T2406N40', 11, 999, -40, 'کاربر در سه ماه گذشته بیش از 10 تعامل معوق داشته است'))


def import_rules_done_past_due_trades_between_last_3_to_12_months():
    # B30DayDelayLast3-12M = 0	20	T2301P20	کاربر در یکسال گذشته هیچ تعامل سررسید گذشته‌ای نداشته است
    rule = RuleDonePastDueTradesBetweenLast3To12Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T2301P20', 0, 0, 20, 'کاربر در یکسال گذشته هیچ تعامل سررسید گذشته‌ای نداشته است'))

    # B30DayDelayLast3-12M = 1	15	T2302P15	کاربر در یکسال گذشته 1 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T2302P15', 1, 1, 15, 'کاربر در یکسال گذشته 1 تعامل سررسید گذشته‌ داشته است'))

    # 2 <= B30DayDelayLast3-12M ≤ 3	05	T2303P5	کاربر در یکسال گذشته بین 2 تا 3 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T2303P5', 2, 3, 5, 'کاربر در یکسال گذشته بین 2 تا 3 تعامل سررسید گذشته‌ داشته است'))

    # 4 <= B30DayDelayLast3-12M ≤ 6	-10	T2304N10	کاربر در یکسال گذشته بین 4 تا 6 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'T2304N10', 4, 6, -10, 'کاربر در یکسال گذشته بین 4 تا 6 تعامل سررسید گذشته‌ داشته است'))

    # 7 <= B30DayDelayLast3-12M ≤ 10	-15	T2305N15	کاربر در یکسال گذشته بین 7 تا 10 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesBetweenLast3To12Months()
    rule.save(
        creat_rule(rule, 'T2305N15', 7, 10, -15, 'کاربر در یکسال گذشته بین 7 تا 10 تعامل سررسید گذشته‌ داشته است'))

    # B30DayDelayLast3-12M >= 11	-20	T2306N20	کاربر در یکسال گذشته بیش از 10 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesBetweenLast3To12Months()
    rule.save(
        creat_rule(rule, 'T2306N20', 11, 999, -20, 'کاربر در یکسال گذشته بیش از 10 تعامل سررسید گذشته‌ داشته است'))


def import_rules_done_past_due_trades_of_last_3_months():
    # B30DayDelayLast3M = 0	20	T2201P20	کاربر در سه ماه گذشته هیچ تعامل سررسید گذشته‌ای نداشته است
    rule = RuleDonePastDueTradesOfLast3Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T2201P20', 0, 0, 20, 'کاربر در سه ماه گذشته هیچ تعامل سررسید گذشته‌ای نداشته است'))

    # B30DayDelayLast3M = 1	10	T2202P10	کاربر در سه ماه گذشته 1 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesOfLast3Months()
    rule.save(creat_rule(rule, 'T2202P10', 1, 1, 10, 'کاربر در سه ماه گذشته 1 تعامل سررسید گذشته‌ داشته است'))

    # 2 < B30DayDelayLast3M ≤ 3	00	T2203P0	کاربر در سه ماه گذشته بین 2 تا 3 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesOfLast3Months()
    rule.save(creat_rule(rule, 'T2203P0', 2, 3, 0, 'کاربر در سه ماه گذشته بین 2 تا 3 تعامل سررسید گذشته‌ داشته است'))

    # 4 <= B30DayDelayLast3M ≤ 6	-10	T2204N10	کاربر در سه ماه گذشته بین 4 تا 6 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesOfLast3Months()
    rule.save(creat_rule(rule, 'T2204N10', 4, 6, -10, 'کاربر در سه ماه گذشته بین 4 تا 6 تعامل سررسید گذشته‌ داشته است'))

    # 7 <= B30DayDelayLast3M ≤ 10	-20	T2205N20	کاربر در سه ماه گذشته بین 7 تا 10 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesOfLast3Months()
    rule.save(
        creat_rule(rule, 'T2205N20', 7, 10, -20, 'کاربر در سه ماه گذشته بین 7 تا 10 تعامل سررسید گذشته‌ داشته است'))

    # B30DayDelayLast3M >= 11	-30	T2206N30	کاربر در سه ماه گذشته بیش از 10 تعامل سررسید گذشته‌ داشته است
    rule = RuleDonePastDueTradesOfLast3Months()
    rule.save(
        creat_rule(rule, 'T2206N30', 11, 999, -30, 'کاربر در سه ماه گذشته بیش از 10 تعامل سررسید گذشته‌ داشته است'))


def import_rules_done_timely_trades_between_last_3_to_12_months():
    # Last1YSD = 0	00	H0701P0	کاربر در یکسال گذشته هیچ تعامل موفقی با سایر کاربران نداشته است
    rule = RuleDoneTimelyTradesBetweenLast3To12Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'H0701P0', 0, 0, 0, 'کاربر در یکسال گذشته هیچ تعامل موفقی با سایر کاربران نداشته است'))

    # Last1YSD = 1	05	H0702P05	کاربر در یکسال گذشته 1 تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneTimelyTradesBetweenLast3To12Months()
    rule.save(creat_rule(rule, 'H0702P05', 1, 1, 5, 'کاربر در یکسال گذشته 1 تعامل موفق با سایر کاربران داشته است'))

    # 2 <= Last1YSD ≤ 3	10	H0703P10	کاربر در یکسال گذشته بین 2 تا 3 تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneTimelyTradesBetweenLast3To12Months()
    rule.save(
        creat_rule(rule, 'H0703P10', 2, 3, 10, 'کاربر در یکسال گذشته بین 2 تا 3 تعامل موفق با سایر کاربران داشته است'))

    # 4 <= Last1YSD ≤ 6	20	H0704P20	کاربر در یکسال گذشته بین 4 تا 6 تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneTimelyTradesBetweenLast3To12Months()
    rule.save(
        creat_rule(rule, 'H0704P20', 4, 6, 20, 'کاربر در یکسال گذشته بین 4 تا 6 تعامل موفق با سایر کاربران داشته است'))

    # 7 <= Last1YSD ≤ 10	30	H0705P30	کاربر در یکسال گذشته بین 7 تا 10 تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneTimelyTradesBetweenLast3To12Months()
    rule.save(
        creat_rule(rule, 'H0705P30', 7, 10, 30,
                   'کاربر در یکسال گذشته بین 7 تا 10 تعامل موفق با سایر کاربران داشته است'))

    # Last1YSD >= 11	40	H0706P40	کاربر در یکسال گذشته بیش از 10 تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneTimelyTradesBetweenLast3To12Months()
    rule.save(
        creat_rule(rule, 'H0706P40', 11, 999, 40,
                   'کاربر در یکسال گذشته بیش از 10 تعامل موفق با سایر کاربران داشته است'))


def import_rules_done_timely_trades_of_last_3_months():
    # Last3MSD = 0	00	H0601P0	کاربر در سه ماه گذشته هیچ تعامل موفقی با سایر کاربران نداشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'H0601P0', 0, 0, 0, 'کاربر در سه ماه گذشته هیچ تعامل موفقی با سایر کاربران نداشته است'))

    # Last3MSD = 1	10	H0602P10	کاربر در سه ماه گذشته 1 تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(creat_rule(rule, 'H0602P10', 1, 1, 10, 'کاربر در سه ماه گذشته 1 تعامل موفق با سایر کاربران داشته است'))

    # Last3MSD = 2	20	H0603P20	کاربر در سه ماه گذشته ۲ تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(creat_rule(rule, 'H0603P20', 2, 2, 20, 'کاربر در سه ماه گذشته ۲ تعامل موفق با سایر کاربران داشته است'))

    # Last3MSD = 3	30	H0604P30	کاربر در سه ماه گذشته 3 تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(creat_rule(rule, 'H0604P30', 3, 3, 30, 'کاربر در سه ماه گذشته 3 تعامل موفق با سایر کاربران داشته است'))

    # Last3MSD ≥ 4	40	H0605P40	کاربر در سه ماه گذشته بیش از 3 تعامل موفق با سایر کاربران داشته است
    rule = RuleDoneArrearTradesOfLast3Months()
    rule.save(
        creat_rule(rule, 'H0605P40', 4, 999, 40, 'کاربر در سه ماه گذشته بیش از 3 تعامل موفق با سایر کاربران داشته است'))


def import_rules_done_trades_total_amount():
    # SDealAmountRatio = 0	00	V1201P0	کاربر تعاملی نداشته است
    rule = RuleDoneTradesAverageTotalAmount()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'V1201P0', 0, 0, 0, 'کاربر تعاملی نداشته است'))

    # 0.001 <= SDealAmountRatio ≤ 0.5	10	V1202P10	نسبت بین 0.001 و 0.5 می‌باشد
    rule = RuleDoneTradesAverageTotalAmount()
    rule.save(creat_rule(rule, 'V1202P10', 0.001, 0.5, 10, 'نسبت بین 0.001 و 0.5 می‌باشد'))

    # 0.501 <= SDealAmountRatio ≤ 1	20	V1203P20	نسبت بین 0.501 و 1 می‌باشد
    rule = RuleDoneTradesAverageTotalAmount()
    rule.save(creat_rule(rule, 'V1203P20', 0.501, 1, 20, 'نسبت بین 0.501 و 1 می‌باشد'))

    # 1.001 <= SDealAmountRatio ≤ 1.5	30	V1204P30	نسبت بین 1.001 و 1.5 می‌باشد
    rule = RuleDoneTradesAverageTotalAmount()
    rule.save(creat_rule(rule, 'V1204P30', 1.001, 1.5, 30, 'نسبت بین 1.001 و 1.5 می‌باشد'))

    # 1.501 <= SDealAmountRatio ≤ 2	40	V1205P40	نسبت بین 1.501 و 2 می‌باشد
    rule = RuleDoneTradesAverageTotalAmount()
    rule.save(creat_rule(rule, 'V1205P40', 1.501, 2, 40, 'نسبت بین 1.501 و 2 می‌باشد'))

    # SDealAmountRatio >= 2.001	50	V1206P50	نسبت بیش از 2 می‌باشد
    rule = RuleDoneTradesAverageTotalAmount()
    rule.save(creat_rule(rule, 'V1206P50', 2.001, 999, 50, 'نسبت بیش از 2 می‌باشد'))


def import_rules_done_trades_average_delay_days():
    # AverageDelayRatio = 0	20	T2801P20	کاربر در انجام تعاملات تاخیر نداشته است
    rule = RuleDoneTradesAverageDelayDays()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T2801P20', 0, 0, 20, 'کاربر در انجام تعاملات تاخیر نداشته است'))

    # 0.001 <= AverageDelayRatio ≤ 0.5	10	T2802P10	نسبت بین 0.001 و 0.5 می‌باشد
    rule = RuleDoneTradesAverageDelayDays()
    rule.save(creat_rule(rule, 'T2802P10', 0.001, 0.5, 10, 'نسبت بین 0.001 و 0.5 می‌باشد'))

    # 0.501 <= AverageDelayRatio ≤ 1	00	T2803P0	نسبت بین 0.501 و 1 می‌باشد
    rule = RuleDoneTradesAverageDelayDays()
    rule.save(creat_rule(rule, 'T2803P0', 0.501, 1.0, 0, 'نسبت بین 0.501 و 1 می‌باشد'))

    # 1.001 <= AverageDelayRatio ≤ 1.5	-10	T2804N10	نسبت بین 1.001 و 1.5 می‌باشد
    rule = RuleDoneTradesAverageDelayDays()
    rule.save(creat_rule(rule, 'T2804N10', 1.001, 1.5, -10, 'نسبت بین 1.001 و 1.5 می‌باشد'))

    # 1.501 <= AverageDelayRatio ≤ 2	-20	T2805N20	نسبت بین 1.501 و 2 می‌باشد
    rule = RuleDoneTradesAverageDelayDays()
    rule.save(creat_rule(rule, 'T2805N20', 1.501, 2, -20, 'نسبت بین 1.501 و 2 می‌باشد'))

    # AverageDelayRatio >= 2.001	-30	T2806N30	نسبت بیش از 2 می‌باشد
    rule = RuleDoneTradesAverageDelayDays()
    rule.save(creat_rule(rule, 'T2806N30', 2.001, 999, 0, 'نسبت بیش از 2 می‌باشد'))


def creat_rule(rule: RuleModel, code: str, min_val, max_val, score: int, desc: str):
    rule.code = code
    rule.min = min_val
    rule.max = max_val
    rule.score = score
    rule.desc = desc
    return rule


if __name__ == '__main__':
    program.launch_app()
    import_rules_done_arrear_trades_between_last_3_to_12_months()
    import_rules_done_arrear_trades_of_last_3_months()
    import_rules_done_past_due_trades_between_last_3_to_12_months()
    import_rules_done_past_due_trades_of_last_3_months()
    import_rules_done_timely_trades_between_last_3_to_12_months()
    import_rules_done_timely_trades_of_last_3_months()
    import_rules_done_trades_average_delay_days()
    import_rules_done_trades_total_amount()
