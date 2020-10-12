from datetime import datetime

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{Menu} is avaiable from: {start}:{end}".format(Menu = self.name, start = self.start_time, end = self.end_time)
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
    return bill
  
  
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu('Brunch', brunch_items, 11, 16)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird = Menu('Early-bird Dinners', early_bird_items, 15, 18)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu('Dinner', dinner_items, 17, 23)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu('Kids', kids_items, 11, 21)

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas = Menu('Take a\' Arepa', arepas_items, 10, 8)

#print(brunch, '\n', early_bird, '\n', dinner, '\n', kids)

#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

class Franchise:

  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
      return "Our store is located at {location}".format(location = self.address)

  def available_menus(self, time):
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menu_list.append(menu)
    return menu_list

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

#print(new_installment)

#print(flagship_store.available_menus(12))

#print(flagship_store.available_menus(17))

class Business:

  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

actual_biz = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

arepas_place = Franchise('189 Fitzgerald Avenue', arepas)

arepa_biz = Business('Take a\'Arepa!', arepas_place)

#print(arepa_biz.franchises.menus)
