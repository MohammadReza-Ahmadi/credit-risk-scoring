from mongoengine.queryset.visitor import Q

from data.rules import Rule
from infrastructure.constants import rules_max_val
from service.util import create_new_rule
from src import program


def import_rule_history_master():
    # Delete all histories(H) rules
    l2_rules: [Rule] = Rule.objects(Q(parent='H'))
    for r in l2_rules:
        l3_rules: [Rule] = Rule.objects(Q(parent=r.code))
        l3_rules.delete()
    l2_rules.delete()
    l1_rule = Rule.objects(Q(code='H'))
    l1_rule.delete()
    print('Histories(H) rules are deleted.')
    # define Identities(I)' rules master: level 1
    rule = Rule()
    # rule.drop_collection()
    rule = create_new_rule(rule, 1, None, 'H', 'سوابق تعاملات', 30, 270)
    rule.save()
    print('Histories(H) master rule is created.')


def import_rules_history_membership_days_counts_h5():
    # define History(H)' rules of membership_days master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'H', 'H5', 'مدت زمان عضویت فعال', 6.67, 60)
    rule.save()

    # define History(H)' rules of membership_days details: level 3
    # Just Registered MembershipDaysWithAtleast1SD == 0 	00	H0501P0	عضو جدید
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H5', 'H0501P0', 'عضو جدید', 0, 0, 0)
    rule.save()

    #  1 <=  MembershipDaysWithAtleast1SD ≤ 90	    10	H0502P10	 عضویت بین 1 تا 90 روز
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H5', 'H0502P10', ' عضویت بین 1 تا 90 روز', 1.11, 10, 1, 90)
    rule.save()

    # 91 <=  MembershipDaysWithAtleast3SD ≤ 180	    20	H0503P20	 عضویت بین 91 تا 180 روز
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H5', 'H0503P20', 'عضویت بین 91 تا 180 روز', 2.22, 20, 91, 180)
    rule.save()

    # 181 <=  MembershipDaysWithAtleast5SD ≤ 365	30	H0504P30	 عضویت بین 181 تا 365 روز
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H5', 'H0504P30', ' عضویت بین 181 تا 365 روز', 3.33, 30, 181, 365)
    rule.save()

    # 366 <= MembershipDaysWithAtleast10SD ≤ 720	40	H0505P40	 عضویت بین 366 تا 720 روز
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H5', 'H0505P40', ' عضویت بین 366 تا 720 روز', 4.44, 40, 366, 720)
    rule.save()

    # 721 <= MembershipDaysWithAtleast15SD ≤ 1080	50	H0506P50	 عضویت بین 721 تا 1080 روز
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H5', 'H0506P50', ' عضویت بین 721 تا 1080 روز', 5.50, 50, 721, 1080)
    rule.save()

    #     MembershipDaysWithAtleast20SD >= 1081	    60	H0507P60	 عضویت بیش از 1081 روز
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H5', 'H0507P60', ' عضویت بیش از 1081 روز', 6.67, 60, 1081, rules_max_val)
    rule.save()
    print('Histories(H) membership_days_counts_h5 rules are created.')


def import_rules_history_done_timely_trades_of_last_3_months_h6():
    # define History(H)' rules of done_timely_trades_of_last_3_months master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'H', 'H6', 'تعداد تعاملات موفق در 3 ماه گذشته', 4.44, 40)
    rule.save()

    # define History(H)' rules of done_timely_trades_of_last_3_months details: level 3
    # Last3MSD = 0	00	H0601P0	کاربر در سه ماه گذشته هیچ تعامل موفقی با سایر کاربران نداشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H6', 'H0601P0', 'کاربر در سه ماه گذشته هیچ تعامل موفقی با سایر کاربران نداشته است', 0, 0, 0, 0)
    rule.save()

    # Last3MSD = 1	10	H0602P10	کاربر در سه ماه گذشته 1 تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H6', 'H0602P10', 'کاربر در سه ماه گذشته 1 تعامل موفق با سایر کاربران داشته است', 1.11, 10, 1, 1)
    rule.save()

    # Last3MSD = 2	20	H0603P20	کاربر در سه ماه گذشته ۲ تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H6', 'H0603P20', 'کاربر در سه ماه گذشته ۲ تعامل موفق با سایر کاربران داشته است', 2.22, 20, 2, 2)
    rule.save()

    # Last3MSD = 3	30	H0604P30	کاربر در سه ماه گذشته 3 تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H6', 'H0601P0', 'کاربر در سه ماه گذشته 3 تعامل موفق با سایر کاربران داشته است', 3.33, 30, 3, 3)
    rule.save()

    # Last3MSD ≥ 4	40	H0605P40	کاربر در سه ماه گذشته بیش از 3 تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H6', 'H0605P40', 'کاربر در سه ماه گذشته بیش از 3 تعامل موفق با سایر کاربران داشته است', 4.44, 40, 4, 4)
    rule.save()
    print('Histories(H) done_timely_trades_of_last_3_months_h6 rules are created.')


