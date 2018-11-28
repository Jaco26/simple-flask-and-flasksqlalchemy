
class Person:
  def __init__(self, name, age, food):
    self.name = name
    self.age = int(age)
    self.food = food

  def say_hello(self):
    return 'Hello! My name is {}'.format(self.name)
  
  def json(self, *args):
    if args:
      accum = {}
      for arg in args:
        accum[arg] = self.__dict__[arg]
      return accum
    return self.__dict__

  
jacob = Person('Jacob', 27)

# print(jacob.__dict__)
print(jacob.json('age'))
