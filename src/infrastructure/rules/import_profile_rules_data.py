from data.rule.profile.rules_profile_address_verifications import RuleProfileAddressVerification
from data.rule.profile.rules_profile_has_kycs import RuleProfileHasKyc
from data.rule.profile.rules_profile_membership_days_counts import RuleProfileMembershipDaysCount
from data.rule.profile.rules_profile_military_service_status import RuleProfileMilitaryServiceStatus
from data.rule.profile.rules_profile_recommended_to_others_counts import RuleProfileRecommendedToOthersCount
from data.rule.profile.rules_profile_sim_card_ownerships import RuleProfileSimCardOwnership
from data.rule.profile.rules_profile_star_counts_avgs import RuleProfileStarCountAvg
from infrastructure.constants import rules_max_val
from service.util import create_rule_by_status_code, create_rule
from src import program
from src.infrastructure.scoring_enums import ProfileMilitaryServiceStatusEnum


def import_rules_profile_has_kycs_i0():
    # KYC = Yes	40	I0101P40    %4	احراز هویت نهایی از طریق استعلام ثبت احوال
    rule = RuleProfileHasKyc()
    rule.drop_collection()
    rule.save(create_rule_by_status_code(rule, 'I0101P40', 1, 40, 0.04, 'احراز هویت نهایی از طریق استعلام ثبت احوال'))

    # KYC = No	00	I0102P0 0%	عدم احراز هویت
    rule = RuleProfileHasKyc()
    rule.save(create_rule_by_status_code(rule, 'I0102P0', 0, 0, 0, 'عدم احراز هویت'))


def import_rules_profile_military_service_status_i0():
    # MilServiceFinished/Exempted/Ongoing	20  2%	I0201P20	پایان خدمت
    rule = RuleProfileMilitaryServiceStatus()
    rule.drop_collection()
    rule.save(create_rule_by_status_code(rule, 'I0201P20', ProfileMilitaryServiceStatusEnum.FINISHED.value, 20, 0.02, 'پایان خدمت'))

    # MilServiceFinished/Exempted/Ongoing	20  2%	I0202P20	 معافیت
    rule = RuleProfileMilitaryServiceStatus()
    rule.save(create_rule_by_status_code(rule, 'I0202P20', ProfileMilitaryServiceStatusEnum.EXEMPTED.value, 20, 0.02, 'معافیت'))

    # MilServiceFinished/Exempted/Ongoing	20  2%	I0203P20	در حال خدمت
    rule = RuleProfileMilitaryServiceStatus()
    rule.save(create_rule_by_status_code(rule, 'I0203P20', ProfileMilitaryServiceStatusEnum.ONGOING.value, 20, 0.02, 'در حال خدمت'))

    # MilServiceSubjected	00	I0204P0     0%	مشمول غیر غایب
    rule = RuleProfileMilitaryServiceStatus()
    rule.save(create_rule_by_status_code(rule, 'I0204P0', ProfileMilitaryServiceStatusEnum.SUBJECTED.value, 0, 0, 'مشمول غیر غایب'))

    # MilServiceAbsent	-50	I0205N50        -5% 	غایب
    rule = RuleProfileMilitaryServiceStatus()
    rule.save(create_rule_by_status_code(rule, 'I0205N50', ProfileMilitaryServiceStatusEnum.ABSENT.value, -50, -0.05, 'غایب'))


def import_rules_profile_sim_card_ownerships_i0():
    # SimCardOwnership = Yes	20	I0301P20    2%	تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه در سامانه شاهکار
    rule = RuleProfileSimCardOwnership()
    rule.drop_collection()
    rule.save(create_rule_by_status_code(rule, 'I0301P20', 1, 20, 0.02, 'تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه در سامانه شاهکار'))

    # SimCardOwnership = No	00	I0302P0     0%	عدم تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه
    rule = RuleProfileSimCardOwnership()
    rule.save(create_rule_by_status_code(rule, 'I0302P0', 0, 0, 0, 'عدم تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه'))


