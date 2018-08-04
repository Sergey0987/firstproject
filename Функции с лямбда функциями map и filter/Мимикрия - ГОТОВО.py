#Надо написать для transformation такое лябда выражение, чтобы
#transformed_values получилась копией values

transformation = lambda x: x

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(transformation, values))

print(transformed_values)
