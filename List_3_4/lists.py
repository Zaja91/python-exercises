motocycles = ['honda', 'ducati', 'yamaha', 'ducati']
print(motocycles)


for m in motocycles:
  if m == 'ducati':
    motocycles.remove(m)

print(motocycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
for car in cars:
  print(f'{car.title()}')

for value in range(1,5):
  print(value)

numbers = list(range(2,12,2))
print(numbers)

squares = [value**2 for value in numbers]
print(squares)

print(squares[0:3]) # per capire quanti ne printa basta fare 3 - 0 = 3
print(squares)

print(squares[1:4]) # 4 - 1 = 3 a partire dal indice 1

# primi 3 [:3] ultimi 3  [-3:]

print("Here are the first 3 numbers:")

for n in numbers[:3]:
  print(n)

print("Here are the last 3 numbers")

for n in numbers[-3:]:
  print(n)

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Con metodo slice creiamo un nuovo array mentre se faccio friend_foods = my_foods entrambi puntano allo
# stesso obj in memoria e se modifico il primo cambia anche il secondo perche cambia il valore in memoria al quale puntano entrambi

# ---------------->>>>>>><<<<<<<<<----------------------

#An immutable list its called a tuple in python

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# We can't change dimension[0] = 250 because it's immutable 



