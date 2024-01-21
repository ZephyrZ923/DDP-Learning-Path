numbers = range(0,10,2)

list1 = list(numbers)
print(list1)


numbers1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced = numbers1[2:5]
print(sliced)  # Output: [2, 3, 4]
first_two = numbers1[:2]
last_two = numbers1[-2:]
print(first_two)
print(last_two)



every_three = numbers1[::3]
print(every_three)

numbers3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_numbers = numbers3[::-2]
print(reversed_numbers)  


original_list = [1, 2, 3]
copy_list1 = original_list.copy()
copy_list2 = original_list[:]
copy_list3 = list(original_list)
print(original_list,copy_list1,
      copy_list2,copy_list3)
