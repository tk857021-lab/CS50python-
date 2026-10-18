'''names = []

for i in range(3):
    names.append(input("name: "))

for name in sorted(names):
    print(f"hello, {name}")
'''



'''name = input("what is name? ")
file = open("name.txt","a")
file.write(f"{name}\n")
file.close()'''



"""name = input("what is name? ")

with open("name.txt","a") as file:
    file.write(f"{name}\n")"""

"""with open("name.txt","r") as file:
    lines=file.readlines()

for line in lines:
    print("hello,",line)"""



"""with open("name.txt","r") as file:
    lines=file.readlines()

for line in lines:
    print("hello,",line.rstrip())"""





"""with open("name.txt","r") as file:
  for line in file:
     print("hello,",line.rstrip())
"""


"""names = []
with open("name.txt") as file:
  for line in file:
     names.append(line.rstrip())

for name in sorted(names,reverse=True):
   print(f"hello, {name}")"""




"""with open("students.csv") as file:
  for line in file:
     row = line.rstrip().split(",")
     print(f"{row[0]} is in {row[1]}")
"""



"""students = []

with open("students.csv") as file:
  for line in file:
     name,house = line.rstrip().split(",")
     students.append(f"{name} is in {house}")

for stundent in students:
print(student)"""


"""
students = []

with open("students.csv") as file:
  for line in file:
     name,house = line.rstrip().split(",")
     student = {"name":name, "house":house}
     students.append(student)

def get_name(student):
   return student["name"]

for student in sorted(students, key=get_name):
 print(f"{student['name']} is in {student['house']}")"""




"""students = []

with open("students.csv") as file:
  for line in file:
     name,house = line.rstrip().split(",")
     student = {"name":name, "house":house}
     students.append(student)

for student in sorted(students, key=lambda student:student["name"]):
 print(f"{student['name']} is in {student['house']}")
"""
"""import csv


students = []

with open("students.csv") as file:
  reader = csv.reader(file)
  for name,home in reader:
    students.append({"name":name, "home":home})
for student in sorted(students, key=lambda student:student["name"]):
 print(f"{student['name']} is in {student['home']}")
"""


"""import csv


students = []

with open("students.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    students.append({"name":row["name"], "home":row["home"]})
for student in sorted(students, key=lambda student:student["name"]):
 print(f"{student['name']} is from {student['home']}")
"""


"""import csv
name = input("name: ")
home = input("home: ")

with open("students.csv","a") as file:
  writer = csv.writer(file)
  writer.writerow([name, home])"""


import csv
name = input("name: ")
home = input("home: ")

with open("students.csv","a") as file:
  writer = csv.DictWriter(file, fieldnames=["name","home"])
  writer.writerow({"name":name,"home":home})
