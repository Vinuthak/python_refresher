numbers = [1,2,3,4,5]
doubled = [x*2 for x in numbers]
print(doubled)
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
friends = ["Alex", "Romano","Sophia","Sarah","Star"]
friends_s = [s for s in friends if s.startswith('S')]
print(friends_s)