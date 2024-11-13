grades = [35,67,98,100,100]
total = 0
num_of_grades = len(grades)
for grade in grades:
    total = grade+total
print("The average is",total/num_of_grades)