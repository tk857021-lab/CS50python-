from lab import square
import pytest


def main():
   test_square()

"""def test_square():
    if square(2) != 4:
       print("4 is not a square of 2 ")
    if square(3) != 9:
           print("3 is not a square of 9")
    if square(4) != 16:
       print("4 is not a square of 16")
"""
"""
def test_square():
   try:
     assert square(2) == 4
   except AssertionError:
     print("4 is not square")
   try:
     assert square(4) == 16
   except AssertionError:
      print("16 is not square")
"""
def test_square():
   assert square(2) == 4
   assert square(3) == 9
   assert square(-2) == 4
   assert square(0) == 0

def test_str():
   with pytest.raises(TypeError):
      square("cat")
if __name__=="__main__":
   main()

