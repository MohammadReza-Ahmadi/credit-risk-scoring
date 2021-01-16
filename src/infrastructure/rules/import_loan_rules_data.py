from data.rule.loan.rules_loan_arrear_total_balance_ratios import RuleArrearLoansTotalBalanceRatio
from data.rule.loan.rules_loan_arrear_total_counts import RuleArrearLoansTotalCount
from data.rule.loan.rules_loan_monthly_installments_total_balance_ratios import RuleLoanMonthlyInstallmentsTotalBalanceRatio
from data.rule.loan.rules_loan_total_counts import RuleLoansTotalCount
from data.rule.loan.rules_loan_overdue_total_balance_ratios import RuleLoanOverdueTotalBalanceRatio
from data.rule.loan.rules_loan_past_due_total_balance_ratios import RuleLoanPastDueTotalBalanceRatio
from data.rule.loan.rules_loan_past_due_total_counts import RulePastDueLoansTotalCount
from data.rule.loan.rules_loan_suspicious_total_balance_ratios import RuleSuspiciousLoansTotalBalanceRatio
from data.rule.loan.rules_loan_suspicious_total_counts import RuleSuspiciousLoansTotalCount
from service.util import create_rule
from src import program


def import_rules_loans_total_count_h11():
    # Loans = 0	00	H1101P0	کاربر هیچگونه تسهیلات در جریان ندارد
    rule = RuleLoansTotalCount()
    rule.drop_collection()
    rule.save(create_rule(rule, 'H1101P0', 0, 0, 0, 'کاربر هیچگونه تسهیلات در جریان ندارد'))

    # Loans = 1	20	H1102P20	کاربر ۱ تسهیلات در جریان دارد
    rule = RuleLoansTotalCount()
    rule.save(create_rule(rule, 'H1102P20', 1, 1, 20, 'کاربر ۱ تسهیلات در جریان دارد'))

    # Loans = 2	10	H1103P10	کاربر ۲ تسهیلات در جریان دارد
    rule = RuleLoansTotalCount()
    rule.save(create_rule(rule, 'H1103P10', 2, 2, 10, 'کاربر ۲ تسهیلات در جریان دارد'))

    # Loans = 3	01	H1104P1	کاربر ۳ تسهیلات در جریان دارد
    rule = RuleLoansTotalCount()
    rule.save(create_rule(rule, 'H1104P1', 3, 3, 1, 'کاربر ۳ تسهیلات در جریان دارد'))

    # Loans = 4	-20	H1105N20	کاربر ۴ تسهیلات در جریان دارد
    rule = RuleLoansTotalCount()
    rule.save(create_rule(rule, 'H1105N20', 4, 4, -20, 'کاربر ۴ تسهیلات در جریان دارد'))

    # Loans = 5	-30	H1106N30	کاربر ۵ تسهیلات در جریان دارد
    rule = RuleLoansTotalCount()
    rule.save(create_rule(rule, 'H1106N30', 5, 5, -30, 'کاربر ۵ تسهیلات در جریان دارد'))

    # Loans >= 6	-50	H1107N50	کاربر بیش از ۵ تسهیلات در جریان دارد
    rule = RuleLoansTotalCount()
    rule.save(create_rule(rule, 'H1107N50', 6, 999, -50, 'کاربر بیش از ۵ تسهیلات در جریان دارد'))


def import_rules_loan_monthly_installments_total_balance_ratio_v16():
    # MonthlyInstallments = 0	00	V1601P0	کاربر پرداخت اقساط ندارد
    rule = RuleLoanMonthlyInstallmentsTotalBalanceRatio()
    rule.drop_collection()
    rule.save(create_rule(rule, 'V1601P0', 0, 0, 0, 'کاربر پرداخت اقساط ندارد'))

    # 0.001 <= MonthlyInstallments ≤ 0.5	10	V1602P10	نسبت بین 0.001 و 0.5 می‌باشد
    rule = RuleLoanMonthlyInstallmentsTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1602P10', 0.001, 0.5, 10, 'نسبت بین 0.001 و 0.5 می‌باشد'))

    # 0.501 <= MonthlyInstallments ≤ 1	20	V1603P20	نسبت بین 0.501 و 1 می‌باشد
    rule = RuleLoanMonthlyInstallmentsTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1603P20', 0.501, 1, 20, 'نسبت بین 0.501 و 1 می‌باشد'))

    # 1.001 <= MonthlyInstallments ≤ 1.2	-2	V1604N2	نسبت بین 1.001 و 1.2 می‌باشد
    rule = RuleLoanMonthlyInstallmentsTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1604N2', 1.001, 1.2, -2, 'نسبت بین 1.001 و 1.2 می‌باشد'))

    # 1.201 <= MonthlyInstallments ≤ 2	-10	V1605N10	نسبت بین 1.201 و 2 می‌باشد
    rule = RuleLoanMonthlyInstallmentsTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1605N10', 1.201, 2, -10, 'نسبت بین 1.201 و 2 می‌باشد'))

    # MonthlyInstallments >= 2.001	-20	V1606N20	نسبت بیش از 2 می‌باشد
    rule = RuleLoanMonthlyInstallmentsTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1606N20', 2.001, 999, -20, 'نسبت بیش از 2 می‌باشد'))


