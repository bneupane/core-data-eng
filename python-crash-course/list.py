list_of_age = [15, 16, 16, 26, 10]
# print (list_of_age[0:3])
# print (list_of_age[::-1])

# sorted(list_of_age)

list_of_age.sort()
print(list_of_age)

list_of_age.sort(reverse=True)
print(list_of_age)

list_of_age.append(54)
print(list_of_age)

list_of_age.remove(16)
print(list_of_age)

del list_of_age[0]
print(list_of_age)