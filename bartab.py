class Tab:

  menu = {
    'wine': 5,
    'beer': 3,
    'soft_drink': 2,
    'chicken': 10,
    'beef': 15,
    'veggie': 12,
    'cake': 6,
    'cookies': 4
  }

  def __init__(self):
    self.total = 0
    self.items = [ ]

  def add(self, item):
    self.items.append(item)
    self.total += self.menu[item]

  def print_bill(self, tax, service):
    tax = (tax/100) * self.total
    service = (service/100) * self.total
    total = self.total + tax + service

    for item in self.items:
      print(f'{item:20} ${self.menu[item]}')

    print(f'{"Total":20} ${total}:.2f')





















# this is how you comment in python
# python3 to type python in command line
# ctrl z to get out

# name = input('Tell me your name:')
# age = input('and your age?')
# print(name, 'you are', age)

# Calc the area of a circle
# change string into a number by int()
# radius = input('Enter the radius of your circle:')
# area = 3.142 * int(radius) ** 2
# print('The area of your circle is:', area)

# PREVIOUS print method
# print('num 1 is', num1, 'and num 2 is', num2)
# num1 = 33
# num2 = 1011
# FORMAT print method
# print('num 1 is {0} and num 2 is {1}'.format(num1, num2))

# For Loops
# ninjas = ['ryu', 'crystal', 'yoshi', 'ken']
# for ninja in ninjas:
#   if ninja == 'yoshi':
#     print(f'{ninja} - black belt')
#     break
#   else:
#     print(ninja)

# def function(parameters):
  # print(here)
# dictionaries are like key object pairs