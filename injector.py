import os, sys
import names
 
name_list = []

# generate name and check duplicate
def generate_name(gender):
	if gender == "female":
		while True:
			name = names.get_full_name(gender='female')
			print(name)
			if name not in name_list:
				name_list.append(name)
				break
	if gender == "male":
		while True:
			name = names.get_full_name(gender='male')
			print(name)
			if name not in name_list:
				name_list.append(name)
				break
	if gender == "universal":
		while True:
			name = names.get_full_name()
			print(name)
			if name not in name_list:
				name_list.append(name)
				break
	return name


# return False if there is no duplicate in the list
def duplicate_exists_in_list(list):
	count1 = len(list)
	remove_dup = set(list)
	count2 = len(remove_dup)
	if count1 == count2:
		return False
	else:
		return True



directoris = ["L_the_patient", "U_Patient", "U_The_patient"]
keyword = ["the patient", "Patient", "The patient"]
genders = ["female", "male", "universal"]

dir_count = 0

for dir_index in directoris:
	for gender_index in genders:
		dir = "letters/"+dir_index+"/"+gender_index+"/"
		path = os.fsencode(dir)
#dir1 = "testfile/U_The_patient/universal/"
#path1 = os.fsencode(dir1)
#test = os.fsencode("letters/test/")

		for file in os.listdir(path):
		    filename = os.fsdecode(file)
		    print(filename)
		    if filename != ".DS_Store":
			    f = open(dir+filename,'r')
			    filedata = f.read()
			    f.close()

			    new_name = generate_name(gender_index)
			    newdata = filedata.replace(keyword[dir_count],new_name,1)
			    f = open(dir+filename,'w')
			    f.write(new_name+"\n")
			    f.write(newdata)
			    f.close()
	dir_count = dir_count + 1

print(name_list)

if duplicate_exists_in_list(name_list):
	print("DUPLICATE!")
else:
	print("passed sanity check test")
# name = names.get_full_name()
# if name not in name_list:
# 	replace_name()
