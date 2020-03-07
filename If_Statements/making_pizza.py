toppings = []

available_toppings = ('pomodoro', 'mozarella', 'funghi', 'salsiccia', 'alici', 'wurstel')

print(f"Questa e la lista delle possibili scelte per creare la tua pizza: ")
for topping in available_toppings:
    print(topping.title())

client_choice = []

print("Schegli un ingrediente dalla lista per uscire digita 'quit'")
    #prego schegli il tuo ingrediente + per uscire digita "quit"
    #se l'ingrediente rientra nella scelta del available aggiungi al client_choice
    #altrimenti richiedi ancora

user_choice = input("Schegli:")

