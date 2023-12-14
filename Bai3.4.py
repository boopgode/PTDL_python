with open("clean_data1.csv", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]
students.pop()

total_student = len(students)

header = header.split(",")
subjects = header[5:]
for i in range(len(students)):
	students[i] = students[i].split(",")

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]
for s in students:
	for i in range(5,16):
		if s[i] == "-1":
			not_take_exam[i-5] += 1 #số người bỏ thi hoặc không đăng ký thi	

not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,11):
	not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student, 2)
	
import matplotlib.pyplot as plt
import numpy 
figure, axis = plt.subplots()
y_pos = numpy.arange(len(subjects))
plt.bar(y_pos, not_take_exam_percentage)
plt.xticks(y_pos,subjects)
axis.set_ylim(0,100)
plt.ylabel('Phần trăm')
plt.title('Số học sinh bỏ thi hoặc không đăng kí')
rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')
plt.show()