def import_rules_overdue_loans_total_balance_ratio_v18():
    # CurrentLoanAmountRatio = 0	00	V1801P0	کاربر تسهیلات جاری ندارد
    rule = RuleLoanOverdueTotalBalanceRatio()
    rule.drop_collection()
    rule.save(create_rule(rule, 'V1801P0', 0, 0, 0, 'کاربر تسهیلات جاری ندارد'))

    # 0.001 <= CurrentLoanAmountRatio ≤ 0.5	05	V1802P5	نسبت بین 0.001 و 0.5 می‌باشد
    rule = RuleLoanOverdueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1802P5', 0.001, 0.5, 5, 'نسبت بین 0.001 و 0.5 می‌باشد'))

    # 0.501 <= CurrentLoanAmountRatio ≤ 1	10	V1803P10	نسبت بین 0.501 و 1 می‌باشد
    rule = RuleLoanOverdueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1803P10', 0.501, 1, 10, 'نسبت بین 0.501 و 1 می‌باشد'))

    # 1.001 <= CurrentLoanAmountRatio ≤ 1.5	-05	V1804N5	نسبت بین 1.001 و 1.5 می‌باشد
    rule = RuleLoanOverdueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1804N5', 1.001, 1.5, -5, 'نسبت بین 1.001 و 1.5 می‌باشد'))

    # 1.501 <= CurrentLoanAmountRatio ≤ 2	-10	V1805N10	نسبت بین 1.501 و 2 می‌باشد
    rule = RuleLoanOverdueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1805N10', 1.501, 2, -10, 'نسبت بین 1.501 و 2 می‌باشد'))

    # CurrentLoanAmountRatio >= 2.001	-20	V1806N20	نسبت بیش از 2 می‌باشد
    rule = RuleLoanOverdueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1806N20', 2.001, 999, -20, 'نسبت بیش از 2 می‌باشد'))


def import_rules_past_due_loans_total_balance_ratio_v19():
    # PastDueLoanAmountRatio = 0	10	V1901P10	کاربر تسهیلات سررسیدگذشته ندارد
    rule = RuleLoanPastDueTotalBalanceRatio()
    rule.drop_collection()
    rule.save(create_rule(rule, 'V1901P10', 0, 0, 10, 'کاربر تسهیلات سررسیدگذشته ندارد'))

    # 0.001 <= PastDueLoanAmountRatio ≤ 0.1	-05	V1902N5	نسبت بین 0.001 و 0.1 می‌باشد
    rule = RuleLoanPastDueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1902N5', 0.001, 0.1, -5, 'نسبت بین 0.001 و 0.1 می‌باشد'))

    # 0.101 <= PastDueLoanAmountRatio ≤ 0.2	-10	V1903N10	نسبت بین 0.101 و 0.2 می‌باشد
    rule = RuleLoanPastDueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1903N10', 0.101, 0.2, -10, 'نسبت بین 0.101 و 0.2 می‌باشد'))

    # 0.201 <= PastDueLoanAmountRatio ≤ 0.3	-20	V1904N20	نسبت بین 0.201 و 0.3 می‌باشد
    rule = RuleLoanPastDueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1904N20', 0.201, 0.3, -20, 'نسبت بین 0.201 و 0.3 می‌باشد'))

    # 0.301 <= PastDueLoanAmountRatio ≤ 0.5	-30	V1905N30	نسبت بین 0.301 و 0.5 می‌باشد
    rule = RuleLoanPastDueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1905N30', 0.301, 0.5, -30, 'نسبت بین 0.301 و 0.5 می‌باشد'))

    # PastDueLoanAmountRatio >= 0.501	-40	V1906N40	نسبت بیش از 0.5 می‌باشد
    rule = RuleLoanPastDueTotalBalanceRatio()
    rule.save(create_rule(rule, 'V1906N40', 0.501, 999, -40, 'نسبت بیش از 0.5 می‌باشد'))


