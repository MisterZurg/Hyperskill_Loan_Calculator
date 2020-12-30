# Stage 1
# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'

# def print_repaid():
#    print(f"{loan_principal}\n"
#          f"{first_month}\n"
#          f"{second_month}\n"
#          f"{third_month}\n"
#          f"{final_output}\n")

# Stage 2/4: Dreamworld
import math


def users_input_stage_2():
    loan_principal = int(input("Enter the loan principal:\n"))
    next_step = input("What do you want to calculate?\n"
                      "type \"m\" - for number of monthly payments,\n" \
                      "type \"p\" - for the monthly payment:")
    if next_step == "m":
        monthly_payment = int(input("Enter the monthly payment:\n"))
        calculate_number_of_monthly_payments_stage2(loan_principal, monthly_payment)
    elif next_step == "p":
        number_of_months = int(input("Enter the number of months:\n"))
        calculate_monthly_payment_stage2(loan_principal, number_of_months)
    else:
        print("I don't have a clue what are you talking about :/")


def calculate_number_of_monthly_payments_stage2(principal, payment):
    months_cnt = math.ceil(principal / payment)
    if months_cnt % 10 == 1:
        print(f"It will take {months_cnt} month to repay the loan")
    else:
        print(f"It will take {months_cnt} months to repay the loan")


def calculate_monthly_payment_stage2(principal, months):
    monthly_payment = math.ceil(principal / months)
    if monthly_payment == principal / months:
        print(f"Your monthly payment = {monthly_payment}")
    else:
        last_payment = principal - (months - 1) * monthly_payment
        print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}.")


# users_input_stage_2()

# Stage 3/4: Annuity payment
# Ну начинается: слив досрочного профильного ЕГЭ 2020
def users_input_stage_3():
    next_step = input("What do you want to calculate?\n"
                      "type \"n\" for number of monthly payments,\n"
                      "type \"a\" for annuity monthly payment amount,\n"
                      "type \"p\" for loan principal:")
    if next_step == "n":
        number_of_monthly_payments()
    elif next_step == "a":
        annuity_monthly_payment_amount()
    elif next_step == "p":
        loan_principal_rate()
    else:
        print("Помощь -> Выход -> Выход АВАРИЙНЫЙ!")


def number_of_monthly_payments():
    # Как ни странно ввод параметров
    loan_principal = int(input("Enter the loan principal:\n"))
    monthly_payment = int(input("Enter the monthly payment:\n"))
    loan_interest = float(input("Enter the loan interest:\n"))

    i = loan_interest / (12 * 100)
    argument = (monthly_payment / (monthly_payment - i * loan_principal))
    base = 1 + i
    n = math.log(argument, base)
    n = math.ceil(n)  # Округляем в большую сторну // X months
    years = n // 12
    months = n % 12
    if years != 0 and months != 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years != 0 and months == 0:
        print(f"It will take {years} years to repay this loan!")
    elif years == 0 and months != 0:
        print(f"It will take {months} months to repay this loan!")
    else:
        print(f"I don't have a clue how long it will take to repay this loan :/")


def annuity_monthly_payment_amount():
    loan_principal = int(input("Enter the loan principal:\n"))
    number_of_periods = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n"))

    i = loan_interest / (12 * 100)
    a = loan_principal * (i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1)
    print(f"Your monthly payment = {math.ceil(a)}!")


def loan_principal_rate():
    annuity_payment = float(input("Enter the annuity payment:\n"))
    number_of_periods = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n"))

    i = loan_interest / (12 * 100)
    dividend = i * (1 + i) ** number_of_periods
    divisor = ((1 + i) ** number_of_periods) - 1
    p = annuity_payment // (dividend / divisor)
    print(f"Your loan principal = {p}!")


# users_input_stage_3()

# Stage 4/4: Differentiate payment
import argparse


def diff(principal, n, interest):
    overpayment = 0
    interest /= 12 * 100
    for month in range(1, n + 1):
        D = (principal / n) + interest * (principal - (principal * (month - 1) / n))
        overpayment += math.ceil(D)
        print(f"Month {month}: payment is {math.ceil(D)}")
    print(f"\nOverpayment = {overpayment - principal}")


