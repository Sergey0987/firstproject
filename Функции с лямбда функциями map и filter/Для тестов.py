income1 = [10,39,75]
income2 = [100,390,750]

def double_money(dollars1, dollars2):
    return dollars1 + dollars2


new_income = list(map(double_money, income1, income2))

print(new_income)