def import_rules_profile_address_verifications_i0():
    # AddressVerification = Yes	20	I0401P20    2%	احراز اصالت نشانی محل سکونت کاربر از طریق وارد کردن رمز پستی
    rule = RuleProfileAddressVerification()
    rule.drop_collection()
    rule.save(create_rule_by_status_code(rule, 'I0401P20', 1, 20, 0.02, 'احراز اصالت نشانی محل سکونت کاربر از طریق وارد کردن رمز پستی'))

    # AddressVerification = No	00	I0402P0 0%	عدم احراز اصالت نشانی محل سکونت کاربر
    rule = RuleProfileAddressVerification()
    rule.save(create_rule_by_status_code(rule, 'I0402P0', 0, 0, 0, 'عدم احراز اصالت نشانی محل سکونت کاربر'))


def import_rules_profile_membership_days_counts_h5():
    # Just Registered MembershipDaysWithAtleast1SD == 0 	00	H0501P0	عضو جدید
    rule = RuleProfileMembershipDaysCount()
    rule.drop_collection()
    rule.save(create_rule(rule, 'H0501P0', 0, 0, 0, 'عضو جدید'))

    #  1 <=  MembershipDaysWithAtleast1SD ≤ 90	    10	H0502P10	 عضویت بین 1 تا 90 روز
    rule = RuleProfileMembershipDaysCount()
    rule.save(create_rule(rule, 'H0502P10', 1, 90, 10, ' عضویت بین 1 تا 90 روز'))

    # 91 <=  MembershipDaysWithAtleast3SD ≤ 180	    20	H0503P20	 عضویت بین 91 تا 180 روز
    rule = RuleProfileMembershipDaysCount()
    rule.save(create_rule(rule, 'H0503P20', 91, 180, 20, ' عضویت بین 91 تا 180 روز'))

    # 181 <=  MembershipDaysWithAtleast5SD ≤ 365	30	H0504P30	 عضویت بین 181 تا 365 روز
    rule = RuleProfileMembershipDaysCount()
    rule.save(create_rule(rule, 'H0504P30', 181, 365, 30, ' عضویت بین 181 تا 365 روز'))

    # 366 <= MembershipDaysWithAtleast10SD ≤ 720	40	H0505P40	 عضویت بین 366 تا 720 روز
    rule = RuleProfileMembershipDaysCount()
    rule.save(create_rule(rule, 'H0505P40', 366, 720, 40, ' عضویت بین 366 تا 720 روز'))

    # 721 <= MembershipDaysWithAtleast15SD ≤ 1080	50	H0506P50	 عضویت بین 721 تا 1080 روز
    rule = RuleProfileMembershipDaysCount()
    rule.save(create_rule(rule, 'H0506P50', 721, 1080, 50, ' عضویت بین 721 تا 1080 روز'))

    #     MembershipDaysWithAtleast20SD >= 1081	    60	H0507P60	 عضویت بیش از 1081 روز
    rule = RuleProfileMembershipDaysCount()
    rule.save(create_rule(rule, 'H0507P60', 1081, rules_max_val, 60, ' عضویت بیش از 1081 روز'))


