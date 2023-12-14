import subprocess

start =1000001
end =2900704

file = open("raw_data12.txt", "w")

for sbd in range(start,end):
	command = 'curl -F "SoBaoDanh=0' + str(sbd) + '" diemthi.hcm.edu.vn/Home/Show'
	result = subprocess.check_output(command)

	file.write(str(result) + "\n")

	
# mỗi dòng mất 1s