# read file
with open("clean_data1.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

# split header/ tách tiêu đề
header = header.split(",")
subjects = header[5:]

# turn each student to a list/chuyển từng học sinh vào một danh sách
for i in range(len(students)):
	students[i] = students[i].split(",")

# remove empty list (end of file)/xóa danh sách trống (cuối tệp)
students.pop()

# number of students who took 0,1,2,3,... subjects/số học sinh thi 0,1,2,3, ... môn
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]
average = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	total = 0
	for i in range(11):
		if s[i+5] != "-1":
			total += float(s[i+5])
			count += 1

	num_of_exam_taken[count] += 1
	average[count] += total/count

for i in range(12):
	if num_of_exam_taken[i] != 0:
		average[i] = round(average[i]/num_of_exam_taken[i], 2)

print("num of exam taken",num_of_exam_taken)
print("average",average)

# https://matplotlib.org/3.1.0/gallery/ticks_and_spines/custom_ticker1.html#sphx-glr-gallery-ticks-and-spines-custom-ticker1-py
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.arange(12)
print("x: ",x)

fig, axis = plt.subplots()
plt.bar(x, average)

# set limit/đặt giới hạn
axis.set_ylim(0,10)

# label for column x
plt.xticks(x, y)

axis.set_ylabel('Điểm Trung Bình')
axis.set_xlabel('Số môn thi')

rects = axis.patches

# Make some labels./Tạo một số nhãn.
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
labels = average
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height, label,ha='center', va='bottom')

plt.title('Điểm trung bình theo số lượng môn thi')
	
plt.show()