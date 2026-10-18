"""def main():
    name ,house = get_student()
    print(f"{name} is in {house}")

def get_student():
    n = input("name: ")
    h = input("house: ")
    return n,h
if __name__=="__main__":
    main()
"""
"""
def main():
    student = get_student()
    if student['name'] == "batman":
        student['name'] = "bhatman"
    print(f"{student['name']} is in {student['house']}")

def get_student():
    student ={}
    name = input("name: ")
    house = input("house: ")
    return {"name":name,"house":house}
if __name__=="__main__":
    main()
"""


class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def student(self):
        print(f"{self.name} form {self.house}")
student = Student("bhatman" , "batcave" )
student.student()


