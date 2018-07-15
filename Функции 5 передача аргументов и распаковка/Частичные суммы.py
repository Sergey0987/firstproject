def partSums(*args):
    partSumsList = []
    nextPartSums = 0
    if len(partSumsList) == 0:
        partSumsList.append(0)
    for number in args:
            nextPartSums = nextPartSums + number
            partSumsList.append(nextPartSums)
    print(partSumsList)

partSums(1, 1/2, 1/4, 1/8, 1/16, 1/32)
partSums()
