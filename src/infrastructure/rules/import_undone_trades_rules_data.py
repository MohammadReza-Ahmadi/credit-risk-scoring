from data.rule.undone.rules_undone_arrear_trades_counts import RuleUnDoneArrearTradesCount
from data.rule.undone.rules_undone_arrear_trades_total_balance_of_last_year_ratios import RuleUnDoneArrearTradesTotalBalanceOfLastYearRatio
from data.rule.undone.rules_undone_past_due_trades_counts import RuleUnDonePastDueTradesCount
from data.rule.undone.rules_undone_past_due_trades_total_balance_of_last_year_ratios import RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio
from data.rule.undone.rules_undone_undue_trades_counts import RuleUnDoneUndueTradesCount
from data.rule.undone.rules_undone_undue_trades_total_balance_of_last_year_ratios import RuleUnDoneUndueTradesTotalBalanceOfLastYearRatio
from service.util import creat_rule
from src import program


def import_rules_undone_undue_trades_counts():
    # NumNotDueDeal = 0 00 	H1001P0	کاربر تعامل سررسید نشده ندارد
    rule = RuleUnDoneUndueTradesCount()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'H1001P0', 0, 0, 0, 'کاربر تعامل سررسید نشده ندارد'))

    # NumNotDueDeal = 1 01	H1002P2	کاربر 1 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1002P2', 1, 1, 1, 'کاربر 1 تعامل سررسید نشده دارد'))

    # NumNotDueDeal = 2	05	H1003P5	کاربر 2 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1003P5', 2, 2, 5, 'کاربر 2 تعامل سررسید نشده دارد'))

    # NumNotDueDeal = 3	10	H1004P10	کاربر 3 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1004P10', 3, 3, 10, 'کاربر 3 تعامل سررسید نشده دارد'))

    # NumNotDueDeal = 4	20	H1005P20	کاربر 4 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1005P20', 4, 4, 20, 'کاربر 4 تعامل سررسید نشده دارد'))

    # NumNotDueDeal = 5	10	H1006P10	کاربر 5 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1006P10', 5, 5, 10, 'کاربر 5 تعامل سررسید نشده دارد'))

    # NumNotDueDeal = 6	00	H1007P0	کاربر 6 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1007P0', 6, 6, 0, 'کاربر 6 تعامل سررسید نشده دارد'))

    # 7 <= NumNotDueDeal ≤ 10	-10	H1008N10	کاربر بین 7 تا 10 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1008N10', 7, 10, -10, 'کاربر بین 7 تا 10 تعامل سررسید نشده دارد'))

    # 11 <= NumNotDueDeal ≤ 20	-20	H1009N20	کاربر بین 11 تا 20 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1009N20', 11, 20, -20, 'کاربر بین 11 تا 20 تعامل سررسید نشده دارد'))

    # 21 <= NumNotDueDeal ≤ 30	-30	H1010N30	کاربر بین 21 تا 30 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1010N30', 21, 30, -30, 'کاربر بین 21 تا 30 تعامل سررسید نشده دارد'))

    # NotDueDeal >= 31	-50	H1011N50	کاربر بیش از 30 تعامل سررسید نشده دارد
    rule = RuleUnDoneUndueTradesCount()
    rule.save(creat_rule(rule, 'H1011N50', 31, 999, -50, 'کاربر بیش از 30 تعامل سررسید نشده دارد'))


def import_rules_undone_past_due_trades_total_balance_of_last_year_ratios():
    # UnfinishedB30Din1YRatio = 0	20	V1301P20	کاربر تعامل سررسید گذشته خاتمه نیافته ندارد
    rule = RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'V1301P20', 0, 0, 20, ' تعامل سررسید گذشته خاتمه نیافته ندارد'))

    # 0.001 <= UnfinishedB30Din1YRatio ≤ 0.5	00	V1302P0	نسبت بین 0.001 و 0.5 می‌باشد
    rule = RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1302P0', 0.001, 0.5, 0, 'نسبت بین 0.001 و 0.5 می‌باشد'))

    # 0.5001 <= UnfinishedB30Din1YRatio ≤ 1	-10	V1303N10	نسبت بین 0.5001 و 1 می‌باشد
    rule = RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1303N10', 0.5001, 1, -10, 'نسبت بین 0.5001 و 1 می‌باشد'))

    # If SDA (denominator) = 0	-20	V1304N20	کاربر در یکسال گذشته تعامل موفقی ندارد (اولین تعامل در حال انجام سررسید گذشته شده)
    rule = RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1304N20', 0, 0, -20, 'کاربر در یکسال گذشته تعامل موفقی ندارد (اولین تعامل در حال انجام سررسید گذشته شده)'))

    # 1 < UnfinishedB30Din1YRatio ≤ 1.5	-20	V1305N20	نسبت بین 1.001 و 1.5 می‌باشد
    rule = RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1305N20', 1.001, 1.5, -20, 'نسبت بین 1.001 و 1.5 می‌باشد'))

    # 1.501 <= UnfinishedB30Din1YRatio ≤ 2	-30	V1306N30	نسبت بین 1.501 و 2 می‌باشد
    rule = RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1306N30', 1.501, 2, -30, 'نسبت بین 1.501 و 2 می‌باشد'))

    # UnfinishedB30Din1YRatio > 2	-40	V1307N40	نسبت بیش از 2 می‌باشد
    rule = RuleUnDonePastDueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1307N40', 3, 999, -40, 'نسبت بیش از 2 می‌باشد'))


