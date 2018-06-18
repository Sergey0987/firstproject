def mirror(arr):
    print(id(arr))
    mirroredPart = arr[:]
    mirroredPart.reverse()
    for i in mirroredPart:
        arr.append(i)
    print(arr, id(arr))


#Ошибка метод reverse() изменяет сам список. Сначала создать новый список полным срезом, затем его обратить и после этого сложить. Создастся новый список. Либо 
mirror([1,2,3,4,5])
