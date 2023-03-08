has_high_income = True
good_credit = True

if has_high_income and good_credit:
    print('Eligible for loan')

money_at_hand = True
money_in_bank = False

if money_at_hand or money_in_bank:
    print('Eligible')

has_high_income = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
    print('Eligible for loan')