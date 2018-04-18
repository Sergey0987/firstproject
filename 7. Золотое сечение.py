def goldenRatio(i):
    first_arg=0
    second_arg=1
    for j in range(i):
        first_arg,second_arg=second_arg,first_arg+second_arg
    print((first_arg+second_arg)/second_arg)


goldenRatio(4)

