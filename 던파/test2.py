loan = 500000000
interest_rate = 0.044 / 12
payment = 5000000
month = 0
total_interest = 0

while loan > 0:
    interest = loan * interest_rate
    total_interest += interest
    repayment = payment - interest
    loan -= repayment
    month += 1

print(month)
print(total_interest)


loan = 500000000
interest_rate = 0.044 / 12
extra_payment = 2000000
total_interest = 0
month = 0

# 원금 상환액 계산
principal_payment = loan / (30 * 12) + extra_payment 

while loan > 0:
    # 이자 계산
    interest = loan * interest_rate
    total_interest += interest
    # 매달 상환액
    principal_payment = min(principal_payment, loan)
    monthly_payment = principal_payment + interest
    print(f'Month {month+1}: {monthly_payment}')
    # 원금 상환
    loan -= principal_payment
    month += 1

print(f'Total interest paid: {total_interest}')
print(f'Total months: {month}')