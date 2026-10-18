"""email = input("email: ")
if "@" in email and "." in email :
    print("valid")
else:
    print("invalid")
"""

"""
email = input("email: ")
username, domain = email.split("@")

if (username) and ("." in domain) :
    print("valid")
else:
    print("invalid")"""



"""email = input("email: ")
username, domain = email.split("@")

if (username) and domain.endswith(".com") :
    print("valid")
else:
    print("invalid")"""

"""
import re

email = input("email: ")
if re.search("@", email):
     print("valid")
else:
     print("invalid")"""



"""import re

email = input("email: ")
if re.search(".*@.*", email):
     print("valid")
else:
     print("invalid")
"""


"""import re

email = input("email: ")
if re.search(".+@.+", email):
     print("valid")
else:
     print("invalid")
"""

"""
import re

email = input("email: ")
if re.search(r".+@.+.com", email):
     print("valid")
else:
     print("invalid")
"""


"""import re

email = input("email: ")
if re.search(r"^.+@.+.com$", email):
     print("valid")
else:
     print("invalid")
"""


"""import re

email = input("email: ")
if re.search(r"^[^@]+@[^@]+.com$", email):
     print("valid")
else:
     print("invalid")"""



"""import re

email = input("email: ")
if re.search(r"^cs50.python
w+@w+.com$", email):
     print("valid")
else:
     print("invalid")"""

"""name= input("name: ").strip()
if "," in name:
    last ,first = name.split(", ")
    name = f"{first}{last}"
print(f"hello, {name}")
"""
"""import re
name= input("name: ").strip()
matching = re.search(f"^(.+), (.+)+$", name)
if matching:
    last ,first = matching.groups()
    name = f"{first}{last}"
print(f"hello, {name}")
"""


"""import re
name= input("name: ").strip()
matching = re.search(f"^(.+), (.+)+$", name)
if matching:
    name = matching.group(2) +" "+matching.group(1)
print(f"hello, {name}")"""

import re
url = input("url: ").strip()
username = re.sub(r"https://twitter.com/", "", url)
print(f"username, {username}")
