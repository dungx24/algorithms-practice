import numpy as np 

#create a np array with elements from 1 to 20
arr = np.arange(start=1, stop=21, step=1)
print(arr)

#create an array with elements equal to square of each one in arr
arr_squared = arr**2
print(arr_squared)

#convert to farenheit for elements in arr_squared
arr_farenheit = arr_squared*1.8 + 32
print(arr_farenheit)

#use slicing
matrix = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60],
    [65, 70, 75, 80]
])
print(matrix[1,:])
print(matrix[:,2])
print(matrix[2:,2:])

#boolean masking
scores = np.array([55, 82, 95, 40, 71, 63, 99, 50, 88])
print(np.sum(scores >= 50))
passing_scores = scores[scores >= 50]
print(passing_scores)
failed_students = (scores < 50)
print(np.average(scores[failed_students]))

#Axis operation
grades = np.array([
    [80, 85, 88],  # Sinh viên 1
    [75, 90, 92],  # Sinh viên 2
    [90, 91, 89],  # Sinh viên 3
    [82, 78, 85]   # Sinh viên 4
])
print(np.average(grades, axis=0))
ave = np.average(grades, axis=1)
print(np.round(ave, 2))
for i in range(len(grades)):
	print(np.max(grades[i,:]))

#Normalization
data = np.array([10, 20, 30, 40, 50])
print(np.mean(data))
print(np.std(data)) #tính độ lệch chuẩn
print((data - np.mean(data))/np.std(data))












