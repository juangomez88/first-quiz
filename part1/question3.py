################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class Oven:
  def __init__(self):
    self.contents = []

  def add(self, item):
    self.contents.append(item)

  def freeze(self):
    self.contents = ["snow"]

  def boil(self):
    if "cheese" in self.contents and "dough" in self.contents and "tomato" in self.contents:
      self.contents = ["pizza"]
    elif "lead" in self.contents and "mercury" in self.contents:
      self.contents = ["gold"]
    else:
      self.contents = ["unknown"]

  def wait(self):
    pass

  def get_output(self):
    return self.contents[0] if self.contents else "unknown"

def make_oven():
  return Oven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()

  def test_alchemy_combine():
    assert alchemy_combine(
      make_oven(),
      ["lead", "mercury"],
      5000
    ) == "gold"

    assert alchemy_combine(
      make_oven(),
      ["water", "air"],
      -100
    ) == "snow"

    assert alchemy_combine(
      make_oven(),
      ["cheese", "dough", "tomato"],
      150
    ) == "pizza"