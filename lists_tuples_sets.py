#lists are mutable[]
#tuples are not mutable()
#sets have no duplicates and are mutable and the order is not guaranteed.
#we can get the elements in lists and tuples with subscript notation,
#that is list[0],tuple[0] but not with sets.
#reassignment is possible only with lists.
#tuple attribute has no append() because tuples are immutable.
#we can remove elements from list-remove()
#add works with sets not ammend()
#because ammend adds the element at the end but sets dont have specific order
#list is the most standard collection wherre we can modify elements.
my_set = {"family","work"}
my_set.add("Love")
print(my_set)
my_tuple = ("family","work","Love")
print(my_tuple[0])
my_list = ["family","work","Love"]
my_list.append("laugh")
print(my_list)
#my_list.add("Life") List object has no attribute "add()"
