"""class  Dog:
    def __init__(self, name , breed,owner):
        self.name=name
        self.breed=breed
        self.owner = owner

    def bark(self):
        print("boo boo")

class owner:
    def __init__(self, name,address,contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

owner1= owner("tushar","bk","dcb")
dog1 = Dog("b","a", owner1)
dog1.bark()
print(f"{dog1.name},{dog1.breed}")

owner2= owner("tushar","bk","indl")
dog2 = Dog("c","o", owner2)
dog2.bark()
print(f"{dog2.name},{dog2.breed}")
"""
###############

"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Greet(self):
        print(f"this is you {self.name} and this is your {self.age}")


greet = Person("tushar","18")
greet.Greet()"""
####################
""""class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        # Combined into a single line to fix the SyntaxError
        print(f"Message sent to {user.username}: hi {user.username}, it's {self.username}")

user1 = User("batman", "bat.gmail", 123)
# Changed 000 to "000" because Python does not allow leading zeros for integers
user2 = User("tushar", "tu.gmail", "000")

user1.say_hi_to_user(user2)"""
################################################

"""
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    def clean_email(self):
        return self._email.lower().strip()

user1 = User("batman", "   bhatman,ji.gmail   ", 123)

print(user1.clean_email())

"""

##############

"""class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    def get_email(self):
        return self._email
    def set_email(self,new_email):
         if "@" in new_email:
          self._email = new_email



user1 = User("batman", "batman,ji.gmail", 123)

print(user1.get_email())

user1.set_email("bhatman,ji.gmail")
print(user1.get_email())

"""
###############################################
""""
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    @property
    def email(self):
        print("email assesed")
        return self._email
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("batman", "batman,ji.gmail", 123)
user1.email = "bhatman,ji@.gmail"
print(user1.email)



"""

######################"""##########################

'''class User:
    user_count = 0

    def __init__(self, username,email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username},email: {self.email}")

user1 = User("tushar","tu.@gmail")
user2 = User("bhatman,ji","bhatman,ji.@gmail")


print(User.user_count)'''
###################################


""""class BankAccount:
    MIN_BALANCE = 100
    def __init__(self,owner ,balance):
        self.owner = owner
        self._balance = balance
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit",amount)
        else:
            print("deposit amount must be positive")
    def _is_valid_amount(self,amount):
        return amount > 0
    def __log_transaction(self, transaction_type,amount):
        print(f"logging {transaction_type} of ${amount}.new balance:${self._balance}")



    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5

account = BankAccount("tushar", 1000)
money = int(input("money: "))
account.deposit(money)
"""
####################################
"""

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1

print(account.balance)
"""
"""
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self._balance += amount

    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("insufficant fund")
        self._balance -= amount

account = BankAccount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)"""

#########################################################
"""
class EmailServer:

    def _connect(self):
        print("connect to email server")

    def _authentication(self):
        print("authenticatig ...")

    def send_email(self):
        self._connect()
        self._authentication
        print("send email...")
        self._disconnect()

    def _disconnect(self):
        print("disconnecting from server...")"""

"""
class Vehicle:
    def __init__(self,brand,modal,year):
        self.brand = brand
        self.modal = modal
        self.year = year

    def start(self):
        print("Vehicla is starting ")

    def stop(self):
        print("Vehicla is stoping")



class CAR(Vehicle):
    def __init__(self,brand,modal,year,number_of_door,number_of_wheels):
        super().__init__(brand,modal,year)
        self.number_of_door = number_of_door
        self.number_of_wheels = number_of_wheels


class Bike(Vehicle):
    def __init__(self,brand,modal,year,number_of_wheels):
        super().__init__(brand,modal,year)
        self.number_of_wheels = number_of_wheels


ford = CAR("ford","marstag",1970,4,4)
honda = Bike("honda","palser",2016,2)
print(ford.__dict__)
print(honda.__dict__)
ford.start()
honda.start()
"""

##############################################




class Vehicle:
    def __init__(self,brand,modal,year):
        self.brand = brand
        self.modal = modal
        self.year = year

    def start(self):
        print("Vehicla is starting ")

    def stop(self):
        print("Vehicla is stoping")



class CAR(Vehicle):
    def __init__(self,brand,modal,year,number_of_door,number_of_wheels):
        super().__init__(brand,modal,year)
        self.number_of_door = number_of_door
        self.number_of_wheels = number_of_wheels


class Bike(Vehicle):
    def __init__(self,brand,modal,year,number_of_wheels):
        super().__init__(brand,modal,year)
        self.number_of_wheels = number_of_wheels

vehicles = [
CAR("ford","marstag",1970,4,4),
Bike("honda","palser",2016,2)
]



for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Instance {vehicle.brand},{vehicle.modal}({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()

    else:
        raise Exception("object is not valid")