def import_rules_undone_arrear_trades_total_balance_of_last_year_ratios():
    # UnfinishedB30Din1YRatio = 0	30	V1401P30	کاربر تعامل معوق خاتمه نیافته ندارد
    rule = RuleUnDoneArrearTradesTotalBalanceOfLastYearRatio()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'V1401P30', 0, 0, 30, 'کاربر تعامل معوق خاتمه نیافته ندارد'))

    # 0.001 <= UnfinishedB30Din1YRatio ≤ 0.5	00	V1402P0	نسبت بین 0.001 و 0.5 می‌باشد
    rule = RuleUnDoneArrearTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1402P0', 0.001, 0.5, 0, 'نسبت بین 0.001 و 0.5 می‌باشد'))

    # 0.5001 <= UnfinishedB30Din1YRatio ≤ 1	-10	V1403N10	نسبت بین 0.5001 و 1 می‌باشد
    rule = RuleUnDoneArrearTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1403N10', 0.5001, 1, -10, 'نسبت بین 0.5001 و 1 می‌باشد'))

    # If SDA (denominator) = 0	-20	V1404N20	کاربر در یکسال گذشته تعامل موفقی ندارد (اولین تعامل در حال انجام معوق است)
    rule = RuleUnDoneArrearTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1404N20', 0, 0, -20, 'کاربر در یکسال گذشته تعامل موفقی ندارد (اولین تعامل در حال انجام معوق است)'))

    # 1 < UnfinishedB30Din1YRatio ≤ 1.5	-20	V1405N20	نسبت بین 1.001 و 1.5 می‌باشد
    rule = RuleUnDoneArrearTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1405N20', 1.001, 1.5, -20, 'نسبت بین 1.001 و 1.5 می‌باشد'))

    # 1.501 <= UnfinishedB30Din1YRatio ≤ 2	-30	V1406N30	نسبت بین 1.501 و 2 می‌باشد
    rule = RuleUnDoneArrearTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1406N30', 1.501, 2, -30, 'نسبت بین 1.501 و 2 می‌باشد'))

    # UnfinishedB30Din1YRatio > 2	-40	V1407N40	نسبت بیش از 2 می‌باشد
    rule = RuleUnDoneArrearTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1407N40', 3, 999, -40, 'نسبت بیش از 2 می‌باشد'))


def import_rules_undone_undue_trades_total_balance_of_last_year_ratios():
    # If SDA(denominator) = 0	00	V1501P0	کاربر در یکسال گذشته تعامل موفقی ندارد (اولین تعامل در حال انجام است)
    rule = RuleUnDoneUndueTradesTotalBalanceOfLastYearRatio()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'V1501P0', 0, 0, 0, 'کاربر در یکسال گذشته تعامل موفقی ندارد (اولین تعامل در حال انجام است)'))

    # 0 ≤ NotDueDealAmountRatio ≤ 1	00	V1502P0	نسبت بین 0 و ۱ می‌باشد
    rule = RuleUnDoneUndueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1502P0', 0, 1, 0, 'نسبت بین 0 و ۱ می‌باشد'))

    # 1.001 < NotDueDealAmountRatio ≤ 1.5	-05	V1503N5	نسبت بین 1 و 1.5 می‌باشد
    rule = RuleUnDoneUndueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1503N5', 0.001, 1.5, -5, 'نسبت بین 1 و 1.5 می‌باشد'))

    # 1.501 <= NotDueDealAmountRatio ≤ 2	-10	V1504N10	نسبت بین 1.5 و ۲ می‌باشد
    rule = RuleUnDoneUndueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1504N10', 1.501, 2, -10, 'نسبت بین 1.5 و ۲ می‌باشد'))

    # 2.001 <= NotDueDealAmountRatio ≤ 3	-20	V1505N20	نسبت بین ۲ و ۳ می‌باشد
    rule = RuleUnDoneUndueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1505N20', 2.001, 3, -20, 'نسبت بین ۲ و ۳ می‌باشد'))

    # NotDueDealAmountRatio > 3	-30	V1506N30	نسبت بیش از ۳ می‌باشد
    rule = RuleUnDoneUndueTradesTotalBalanceOfLastYearRatio()
    rule.save(creat_rule(rule, 'V1506N30', 3.001, 999, -30, 'نسبت بیش از ۳ می‌باشد'))


