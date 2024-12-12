income = float(input("enter your monthly income: "))
expenses = float(input("enter your total monthly expenses: "))
monthly_savings = income - expenses
annual_interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print(f"your monthly_savings are $f{monthly_savings}")
print(f"projected savings after one year, with interest, is: ${projected_savings}")
