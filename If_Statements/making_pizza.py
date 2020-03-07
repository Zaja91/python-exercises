toppings = []

available_toppings = ('pomodoro', 'mozarella', 'funghi', 'salsiccia', 'alici', 'wurstel')

print(f"Questa e la lista delle possibili scelte per creare la tua pizza: {available_toppings}")

still_choosing = True

while still_choosing:
    name = input("\n What ingredient do you want:")
    toppings.append(name)

    if name == 'quit':
        still_choosing = False

toppings.pop()
print(f"La tua pizza: {toppings}")


