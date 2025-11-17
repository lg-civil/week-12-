# # Objective:
# # Students will understand how to create, modify, and access elements in Python lists.

# # Topics Covered:
# # Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# collections are used to store multiples items in a single variable 
# lists are ordered ncollections of items
# lists are mutable, meaning you can change their content
# lists are created using [] brackets

lists_of_fruits = ["apple", "banana", "cherry", "date"]
print(lists_of_fruits)  # ['apple', "banana", "cherru", "date"]
print(type(lists_of_fruits))        # <class 'list'>

# Accessing items in a list
print(lists_of_fruits[0])
print(lists_of_fruits[1])
print(lists_of_fruits[-1])
print(lists_of_fruits[1:3])


# reversing
lists_of_fruits.reverse()
print(lists_of_fruits)
print(lists_of_fruits[ : : -1])

# appending items to a list
lists_of_fruits.append("elderberry") # add items to the end of the list
print(lists_of_fruits)
lists_of_fruits.extend(["dragon fruit", "mango"])  # add multiple items to the end of the list
print(lists_of_fruits)
# popping items from a list 
popped_item = lists_of_fruits.pop()
# removes and returns the last item
print(popped_item) # mango
print(lists_of_fruits)
# inserting items at a specific index
lists_of_fruits.insert(1, "blueberry")
print(lists_of_fruits)
#  removing a specific item by value
lists_of_fruits.remove("banana")
print(lists_of_fruits)
lists_of_fruits.insert(3, "banana")
lists_of_fruits.sort() 
# sorts the list in ascending order
print(lists_of_fruits)
# why use lists ? instead of individual variables
# imagine you have 100 things to manage
lists_of_items = list(range(1,101))
print(lists_of_items)
# create a list of numbers
lists_of_items  = list(range(1,1001))
print(lists_of_items)
print(len(lists_of_items))
lists_of_items = list(range(1,1000001))
print(lists_of_items)








# # Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.

# # Print the second and last item.

# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element.