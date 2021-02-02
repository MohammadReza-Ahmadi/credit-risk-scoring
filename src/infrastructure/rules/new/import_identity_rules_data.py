from mongoengine.queryset.visitor import Q

from data.rules import Rule
from service.util import create_new_rule
from src import program
from src.infrastructure.scoring_enums import ProfileMilitaryServiceStatusEnum


def import_rule_identity_master():
    # Delete all histories(H) rules
    l2_rules: [Rule] = Rule.objects(Q(parent='I'))
    for r in l2_rules:
        l3_rules: [Rule] = Rule.objects(Q(parent=r.code))
        l3_rules.delete()
    l2_rules.delete()
    l1_rule = Rule.objects(Q(code='I'))
    l1_rule.delete()
    print('Identities(I) rules are deleted.')
    # define Identities(I)' rules master: level 1
    rule = Rule()
    rule = create_new_rule(rule, 1, None, 'I', 'اطلاعات هویتی', 10, 100)
    rule.save()
    print('Identities(I) master rule is created.')


def import_rules_identity_has_kycs_i1():
    # define Identities(I)' rules of kycs master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'I', 'I1', 'احراز هویت', 4)
    rule.save()

    # define Identities(I)' rules of kycs details: level 3
    # KYC = Yes	40	I0101P40    %4	احراز هویت نهایی از طریق استعلام ثبت احوال
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I1', 'I0101P40', 'احراز هویت نهایی از طریق استعلام ثبت احوال', 4, 40, 1)
    rule.save()

    # KYC = No	00	I0102P0 0%	عدم احراز هویت
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I1', 'I0102P0', 'عدم احراز هویت', 0, 0, 0)
    rule.save()
    print('Identities(I) has_kycs_i1 rules are created.')


def import_rules_identity_military_service_status_i2():
    # define Identities(I)' rules of military_service master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'I', 'I2', 'خدمت وظیفه عمومی', 2)
    rule.save()

    # define Identities(I)' rules of military_service details: level 3
    # MilServiceFinished/Exempted/Ongoing	20  2%	I0201P20	پایان خدمت
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I2', 'I0201P20', 'پایان خدمت', 2, 20, ProfileMilitaryServiceStatusEnum.FINISHED.value)
    rule.save()

    # MilServiceFinished/Exempted/Ongoing	20  2%	I0202P20	 معافیت
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I2', 'I0202P20', 'معافیت', 2, 20, ProfileMilitaryServiceStatusEnum.EXEMPTED.value)
    rule.save()

    # MilServiceFinished/Exempted/Ongoing	20  2%	I0203P20	در حال خدمت
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I2', 'I0203P20', 'در حال خدمت', 2, 20, ProfileMilitaryServiceStatusEnum.ONGOING.value)
    rule.save()

    # MilServiceSubjected	00	I0204P0     0%	مشمول غیر غایب
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I2', 'I0204P0', 'مشمول غیر غایب', 2, 20, ProfileMilitaryServiceStatusEnum.SUBJECTED.value)
    rule.save(rule)

    # MilServiceAbsent	-50	I0205N50        -5% 	غایب
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I2', 'I0205N50', 'غایب', 5, -50, ProfileMilitaryServiceStatusEnum.ABSENT.value)
    rule.save(rule)
    print('Identities(I) military_service_status_i2 rules are created.')


def import_rules_identity_sim_card_ownerships_i3():
    # define Identities(I)' rules of sim_care_ownership master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'I', 'I3', 'مالکیت خط تلفن همراه', 2)
    rule.save()

    # define Identities(I)' rules of sim_care_ownership details: level 3
    # SimCardOwnership = Yes	20	I0301P20    2%	تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه در سامانه شاهکار
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I3', 'I0301P20', 'تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه در سامانه شاهکار', 2, 20, 1)
    rule.save(rule)

    # SimCardOwnership = No	00	I0302P0     0%	عدم تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I3', 'I0302P0', 'عدم تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه', 0, 0, 0)
    rule.save(rule)
    print('Identities(I) sim_card_ownerships_i3 rules are created.')


def import_rules_identity_address_verifications_i4():
    # define Identities(I)' rules of address_verifications master: level 2
    rule = Rule()
    rule = create_new_rule(rule, 2, 'I', 'I4', 'احراز اصالت محل سکونت', 2)
    rule.save()

    # define Identities(I)' rules of address_verifications details: level 3
    # AddressVerification = Yes	20	I0401P20    2%	احراز اصالت نشانی محل سکونت کاربر از طریق وارد کردن رمز پستی
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I4', 'I0401P20', 'احراز اصالت نشانی محل سکونت کاربر از طریق وارد کردن رمز پستی', 2, 20, 1)
    rule.save()

    # AddressVerification = No	00	I0402P0 0%	عدم احراز اصالت نشانی محل سکونت کاربر
    rule = Rule()
    rule = create_new_rule(rule, 3, 'I4', 'I0402P0', 'تطابق هویت واقعی کاربر با مشخصات مالک خط تلفن همراه در سامانه شاهکار', 0, 0, 0)
    rule.save(rule)
    print('Identities(I) address_verifications_i4 rules are created.')


def import_rules_identities():
    program.launch_app()
    import_rule_identity_master()
    import_rules_identity_has_kycs_i1()
    import_rules_identity_military_service_status_i2()
    import_rules_identity_sim_card_ownerships_i3()
    import_rules_identity_address_verifications_i4()