def import_rules_history_done_timely_trades_between_last_3_to_12_months_h7():
    # define History(H)' rules of done_timely_trades_between_last_3_to_12_months master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'H', 'H7', 'تعداد تعاملات موفق در ۳ تا ۱۲ ماه گذشته', 4.44, 40)
    rule.save()

    # define History(H)' rules of done_timely_trades_of_last_3_months details: level 3
    # Last1YSD = 0	00	H0701P0	کاربر در یکسال گذشته هیچ تعامل موفقی با سایر کاربران نداشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H7', 'H0701P0', 'کاربر در یکسال گذشته هیچ تعامل موفقی با سایر کاربران نداشته است', 0, 0, 0, 0)
    rule.save()

    # Last1YSD = 1	05	H0702P05	کاربر در یکسال گذشته 1 تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H7', 'H0702P05', 'کاربر در یکسال گذشته 1 تعامل موفق با سایر کاربران داشته است', 0.56, 5, 1, 1)
    rule.save()

    # 2 <= Last1YSD ≤ 3	10	H0703P10	کاربر در یکسال گذشته بین 2 تا 3 تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H7', 'H0703P10', 'کاربر در یکسال گذشته بین 2 تا 3 تعامل موفق با سایر کاربران داشته است', 1.11, 10, 2, 3)
    rule.save()

    # 4 <= Last1YSD ≤ 6	20	H0704P20	کاربر در یکسال گذشته بین 4 تا 6 تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H7', 'H0704P20', 'کاربر در یکسال گذشته بین 4 تا 6 تعامل موفق با سایر کاربران داشته است', 2.22, 20, 4, 6)
    rule.save()

    # 7 <= Last1YSD ≤ 10	30	H0705P30	کاربر در یکسال گذشته بین 7 تا 10 تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H7', 'H0705P30', 'کاربر در یکسال گذشته بین 7 تا 10 تعامل موفق با سایر کاربران داشته است', 3.33, 30, 7, 10)
    rule.save()

    # Last1YSD >= 11	40	H0706P40	کاربر در یکسال گذشته بیش از 10 تعامل موفق با سایر کاربران داشته است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H7', 'H0706P40', 'کاربر در یکسال گذشته بیش از 10 تعامل موفق با سایر کاربران داشته است', 4.44, 40, 11,
                           rules_max_val)
    rule.save()
    print('Histories(H) done_timely_trades_between_last_3_to_12_months_h7 rules are created.')


def import_rules_history_recommended_to_others_counts_h8():
    # define History(H)' rules of recommended_to_others_counts master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'H', 'H8', 'پیشنهاد شدن کاربر به سایرین جهت انجام تعامل پس از انجام موفقیت آمیز تعامل', 4.44, 40)
    rule.save()

    # define History(H)' rules of recommended_to_others_counts details: level 3
    # Recommendation = 0	00	H0801P0	کاربر توسط کسی پیشنهاد نشده است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H8', 'H0801P0', 'کاربر توسط کسی پیشنهاد نشده است', 0, 0, 0, 0)
    rule.save()

    # Recommendation = 1	10	H0802P10	پیشنهاد شده توسط 1 نفر
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H8', 'H0802P10', 'پیشنهاد شده توسط 1 نفر', 1.11, 10, 1, 1)
    rule.save()

    # 2 < Recommendation ≤ 3	20	H0803P20	پیشنهاد شده توسط 2 تا 3 نفر
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H8', 'H0803P20', 'پیشنهاد شده توسط 2 تا 3 نفر', 2.22, 20, 2, 3)
    rule.save()

    # 4 < Recommendation ≤ 10	30	H0804P30	پیشنهاد شده توسط 4 تا 10 نفر
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H8', 'H0804P30', 'پیشنهاد شده توسط 4 تا 10 نفر', 3.33, 30, 4, 10)
    rule.save()

    # 11 < Recommendation ≤ 30	40	H0805P40	پیشنهاد شده توسط 11 تا 30 نفر
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H8', 'H0805P40', 'پیشنهاد شده توسط 11 تا 30 نفر', 4.44, 40, 11, 30)
    rule.save()

    # Recommendation > 30	50	H0806P50	پیشنهاد شده توسط بیش از 30 نفر
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H8', 'H0806P50', 'پیشنهاد شده توسط بیش از 30 نفر', 5.56, 50, 30, rules_max_val)
    rule.save()
    print('Histories(H) recommended_to_others_counts_h8 rules are created.')