def rules_undone_past_due_trades_counts():
    # UnfinishedB30DayDelay = 0	10	T2601P10	کاربر در سه ماه گذشته هیچ تعامل سررسید گذشته‌ای نداشته است
    rule = RuleUnDonePastDueTradesCount()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T2601P10', 0, 0, 10, 'کاربر در سه ماه گذشته هیچ تعامل سررسید گذشته‌ای نداشته است'))

    # UnfinishedB30DayDelay = 1	-20	T2602N20	کاربر در سه ماه گذشته یک تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDonePastDueTradesCount()
    rule.save(creat_rule(rule, 'T2602N20', 1, 1, -20, 'کاربر در سه ماه گذشته یک تعامل سررسید گذشته‌ داشته است'))

    # 2 <= UnfinishedB30DayDelay ≤ 3	-30	T2603N30	کاربر در سه ماه گذشته بین ۲ تا 3 تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDonePastDueTradesCount()
    rule.save(creat_rule(rule, 'T2603N30', 2, 3, -30, 'کاربر در سه ماه گذشته بین ۲ تا 3 تعامل سررسید گذشته‌ داشته است'))

    # 4 <= UnfinishedB30DayDelay ≤ 6	-40	T2604N40	کاربر در سه ماه گذشته بین ۴ تا 6 تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDonePastDueTradesCount()
    rule.save(creat_rule(rule, 'T2604N40', 4, 6, -40, 'کاربر در سه ماه گذشته بین ۴ تا 6 تعامل سررسید گذشته‌ داشته است'))

    # 7 <= UnfinishedB30DayDelay ≤ 10	-50	T2605N50	کاربر در سه ماه گذشته بین ۷ تا 10 تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDonePastDueTradesCount()
    rule.save(creat_rule(rule, 'T2605N50', 7, 10, -50, 'کاربر در سه ماه گذشته بین ۷ تا 10 تعامل سررسید گذشته‌ داشته است'))

    # UnfinishedB30DayDelay >= 11	-60	T2606N60	کاربر در سه ماه گذشته بیش از 10 تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDonePastDueTradesCount()
    rule.save(creat_rule(rule, 'T2606N60', 11, 999, -60, 'کاربر در سه ماه گذشته بیش از 10 تعامل سررسید گذشته‌ داشته است'))


def rules_undone_arrear_trades_counts():
    # UnfinishedA30DayDelay = 0	20	T2701P20	کاربر در سه ماه گذشته هیچ تعامل سررسید گذشته‌ای نداشته است
    rule = RuleUnDoneArrearTradesCount()
    rule.drop_collection()
    rule.save(creat_rule(rule, 'T2701P20', 0, 0, 20, 'کاربر در سه ماه گذشته هیچ تعامل سررسید گذشته‌ای نداشته است'))

    # UnfinishedA30DayDelay = 1	-20	T2702N20	کاربر در سه ماه گذشته یک سررسید گذشته‌ داشته است
    rule = RuleUnDoneArrearTradesCount()
    rule.save(creat_rule(rule, 'T2702N20', 1, 1, -20, 'کاربر در سه ماه گذشته یک سررسید گذشته‌ داشته است'))

    # 2 <= UnfinishedA30DayDelay ≤ 3	-30	T2703N30	کاربر در سه ماه گذشته بین 2 تا 3 تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDoneArrearTradesCount()
    rule.save(creat_rule(rule, 'T2703N30', 2, 3, -30, 'کاربر در سه ماه گذشته بین 2 تا 3 تعامل سررسید گذشته‌ داشته است'))

    # 4 <= UnfinishedA30DayDelay ≤ 6	-40	T2704N40	کاربر در سه ماه گذشته بین 4 تا 6 تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDoneArrearTradesCount()
    rule.save(creat_rule(rule, 'T2704N40', 4, 6, -40, 'کاربر در سه ماه گذشته بین 4 تا 6 تعامل سررسید گذشته‌ داشته است'))

    # 7 <= UnfinishedA30DayDelay ≤ 10	-50	T2705N50	کاربر در سه ماه گذشته بین 7 تا 10 تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDoneArrearTradesCount()
    rule.save(creat_rule(rule, 'T2705N50', 7, 10, -50, 'کاربر در سه ماه گذشته بین 7 تا 10 تعامل سررسید گذشته‌ داشته است'))

    # UnfinishedA30DayDelay >= 11	-60	T2706N60	کاربر در سه ماه گذشته بیش از 10 تعامل سررسید گذشته‌ داشته است
    rule = RuleUnDoneArrearTradesCount()
    rule.save(creat_rule(rule, 'T2706N60', 11, 999, -60, 'کاربر در سه ماه گذشته بیش از 10 تعامل سررسید گذشته‌ داشته است'))


if __name__ == '__main__':
    program.launch_app()
    import_rules_undone_arrear_trades_total_balance_of_last_year_ratios()
    import_rules_undone_past_due_trades_total_balance_of_last_year_ratios()
    import_rules_undone_undue_trades_counts()
    import_rules_undone_undue_trades_total_balance_of_last_year_ratios()
    rules_undone_arrear_trades_counts()
    rules_undone_past_due_trades_counts()
