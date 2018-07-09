def average(values):
    summ = 0
    if len(values) == 0:
        return 0
    else:
        for i in values:
           summ = summ + i
        aver_value = summ / len(values)
        return aver_value

print(average([1,2,3,4,5,6,7]))
print(average([]))
