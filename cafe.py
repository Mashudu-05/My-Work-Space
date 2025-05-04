menu = ['Donuts', 'Cold Coffee', 'Tomato Soup', 'Veg Sandwich', 'Burger']

stock = {'Donuts': 4, 'Tomato Soup': 5, 'Veg Sandwich': 8,
         'Burger': 10, 'Cold Coffee': 10}

# price, has cost of each menu item
price = {'Donuts': 10.00, 'Tomato Soup': 9.99, 'Veg Sandwich': 15.0,
         'Burger': 25.0, 'Cold Coffee': 12.0}

# total stock worth of cafe items
total_stock = 0.0

for item in menu:
    
    quantity = stock[item]
    cost = price[item]
    
    total_stock = total_stock + quantity * cost

print('Total stock worth of cafe items: R', total_stock)
 
