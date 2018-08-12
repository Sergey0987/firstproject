def same_by(characteristic, objects):

    if len(objects) == 0:
        return True
    else:
        from functools import reduce

        verify = list(map(characteristic, objects)) # получение списка значений, после приминения к исходному списку функции 
#        print(verify)

        list_of_average_numbers = int((reduce(lambda x,y: x + y, verify)) / len(verify)) # список со средними значениями для сравнения со значениями в списке verify
#        print(list_of_average_numbers)

        list2 = list(filter(lambda x: x!= list_of_average_numbers, verify))

        if len(list2) > 0:
            return False
        else:
            return True
    

a = same_by(lambda x: x%2, [0, 2, 10, 6])
print(a)

a = same_by(lambda x: x%2, [1, 7, -3])
print(a)

a = same_by(lambda x: x%2, [])
print(a)

a = same_by(lambda x: x%2, [1, 2, 3, 4])
print(a)

a = same_by(len, ['test', 'wave', 'lazy'])
print(a)

a = same_by(len, ['cloud', 'job', 'bicycle'])
print(a)
