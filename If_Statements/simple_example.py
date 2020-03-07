cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#checking if a value its in a list

print('audi' in cars)

#checking if a value its NOT in a list

if 'bmw' not in cars:
    print(f"bmw it's not in {cars}")
else:
    print(f"bmw it's in the list {cars}")