def import_rules_arrear_loans_total_balance_ratios_v20():
    # DelayedLoanAmountRatio = 0	15	V2001P15	کاربر تسهیلات معوق ندارد
    rule = RuleArrearLoansTotalBalanceRatio()
    rule.drop_collection()
    rule.save(create_rule(rule, 'V2001P15', 0, 0, 15, 'کاربر تسهیلات معوق ندارد'))

    # 0.001 <= DelayedLoanAmountRatio ≤ 0.1	-10	V2002N10	نسبت بین 0 و 0.1 می‌باشد
    rule = RuleArrearLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2002N10', 0.001, 0.1, -10, 'نسبت بین 0 و 0.1 می‌باشد'))

    # 0.101 <= DelayedLoanAmountRatio ≤ 0.2	-20	V2003N20	نسبت بین 0.101 و 0.2 می‌باشد
    rule = RuleArrearLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2003N20', 0.101, 0.2, -20, 'نسبت بین 0.101 و 0.2 می‌باشد'))

    # 0.201 <= DelayedLoanAmountRatio ≤ 0.3	-30	V2004N30	نسبت بین 0.201 و 0.3 می‌باشد
    rule = RuleArrearLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2004N30', 0.201, 0.3, -30, 'نسبت بین 0.201 و 0.3 می‌باشد'))

    # 0.301 <= DelayedLoanAmountRatio ≤ 0.5	-40	V2005N40	نسبت بین  0.301و 0.5 می‌باشد
    rule = RuleArrearLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2005N40', 0.301, 0.5, -40, 'نسبت بین  0.301و 0.5 می‌باشد'))

    # DelayedLoanAmountRatio >= 0.501	-50	V2006N50	نسبت بیش از 0.5 می‌باشد
    rule = RuleArrearLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2006N50', 0.501, 999, -50, 'نسبت بیش از 0.5 می‌باشد'))


def import_rules_suspicious_loans_total_balance_ratio_v21():
    # DoubtfulCollectionAmountRatio = 0	20	V2101P20	کاربر تسهیلات مشکوک‌الوصول ندارد
    rule = RuleSuspiciousLoansTotalBalanceRatio()
    rule.drop_collection()
    rule.save(create_rule(rule, 'V2101P20', 0, 0, 20, 'کاربر تسهیلات مشکوک‌الوصول ندارد'))

    # 0.001 <= DoubtfulCollectionAmountRatio ≤ 0.1	-20	V2102N20	نسبت بین 0.001 و 0.1 می‌باشد
    rule = RuleSuspiciousLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2102N20', 0.001, 0.1, -20, 'نسبت بین 0.001 و 0.1 می‌باشد'))

    # 0.101 <= DoubtfulCollectionAmountRatio ≤ 0.2	-30	V2103N30	نسبت بین 0.101 و 0.2 می‌باشد
    rule = RuleSuspiciousLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2103N30', 0.101, 0.2, -30, 'نسبت بین 0.101 و 0.2 می‌باشد'))

    # 0.201 <= DoubtfulCollectionAmountRatio ≤ 0.3	-40	V2104N40	نسبت بین 0.201 و 0.3 می‌باشد
    rule = RuleSuspiciousLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2104N40', 0.201, 0.3, -40, 'نسبت بین 0.201 و 0.3 می‌باشد'))

    # 0.301 <= DoubtfulCollectionAmountRatio ≤ 0.5	-50	V2105N50	نسبت بین 0.301 و 0.5 می‌باشد
    rule = RuleSuspiciousLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2105N50', 0.301, 0.5, -50, 'نسبت بین 0.301 و 0.5 می‌باشد'))

    # DoubtfulCollectionAmountRatio >= 0.501	-60	V2106N60	نسبت بیش از 0.5 می‌باشد
    rule = RuleSuspiciousLoansTotalBalanceRatio()
    rule.save(create_rule(rule, 'V2106N60', 0.501, 999, -60, 'نسبت بیش از 0.5 می‌باشد'))


def import_rules_past_due_loans_total_count_t33():
    # PastDueLoans = 0	10	T3301P10	کاربر تسهیلات سررسید گذشته ندارد
    rule = RulePastDueLoansTotalCount()
    rule.drop_collection()
    rule.save(create_rule(rule, 'T3301P10', 0, 0, 10, 'کاربر تسهیلات سررسید گذشته ندارد'))

    # PastDueLoans = 1	00	T3302P0	کاربر 1 تسهیلات سررسید گذشته دارد
    rule = RulePastDueLoansTotalCount()
    rule.save(create_rule(rule, 'T3302P0', 1, 1, 0, 'کاربر 1 تسهیلات سررسید گذشته دارد'))

    # PastDueLoans = 2	-10	T3303N10	کاربر ۲ تسهیلات سررسید گذشته دارد
    rule = RulePastDueLoansTotalCount()
    rule.save(create_rule(rule, 'T3303N10', 2, 2, -10, 'کاربر ۲ تسهیلات سررسید گذشته دارد'))

    # PastDueLoans = 3	-20	T3304N20	کاربر ۳ تسهیلات سررسید گذشته دارد
    rule = RulePastDueLoansTotalCount()
    rule.save(create_rule(rule, 'T3304N20', 3, 3, -20, 'کاربر ۳ تسهیلات سررسید گذشته دارد'))

    # PastDueLoans >= 4	-30	T3305N30	کاربر بیش از ۳ تسهیلات سررسید گذشته دارد
    rule = RulePastDueLoansTotalCount()
    rule.save(create_rule(rule, 'T3305N30', 4, 999, -30, 'کاربر بیش از ۳ تسهیلات سررسید گذشته دارد'))


