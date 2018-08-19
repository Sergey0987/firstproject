N = int(input())
list_of_numbers = []
list_of_numbers2 = []

for i in range(2, N+1):
    list_of_numbers.append(i)

p = list_of_numbers[0]
index = 0

while p**2 <= N: 

    for i in range(index+p, len(list_of_numbers), p):
        list_of_numbers[i] = False

    index = index + 1

    while list_of_numbers[index] == False:
        index = index + 1

    p = list_of_numbers[index]

for i in range(len(list_of_numbers)):
    if list_of_numbers[i] != False:
        list_of_numbers2.append(list_of_numbers[i])
               
    

print(list_of_numbers2)
