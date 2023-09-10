# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)
array = [1,6,2,1]
print(flatten_and_sort(array))

# How does this solution ensure data immutability? 
#1)The function does not affect the evirorment of its input. Instead it creates a new array using the data from the array that already exists
# Is this solution a pure function? Why or why not? 
# 2)Yes. The function produces same output given the same input. The function produces no side effects. The function does not rely on external state.
# Is this solution a higher order function? Why or why not? 
# 3)It is not a higher order function. It does not accept one or more functions as an argument, and it does not return a function.
# Would it have been easier to solve this problem using a different programming style?
# 4)No,this style is simple, avoids verbosity, and is efficient. the builtin method "sorted" allows you to arrange the iterable in ascending order.
# Why in particular is functional programming a helpful paradigm when solving this problem? 
# 5)As a declarative programming style, its main focus is What to solve, as opposed to an imperative style focusing on How to solve. This solves problems in a very simple, effective way.



# OOP 
# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply) 
# Encapsulation: It keeps max speed, condition, etc in the base class and extended classes use those base class attributes.
# Abstraction: Abstracts away methods for indicating repair and setting intitial values.
# Inheritance: Each pod inherits the condition and other aspects of the pod parent.
# Polymorphism - You can call the repair method on any decendent of pod.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
#2) No, object oriented programming makes code more reusable, and makes it easier to work within larger programs.


# How in particular did Object Oriented Programming assist in the solving of this problem?
# 3)By using the Podracer class template and creating a sebulbaspod in the classes Anakinspod


# Is one of the coding paradigms "better" than the other? Why or why not? 
# 4) No, they each have their respective use cases.

# Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why? 
# 5) Object-Oriented Programming seems more appealing because it makes coding faster as its reusable instead of rewriting the same code over and over

# Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
# 6) Functional programming appears to be more limited if the dataset is complex, where as OOP is more flexible (appears to be)

# Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
# 7)OOP takes more effort to understand. Practice more to deepen understanding, as is typical.