def import_rules_history_star_counts_avgs_h9():
    # define History(H)' rules of star_counts_avgs master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'H', 'H9', ' امتیاز رضایتمندی دریافت شده از طرف مقابل پس از انجام موفقیت آمیز تعامل', 5.56, 50)
    rule.save()

    # define History(H)' rules of star_counts_avgs details: level 3
    # WeightedAveStars <= 1	00	H0901P0	کاربر به طور متوسط کمتر مساوی ۱ ستاره کسب کرده است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H9', 'H0901P0', 'کاربر به طور متوسط کمتر مساوی ۱ ستاره کسب کرده است', 0, 0, 0, 1)
    rule.save()

    # 1.001 <= WeightedAveStars ≤ 2	05	H0902P5	کاربر به طور متوسط بیش از ۱ و کمتر مساوی ۲ ستاره کسب کرده است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H9', 'H0902P5', 'کاربر به طور متوسط بیش از ۱ و کمتر مساوی ۲ ستاره کسب کرده است', 0.56, 5, 1.001, 2)
    rule.save()

    # 2.001 <= WeightedAveStars ≤ 3	10	H0903P10	کاربر به طور متوسط بیش از ۲ و کمتر مساوی ۳ ستاره کسب کرده است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H9', 'H0903P10', 'کاربر به طور متوسط بیش از ۲ و کمتر مساوی ۳ ستاره کسب کرده است', 1.11, 10, 2.001, 3)
    rule.save()

    # 3.001 <= WeightedAveStars ≤ 4	30	H0904P30	کاربر به طور متوسط بیش از ۳ و کمتر مساوی ۴ ستاره کسب کرده است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H9', 'H0904P30', 'کاربر به طور متوسط بیش از ۳ و کمتر مساوی ۴ ستاره کسب کرده است', 3.33, 30, 3.001, 4)
    rule.save()

    # 4.001 <= WeightedAveStars ≤ 5	50	H0905P50	کاربر به طور متوسط بیش از ۴ و کمتر مساوی ۵ ستاره کسب کرده است
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H9', 'H0905P50', 'کاربر به طور متوسط بیش از ۴ و کمتر مساوی ۵ ستاره کسب کرده است', 5.56, 50, 4.001, 5)
    rule.save()
    print('Histories(H) star_counts_avgs_h9 rules are created.')