def import_rules_profile_recommended_to_others_counts_h8():
    # Recommendation = 0	00	H0801P0	کاربر توسط کسی پیشنهاد نشده است
    rule = RuleProfileRecommendedToOthersCount()
    rule.drop_collection()
    rule.save(create_rule(rule, 'H0801P0', 0, 0, 0, 'کاربر توسط کسی پیشنهاد نشده است'))

    # Recommendation = 1	10	H0802P10	پیشنهاد شده توسط 1 نفر
    rule = RuleProfileRecommendedToOthersCount()
    rule.save(create_rule(rule, 'H0802P10', 1, 1, 10, 'پیشنهاد شده توسط 1 نفر'))

    # 2 < Recommendation ≤ 3	20	H0803P20	پیشنهاد شده توسط 2 تا 3 نفر
    rule = RuleProfileRecommendedToOthersCount()
    rule.save(create_rule(rule, 'H0803P20', 2, 3, 20, 'پیشنهاد شده توسط 2 تا 3 نفر'))

    # 4 < Recommendation ≤ 10	30	H0804P30	پیشنهاد شده توسط 4 تا 10 نفر
    rule = RuleProfileRecommendedToOthersCount()
    rule.save(create_rule(rule, 'H0804P30', 4, 10, 30, 'پیشنهاد شده توسط 4 تا 10 نفر'))

    # 11 < Recommendation ≤ 30	40	H0805P40	پیشنهاد شده توسط 11 تا 30 نفر
    rule = RuleProfileRecommendedToOthersCount()
    rule.save(create_rule(rule, 'H0805P40', 11, 30, 40, 'پیشنهاد شده توسط 11 تا 30 نفر'))

    # Recommendation > 30	50	H0806P50	پیشنهاد شده توسط بیش از 30 نفر
    rule = RuleProfileRecommendedToOthersCount()
    rule.save(create_rule(rule, 'H0806P50', 30, rules_max_val, 50, 'پیشنهاد شده توسط بیش از 30 نفر'))


def import_rules_profile_star_counts_avgs_h9():
    # WeightedAveStars <= 1	00	H0901P0	کاربر به طور متوسط کمتر مساوی ۱ ستاره کسب کرده است
    rule = RuleProfileStarCountAvg()
    rule.drop_collection()
    rule.save(create_rule(rule, 'H0901P0', 0, 1, 0, 'کاربر به طور متوسط کمتر مساوی ۱ ستاره کسب کرده است'))

    # 1.001 <= WeightedAveStars ≤ 2	05	H0902P5	کاربر به طور متوسط بیش از ۱ و کمتر مساوی ۲ ستاره کسب کرده است
    rule = RuleProfileStarCountAvg()
    rule.save(create_rule(rule, 'H0902P5', 1.001, 2, 5, 'کاربر به طور متوسط بیش از ۱ و کمتر مساوی ۲ ستاره کسب کرده است'))

    # 2.001 <= WeightedAveStars ≤ 3	10	H0903P10	کاربر به طور متوسط بیش از ۲ و کمتر مساوی ۳ ستاره کسب کرده است
    rule = RuleProfileStarCountAvg()
    rule.save(create_rule(rule, 'H0903P10', 2.001, 3, 10, 'کاربر به طور متوسط بیش از ۲ و کمتر مساوی ۳ ستاره کسب کرده است'))

    # 3.001 <= WeightedAveStars ≤ 4	30	H0904P30	کاربر به طور متوسط بیش از ۳ و کمتر مساوی ۴ ستاره کسب کرده است
    rule = RuleProfileStarCountAvg()
    rule.save(create_rule(rule, 'H0904P30', 3.001, 4, 30, 'کاربر به طور متوسط بیش از ۳ و کمتر مساوی ۴ ستاره کسب کرده است'))

    # 4.001 <= WeightedAveStars ≤ 5	50	H0905P50	کاربر به طور متوسط بیش از ۴ و کمتر مساوی ۵ ستاره کسب کرده است
    rule = RuleProfileStarCountAvg()
    rule.save(create_rule(rule, 'H0905P50', 4.001, 5, 50, 'کاربر به طور متوسط بیش از ۴ و کمتر مساوی ۵ ستاره کسب کرده است'))


if __name__ == '__main__':
    program.launch_app()
    import_rules_profile_address_verifications_i0()
    import_rules_profile_has_kycs_i0()
    import_rules_profile_military_service_status_i0()
    import_rules_profile_sim_card_ownerships_i0()
    import_rules_profile_membership_days_counts_h5()
    import_rules_profile_recommended_to_others_counts_h8()
    import_rules_profile_star_counts_avgs_h9()
