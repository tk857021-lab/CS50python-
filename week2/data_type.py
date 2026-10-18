"""
       list
students=["tushar","bharat","monu"]
for i in range(len(students)):
    print(i+1,students[i])
"""
"""
   #dictionaries
students ={
    "tushar":"katara",
    "bharat":"patak"
}

print(students["tushar"])
print(students["bharat"])


    #print dict with for

for student in students:
    print(students[student])
"""
    #list of dictionaries
students= [
    {"name":"tushar", "house":"blue", "sec_name":"katara" },
    {"name":"bharat", "house":"blue", "sec_name":"patak"}]

for student in students:
   print(student["name"],student["house"],sep=", ")
