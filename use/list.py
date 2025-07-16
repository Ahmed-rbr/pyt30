
# 1. .append() - Adds item to the end of the list
print("1. append()")
my_list = [1, 2, 3]
my_list.append(4)
print("After append:", my_list)  # [1, 2, 3, 4]
print()

# 2. .insert() - Adds item at specific index
print("2. insert()")
my_list = [1, 2, 3]
my_list.insert(1, 100)
print("After insert:", my_list)  # [1, 100, 2, 3]
print()

# 3. .remove() - Removes first match of item
print("3. remove()")
my_list = [1, 2, 3, 2]
my_list.remove(2)
print("After remove:", my_list)  # [1, 3, 2]
print()

# 4. .pop() - Removes item at index (default last)
print("4. pop()")
my_list = [10, 20, 30, 40]
popped = my_list.pop()
print("Popped:", popped)         # 40
print("After pop:", my_list)     # [10, 20, 30]

popped_at_index = my_list.pop(1)
print("Popped at index 1:", popped_at_index)  # 20
print("After second pop:", my_list)           # [10, 30]
print()

# 5. .sort() - Sorts the list
print("5. sort()")
my_list = [3, 1, 4, 2]
my_list.sort()
print("Sorted list:", my_list)   # [1, 2, 3, 4]
print()

# 6. .reverse() - Reverses the list
print("6. reverse()")
my_list = [1, 2, 3, 4]
my_list.reverse()
print("Reversed list:", my_list)  # [4, 3, 2, 1]
print()

# 7. .clear() - Removes all items
print("7. clear()")
my_list = [10, 20, 30]
my_list.clear()
print("After clear:", my_list)   # []
