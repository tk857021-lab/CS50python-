class Calulater:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def mulitply(self):
        return self.num1 * self.num2


x = int(input("x: "))
y = int(input("y: "))

cal = Calulater(x, y)


answer = cal.mulitply()
print(f"this is {answer}")

