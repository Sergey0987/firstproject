# [1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]

def takeLargeBanknotes(banknotes):
    numbers_for_print = []
    for i in banknotes:
        if i > 10:
            numbers_for_print.append(i)
    return numbers_for_print

print(takeLargeBanknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]))