def import_rules_arrear_loans_total_count_t34():
    # DelayedLoans = 0	20	T3401P20	کاربر تسهیلات معوق ندارد
    rule = RuleArrearLoansTotalCount()
    rule.drop_collection()
    rule.save(create_rule(rule, 'T3401P20', 0, 0, 20, 'کاربر تسهیلات معوق ندارد'))

    # DelayedLoans = 1	-10	T3402N10	کاربر 1 تسهیلات معوق دارد
    rule = RuleArrearLoansTotalCount()
    rule.save(create_rule(rule, 'T3402N10', 1, 1, -10, 'کاربر 1 تسهیلات معوق دارد'))

    # DelayedLoans = 2	-20	T3403N20	کاربر ۲ تسهیلات معوق دارد
    rule = RuleArrearLoansTotalCount()
    rule.save(create_rule(rule, 'T3403N20', 2, 2, -20, 'کاربر ۲ تسهیلات معوق دارد'))

    # DelayedLoans = 3	-30	T3404N30	کاربر ۳ تسهیلات معوق دارد
    rule = RuleArrearLoansTotalCount()
    rule.save(create_rule(rule, 'T3404N30', 3, 3, -30, 'کاربر ۳ تسهیلات معوق دارد'))

    # DelayedLoans >= 4	-40	T3405N40	کاربر بیش از ۳ تسهیلات معوق دارد
    rule = RuleArrearLoansTotalCount()
    rule.save(create_rule(rule, 'T3405N40', 4, 999, -40, 'کاربر بیش از ۳ تسهیلات معوق دارد'))


def import_rules_suspicious_loans_total_count_t35():
    # DoubfulCollectionLoans = 0	30	T3501P30	کاربر تسهیلات مشکوک الوصول ندارد
    rule = RuleSuspiciousLoansTotalCount()
    rule.drop_collection()
    rule.save(create_rule(rule, 'T3501P30', 0, 0, 30, 'کاربر تسهیلات مشکوک الوصول ندارد'))

    # DoubfulCollectionLoans = 1	-20	T3502N20	کاربر 1 تسهیلات مشکوک الوصول دارد
    rule = RuleSuspiciousLoansTotalCount()
    rule.save(create_rule(rule, 'T3502N20', 1, 1, -20, 'کاربر 1 تسهیلات مشکوک الوصول دارد'))

    # DoubfulCollectionLoans = 2	-30	T3503N30	کاربر ۲ تسهیلات مشکوک الوصول دارد
    rule = RuleSuspiciousLoansTotalCount()
    rule.save(create_rule(rule, 'T3503N30', 2, 2, -30, 'کاربر ۲ تسهیلات مشکوک الوصول دارد'))

    # DoubfulCollectionLoans = 3	-40	T3504N40	کاربر ۳ تسهیلات مشکوک الوصول دارد
    rule = RuleSuspiciousLoansTotalCount()
    rule.save(create_rule(rule, 'T3504N40', 3, 3, -40, 'کاربر ۳ تسهیلات مشکوک الوصول دارد'))

    # DoubfulCollectionLoans >= 4	-50	T3505N50	کاربر بیش از ۳ تسهیلات مشکوک الوصول دارد
    rule = RuleSuspiciousLoansTotalCount()
    rule.save(create_rule(rule, 'T3505N50', 4, 999, -50, 'کاربر بیش از ۳ تسهیلات مشکوک الوصول دارد'))


if __name__ == '__main__':
    program.launch_app()
    import_rules_loans_total_count_h11()
    import_rules_past_due_loans_total_count_t33()
    import_rules_arrear_loans_total_count_t34()
    import_rules_suspicious_loans_total_count_t35()
    import_rules_loan_monthly_installments_total_balance_ratio_v16()
    import_rules_overdue_loans_total_balance_ratio_v18()
    import_rules_past_due_loans_total_balance_ratio_v19()
    import_rules_arrear_loans_total_balance_ratios_v20()
    import_rules_suspicious_loans_total_balance_ratio_v21()
