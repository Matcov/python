
student_heights = input("Input a list of student heights without commas ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_of_heights = 0
for height in student_heights:
    sum_of_heights += height
    #print (type (height))
    

count = 0
for height in student_heights:
    count += 1

average_height = (sum_of_heights / count)

print("Sum of student heights:", sum_of_heights)
print("Average student height:", average_height)