def annuity_repay_time(loan_principal, monthly_payment, loan_interest):
    i = loan_interest / (12 * 100)
    argument = (monthly_payment / (monthly_payment - i * loan_principal))
    base = 1 + i
    n = math.log(argument, base)
    n = math.ceil(n)  # Округляем в большую сторну // X months
    years = n // 12
    months = n % 12
    if years != 0 and months != 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years != 0 and months == 0:
        print(f"It will take {years} years to repay this loan!")
    elif years == 0 and months != 0:
        print(f"It will take {months} months to repay this loan!")
    else:
        print(f"I don't have a clue how long it will take to repay this loan :/")
    print(f"Overpayment = {monthly_payment * n - loan_principal}")


def annuity_monthly_payment(loan_principal, number_of_periods, loan_interest):
    i = loan_interest / (12 * 100)
    a = loan_principal * (i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1)
    print(f"Your monthly payment = {math.ceil(a)}!\n"
          f"Overpayment = {math.ceil(a) * number_of_periods - loan_principal}")


def annuity_loan_principal(annuity_payment, number_of_periods, loan_interest):
    i = loan_interest / (12 * 100)
    dividend = i * (1 + i) ** number_of_periods
    divisor = ((1 + i) ** number_of_periods) - 1
    p = annuity_payment // (dividend / divisor)
    print(f"Your loan principal = {p}!\n"
          f"Overpayment = {annuity_payment * number_of_periods - p}")


# object which will store all the information about the arguments
parser = argparse.ArgumentParser(description="This program is kinda \
                                pretty much 17-th task from \"EGE\".")

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

# Check arguments
if args.type is None:
    print("Incorrect parameters")
elif args.interest is None or float(args.interest) < 0:  # args.principal is None and
    print("Incorrect parameters")
elif args.type == "diff":
    if args.principal is None or args.periods is None \
            or float(args.principal) < 0 or int(args.periods is None):
        print("Incorrect parameters")
    else:
        diff(int(args.principal), int(args.periods), float(args.interest))
elif args.type == "annuity":
    if args.principal is not None and args.payment is not None and args.interest is not None \
            and 0 < float(args.principal) and 0 < int(args.payment) and 0 < float(args.interest) \
            and args.periods is None:
        annuity_repay_time(int(args.principal), int(args.payment), float(args.interest))
    elif args.principal is not None and args.periods is not None and args.interest is not None \
            and 0 < float(args.principal) and 0 < int(args.periods) and 0 < float(args.interest) \
            and args.payment is None:
        annuity_monthly_payment(int(args.principal), int(args.periods), float(args.interest))
    elif args.payment is not None and args.periods is not None and args.interest is not None \
            and 0 < int(args.payment) and 0 < int(args.periods) and 0 < float(args.interest) \
            and args.principal is None:
        annuity_loan_principal(int(args.payment), int(args.periods), float(args.interest))
    else:
        print("Incorrect parameters")
else:
    print("I cannot calculate mixed payments")

# Examples
# python creditcalc.py --type=diff       --principal=500000      --periods=8 --interest=7.8
# Month 1: payment is 65750
# Month 2: payment is 65344
# Month 3: payment is 64938
# Month 4: payment is 64532
# Month 5: payment is 64125
# Month 6: payment is 63719
# Month 7: payment is 63313
# Month 8: payment is 62907
#
# Overpayment = 14628
# python creditcalc.py --type=diff       --principal=1000000     --periods=10 --interest=10
# Month 1: payment is 108334
# Month 2: payment is 107500
# Month 3: payment is 106667
# Month 4: payment is 105834
# Month 5: payment is 105000
# Month 6: payment is 104167
# Month 7: payment is 103334
# Month 8: payment is 102500
# Month 9: payment is 101667
# Month 10: payment is 100834
#
# Overpayment = 45837
# python creditcalc.py --type=annuity    --principal=1000000     --periods=60 --interest=10
# Your annuity payment = 21248!
# Overpayment = 274880
# python creditcalc.py --type=annuity    --principal=500000      --payment=23000 --interest=7.8
# It will take 2 years to repay this loan!
# Overpayment = 52000
