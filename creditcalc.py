import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="the type of operation")
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)
args = parser.parse_args()


def diff(principal, periods, interest):
    i = float((interest / 100) / 12)
    payment_sum = 0
    month = 1
    while month < periods + 1:
        payment = float(principal / periods + i * (principal - (principal * (month - 1)) / periods))
        print(f"Month {month}: payment is {math.ceil(payment)}")
        payment_sum += math.ceil(payment)
        month += 1
    print()
    print(f"Overpayment = {payment_sum - principal}")


def annuity_payment(principal, periods, interest):
    i = float((interest / 100) / 12)
    payment = principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    print(f"Your annuity payment = {math.ceil(payment)}!")
    print(f"Overpayment = {math.ceil(payment) * periods - principal}")


def annuity_period(principal, payment, interest):
    i = (interest / 100) / 12
    months = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    payment_sum = payment * months
    years = 0
    while months >= 12:
        years += 1
        months -= 12
    if years != 0 and months != 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years == 0 and months != 0:
        print(f"It will take {months} months to repay this loan!")
    elif years != 0 and months == 0:
        print(f"It will take {years} years to repay this loan!")
    print(f"Overpayment = {payment_sum - principal}")


def annuity_principal(payment, periods, interest):
    i = (interest / 100) / 12
    principal = payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    print(f"Your loan principal = {int(principal)}!")
    print(f"Overpayment = {math.ceil(payment) * periods - principal}")


if args.type == "annuity":
    if args.principal and args.periods and args.interest:
        annuity_payment(args.principal, args.periods, args.interest)
    elif args.principal and args.payment and args.interest:
        annuity_period(args.principal, args.payment, args.interest)
    elif args.payment and args.periods and args.interest:
        annuity_principal(args.payment, args.periods, args.interest)
    else:
        print("Incorrect parameters.")
elif args.type == "diff":
    if args.principal and args.periods and args.interest:
        diff(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")