def import_rules_history_undone_undue_trades_counts_h10():
    # define History(H)' rules of undone_undue_trades_counts master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'H', 'H10', 'تعداد تعاملات جاری سررسید نشده', 1.11, 10)
    rule.save()

    # define History(H)' rules of undone_undue_trades_counts details: level 3
    # NumNotDueDeal = 0 00 	H1001P0	کاربر تعامل سررسید نشده ندارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1001P0', 'کاربر تعامل سررسید نشده ندارد', 0, 0, 0, 0)
    rule.save()

    # NumNotDueDeal = 1 02	H1002P2	کاربر 1 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1002P2', 'کاربر 1 تعامل سررسید نشده دارد', 0.22, 2, 1, 1)
    rule.save()

    # NumNotDueDeal = 2	05	H1003P5	کاربر 2 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1003P5', 'کاربر 2 تعامل سررسید نشده دارد', 0.56, 5, 2, 2)
    rule.save()

    # NumNotDueDeal = 3	7	H1004P7	کاربر 3 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1004P7', 'کاربر 3 تعامل سررسید نشده دارد', 0.78, 7, 3, 3)
    rule.save()

    # NumNotDueDeal = 4	10	H1005P10	کاربر 4 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1005P10', 'کاربر 4 تعامل سررسید نشده دارد', 1.11, 10, 4, 4)
    rule.save()

    # NumNotDueDeal = 5	03	H1006P3	کاربر 5 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1006P3', 'کاربر 5 تعامل سررسید نشده دارد', 0.33, 3, 5, 5)
    rule.save()

    # NumNotDueDeal = 6	-1	H1007N1	کاربر 6 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1007N1', 'کاربر 6 تعامل سررسید نشده دارد', 0.11, -1, 6, 6)
    rule.save()

    # 7 <= NumNotDueDeal ≤ 10	-10	H1008N10	کاربر بین 7 تا 10 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1008N10', 'کاربر بین 7 تا 10 تعامل سررسید نشده دارد', 1.11, -10, 7, 10)
    rule.save()

    # 11 <= NumNotDueDeal ≤ 20	-20	H1009N20	کاربر بین 11 تا 20 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1009N20', 'کاربر بین 11 تا 20 تعامل سررسید نشده دارد', 2.22, -20, 11, 20)
    rule.save()

    # 21 <= NumNotDueDeal ≤ 30	-30	H1010N30	کاربر بین 21 تا 30 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1010N30', 'کاربر بین 21 تا 30 تعامل سررسید نشده دارد', 3.33, -30, 21, 30)
    rule.save()

    # NotDueDeal >= 31	-50	H1011N50	کاربر بیش از 30 تعامل سررسید نشده دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H10', 'H1011N50', 'کاربر بیش از 30 تعامل سررسید نشده دارد', 5.56, -50, 31, 999)
    rule.save()
    print('Histories(H) undone_undue_trades_counts_h10 rules are created.')


def import_rules_history_loans_total_count_h11():
    # define History(H)' rules of undone_undue_trades_counts master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'H', 'H11', 'تعداد کل تسهیلات بانکی در جریان', 2.22, 20)
    rule.save()

    # define History(H)' rules of undone_undue_trades_counts details: level 3
    # Loans = 0	00	H1101P0	کاربر هیچگونه تسهیلات در جریان ندارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H11', 'H1101P0', 'کاربر هیچگونه تسهیلات در جریان ندارد', 0, 0, 0, 0)
    rule.save()

    # Loans = 1	20	H1102P20	کاربر ۱ تسهیلات در جریان دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H11', 'H1102P20', 'کاربر ۱ تسهیلات در جریان دارد', 2.22, 20, 1, 1)
    rule.save()

    # Loans = 2	10	H1103P10	کاربر ۲ تسهیلات در جریان دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H11', 'H1103P10', 'کاربر ۲ تسهیلات در جریان دارد', 1.11, 10, 2, 2)
    rule.save()

    # Loans = 3	01	H1104P1	کاربر ۳ تسهیلات در جریان دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H11', 'H1104P1', 'کاربر ۳ تسهیلات در جریان دارد', 0.11, 1, 3, 3)
    rule.save()

    # Loans = 4	-20	H1105N20	کاربر ۴ تسهیلات در جریان دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H11', 'H1105N20', 'کاربر ۴ تسهیلات در جریان دارد', 2.22, -20, 4, 4)
    rule.save()

    # Loans = 5	-30	H1106N30	کاربر ۵ تسهیلات در جریان دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H11', 'H1106N30', 'کاربر ۵ تسهیلات در جریان دارد', 3.33, -30, 5, 5)
    rule.save()

    # Loans >= 6	-50	H1107N50	کاربر بیش از ۵ تسهیلات در جریان دارد
    rule = Rule()
    rule = create_new_rule(rule, 3, 'H11', 'H1107N50', 'کاربر بیش از ۵ تسهیلات در جریان دارد', 5.56, -50, 6, rules_max_val)
    rule.save()
    print('Histories(H) loans_total_count_h11 rules are created.')


def import_rules_histories():
    program.launch_app()
    import_rule_history_master()
    import_rules_history_membership_days_counts_h5()
    import_rules_history_done_timely_trades_of_last_3_months_h6()
    import_rules_history_done_timely_trades_between_last_3_to_12_months_h7()
    import_rules_history_recommended_to_others_counts_h8()
    import_rules_history_star_counts_avgs_h9()
    import_rules_history_undone_undue_trades_counts_h10()
    import_rules_history_loans_total_count_h11()
